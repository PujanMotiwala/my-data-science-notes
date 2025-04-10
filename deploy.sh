#!/bin/bash

# Script to run local preprocessing, then add, commit,
# and push source changes to trigger GitHub Actions deployment.

# --- Configuration ---
COMMIT_MESSAGE="Update notes $(date +'%Y-%m-%d %H:%M:%S')" # Default commit message with timestamp
BRANCH="main" # Or "master" if that's your primary branch
PYTHON_SCRIPT_NAME="preprocess_notes.py" # Assuming it's in the root directory

# --- Script Logic ---

echo "Running local preprocessing script ($PYTHON_SCRIPT_NAME)..."
# Run the python script. Exit immediately if the script fails.
python "$PYTHON_SCRIPT_NAME" || exit 1
echo "Preprocessing script finished successfully."
echo "(Output is in 'docs_build/' - this directory should be in .gitignore)"
echo "--------------------------------------------------"

# Continue with Git operations only if preprocessing succeeded

echo "Adding files to Git (staging changes in 'docs/' and other tracked files)..."
git add .

echo "Committing changes..."
# Check if there are changes staged for commit
if git diff --staged --quiet; then
  echo "No changes staged to commit."
else
  git commit -m "$COMMIT_MESSAGE"
fi

echo "Pushing source changes to origin/$BRANCH..."
git push origin $BRANCH

echo "--------------------------------------------------"
echo "Push complete. GitHub Actions should now be building and deploying your site."
echo "Remember: Actions need to run '$PYTHON_SCRIPT_NAME' before 'mkdocs build --docs-dir docs_build'."
echo "Check the Actions tab in your GitHub repository for progress."
echo "--------------------------------------------------"