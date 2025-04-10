import os
import pathlib
import yaml
import re

# --- Configuration ---
DOCS_DIR = pathlib.Path("docs")
PAGES_FILENAME = ".pages"
# Exclude common non-content items
EXCLUDE_DIRS = {'.obsidian', 'Excalidraw', 'assets'}
EXCLUDE_FILES = {'.DS_Store', PAGES_FILENAME}

# --- Helper Functions ---

def natural_sort_key(s):
    """Sorts strings with numbers naturally (e.g., 1, 2, 10)."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', str(s))]

def generate_title(path):
    """Generate a default title from a filename or directory name."""
    name = path.stem if path.is_file() else path.name
    if name.lower() == 'index':
        # Use parent directory name for index files, capitalize words
        parent_name = path.parent.name
        # Remove leading digits/underscores for title
        clean_name = re.sub(r"^\d+[-_]?", "", parent_name).replace('_', ' ').replace('-', ' ')
        return clean_name.title() if clean_name else "Overview" # Fallback for root index

    # Remove leading digits/underscores, replace underscores/dashes, title case
    clean_name = re.sub(r"^\d+[-_]?", "", name).replace('_', ' ').replace('-', ' ')
    return clean_name.title()

def generate_pages_file(directory_path):
    """Creates or updates the .pages file for a given directory."""
    pages_file_path = directory_path / PAGES_FILENAME
    existing_nav = {}
    existing_data = {}

    # Read existing file to preserve manual settings if possible
    if pages_file_path.exists():
        try:
            with open(pages_file_path, 'r', encoding='utf-8') as f:
                existing_data = yaml.safe_load(f) or {}
                if isinstance(existing_data.get('nav'), list):
                    # Create a map for easier lookup and order preservation
                    for item in existing_data['nav']:
                        if isinstance(item, dict):
                            key = list(item.keys())[0]
                            value = list(item.values())[0]
                            existing_nav[value] = key # Store as path: title
                        elif isinstance(item, str):
                             existing_nav[item] = None # Store path with no title override
        except Exception as e:
            print(f"  Warning: Could not read or parse existing {pages_file_path}: {e}", file=sys.stderr)
            existing_nav = {}
            existing_data = {}


    # Scan directory contents
    items = []
    for item in directory_path.iterdir():
        if item.name in EXCLUDE_FILES or item.name in EXCLUDE_DIRS:
            continue
        if item.is_dir() and not any(item.iterdir()): # Skip empty dirs maybe?
             continue
        if item.is_file() and item.suffix.lower() != '.md':
            continue
        items.append(item)

    # Sort items (e.g., naturally by name)
    items.sort(key=lambda x: natural_sort_key(x.name))

    # Build the new nav list
    new_nav_list = []
    found_paths_in_dir = set()

    for item in items:
        item_path_str = item.name
        if item.is_dir():
            item_path_str += '/' # Indicate directory link for awesome-pages
        found_paths_in_dir.add(item_path_str)

        # Get title: Use existing if available, otherwise generate
        title = existing_nav.get(item_path_str, generate_title(item))

        if title:
            new_nav_list.append({title: item_path_str})
        else: # Should always generate a title, but fallback
             new_nav_list.append(item_path_str)

    # Optionally: Check existing_nav for items that no longer exist and remove them? (More complex)

    # Prepare data to write
    output_data = existing_data # Start with existing data (like title)
    output_data['nav'] = new_nav_list

    # Only write if there's something to navigate to
    if new_nav_list:
        try:
            print(f"  Writing {pages_file_path}")
            with open(pages_file_path, 'w', encoding='utf-8') as f:
                yaml.dump(output_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        except Exception as e:
             print(f"  ERROR writing {pages_file_path}: {e}", file=sys.stderr)


# --- Main Execution ---
if __name__ == "__main__":
    print(f"Generating .pages files in: {DOCS_DIR.resolve()}")
    # Walk through all directories in DOCS_DIR
    for dirpath, dirnames, filenames in os.walk(DOCS_DIR, topdown=True):
        # Modify dirnames in place to exclude certain directories from recursion
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

        current_dir = pathlib.Path(dirpath)
        # Check if the current directory has relevant content (.md files or non-excluded subdirs)
        has_content = any(f.endswith('.md') and f not in EXCLUDE_FILES for f in filenames) or \
                      any(d in dirnames for d in os.listdir(current_dir) if (current_dir / d).is_dir() and d not in EXCLUDE_DIRS)

        if has_content:
             print(f"\nProcessing directory: {current_dir}")
             generate_pages_file(current_dir)

    print("\n.pages file generation complete.")