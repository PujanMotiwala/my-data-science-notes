import os
import re
import pathlib
import sys
import yaml
from io import StringIO

# --- Configuration ---
DOCS_DIR = pathlib.Path("docs") # Root of your notes
BUILD_DIR = pathlib.Path("docs_build") # Temporary directory for processed files
TAGS_HEADING = "## TAGS" # The exact heading introducing the tags section
TAG_PATTERN = re.compile(r"\[\[([^\]]+)\]\]") # Extracts content within [[...]]

# --- Helper Functions ---

def extract_existing_yaml(content_lines):
    """Extracts existing YAML front matter dict and the rest of the content lines."""
    if content_lines and content_lines[0].strip() == '---':
        try:
            end_yaml_index = content_lines[1:].index('---') + 1
            yaml_content = "\n".join(content_lines[1:end_yaml_index])
            # Use safe_load, default to empty dict if YAML is empty or just whitespace
            front_matter = yaml.safe_load(yaml_content)
            if front_matter is None:
                front_matter = {}
            elif not isinstance(front_matter, dict):
                 print(f"  Warning: Existing YAML front matter is not a dictionary. Treating as empty.", file=sys.stderr)
                 front_matter = {} # Treat non-dict YAML as empty for merging
            main_content_lines = content_lines[end_yaml_index + 1:]
            return front_matter, main_content_lines
        except (ValueError, yaml.YAMLError) as e:
            print(f"  Warning: Error parsing existing YAML: {e}. Treating as no YAML.", file=sys.stderr)
            # Fall through if error parsing YAML
            pass
    return {}, content_lines # No YAML or error parsing

def extract_and_find_tags_section(content_lines):
    """Finds the start index of the TAGS section and extracts tags from it."""
    tags = []
    tags_section_start = -1
    try:
        # Find the index of the TAGS heading (case-insensitive)
        tags_section_start = next(i for i, line in enumerate(content_lines)
                                   if line.strip().lower() == TAGS_HEADING.strip().lower())

        # Extract tags from lines *after* the heading
        for line in content_lines[tags_section_start + 1:]:
             # Stop if another heading of the same or higher level is found (optional, for safety)
             # if line.strip().startswith('#'):
             #      break
            for match in TAG_PATTERN.finditer(line):
                tag = match.group(1).strip()
                # Avoid adding links with paths/aliases as tags, check for simple names
                # This is heuristic: assumes simple tags don't have typical file path chars
                if tag and '/' not in tag and '\\' not in tag and '#' not in tag and '|' not in tag:
                    if tag not in tags: # Avoid duplicates
                        tags.append(tag)

    except StopIteration:
        # TAGS heading not found
        tags_section_start = -1

    return tags, tags_section_start

def format_yaml_front_matter(data):
     """Formats dictionary into YAML front matter string."""
     if not data:
          return ""
     # Use StringIO to capture YAML output with desired formatting
     string_stream = StringIO()
     yaml.dump(data, string_stream, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000) # Keep keys in order, allow unicode, prevent weird wrapping
     yaml_output = string_stream.getvalue()
     return f"---\n{yaml_output.strip()}\n---\n"


def process_file(src_path, dest_path):
    """Reads src, extracts tags, adds YAML, removes tag section, writes to dest."""
    print(f"Processing: {src_path}")
    try:
        content_lines = src_path.read_text(encoding="utf-8").splitlines()
        original_content = "\n".join(content_lines) # For comparison

        # Step 1: Extract existing YAML and tags from ## TAGS section
        front_matter, main_content_lines = extract_existing_yaml(content_lines)
        extracted_tags, tags_section_start = extract_and_find_tags_section(main_content_lines)

        # Step 2: Prepare the final content (without the ## TAGS section)
        final_main_lines = main_content_lines
        if tags_section_start != -1:
            # Keep only lines *before* the TAGS heading
            final_main_lines = main_content_lines[:tags_section_start]
        final_main_content_str = "\n".join(final_main_lines)

        # Step 3: Update YAML front matter with extracted tags
        yaml_changed = False
        if extracted_tags:
            existing_tags = front_matter.get('tags', [])
            if not isinstance(existing_tags, list):
                print(f"  Warning: Existing 'tags' in YAML is not a list for {src_path}. Overwriting.", file=sys.stderr)
                existing_tags = [] # Overwrite if not a list

            original_tag_count = len(existing_tags)
            # Add only new tags
            for tag in extracted_tags:
                if tag not in existing_tags:
                    existing_tags.append(tag)

            if len(existing_tags) > original_tag_count:
                 front_matter['tags'] = sorted(list(set(existing_tags))) # Ensure uniqueness and sort
                 yaml_changed = True
            elif 'tags' not in front_matter and extracted_tags: # Add key if it didn't exist
                 front_matter['tags'] = sorted(list(set(extracted_tags)))
                 yaml_changed = True

        # Step 4: Reconstruct final file content
        final_yaml_str = format_yaml_front_matter(front_matter)
        # Ensure there's exactly one newline between YAML and content, unless one is empty
        separator = "\n" if final_yaml_str and final_main_content_str else ""
        final_content = final_yaml_str + separator + final_main_content_str

        # Preserve trailing newline if original had one
        if original_content.endswith('\n') and not final_content.endswith('\n'):
             final_content += '\n'
        elif not original_content.endswith('\n') and final_content.endswith('\n'):
             final_content = final_content.rstrip('\n')

        # --- Step 5: Write if Changed ---
        if final_content != original_content:
            print(f"  Changes detected (YAML update or TAGS removal). Writing to build dir...")
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            dest_path.write_text(final_content, encoding="utf-8")
            # print(f"  File written: {dest_path}")
            return True # Indicate modification occurred
        else:
            # If no change, still ensure file exists in build dir (copy if needed)
            if not dest_path.exists():
                 dest_path.parent.mkdir(parents=True, exist_ok=True)
                 dest_path.write_text(original_content, encoding="utf-8")
            # print(f"  No changes needed for {src_path}.")
            return False

    except Exception as e:
        print(f"  ERROR processing file {src_path}: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    import shutil

    print(f"Source directory: {DOCS_DIR.resolve()}")
    print(f"Build directory: {BUILD_DIR.resolve()}")

    # Clean build directory before starting
    if BUILD_DIR.exists():
        print(f"Cleaning build directory: {BUILD_DIR}")
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(exist_ok=True)

    modified_count = 0
    file_count = 0
    copy_count = 0

    print("Processing files...")
    # Iterate through everything in the source directory
    for src_item in DOCS_DIR.rglob('*'):
        relative_path = src_item.relative_to(DOCS_DIR)
        dest_item = BUILD_DIR / relative_path

        if src_item.is_dir():
            dest_item.mkdir(parents=True, exist_ok=True)
        elif src_item.is_file():
            file_count += 1
            # Process only Markdown files
            if src_item.suffix.lower() == '.md':
                if process_file(src_item, dest_item):
                    modified_count += 1
            else:
                # Copy other files directly
                dest_item.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_item, dest_item) # copy2 preserves metadata
                copy_count += 1
        else:
             print(f"Skipping unknown item type: {src_item}", file=sys.stderr)


    print(f"\nScan complete. Processed {file_count} markdown files.")
    print(f"Copied {copy_count} non-markdown files.")
    print(f"Modified {modified_count} markdown files (YAML update or TAGS removal).")
    print(f"Build ready in: {BUILD_DIR}")
    print(f"\nNow run 'mkdocs build/serve/deploy' using '{BUILD_DIR.name}' as the --docs-dir argument,")
    print(f"or configure your CI/CD to build from '{BUILD_DIR.name}'.")
    print("Example: mkdocs build --config-file mkdocs.yml --docs-dir docs_build")