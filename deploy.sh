#!/bin/bash

# Simple script to add, commit, and push changes to the main branch,
# which will trigger the GitHub Actions deployment workflow.

# --- Configuration ---
COMMIT_MESSAGE="Update notes $(date +'%Y-%m-%d %H:%M:%S')" # Default commit message with timestamp
BRANCH="main" # Or "master" if that's your primary branch

# --- Script Logic ---
echo "Adding files to Git..."
git add .

echo "Committing changes..."
# Check if there are changes staged
if git diff --staged --quiet; then
  echo "No changes to commit."
else
  git commit -m "$COMMIT_MESSAGE"
fi

echo "Pushing changes to origin/$BRANCH..."
git push origin $BRANCH

echo "--------------------------------------------------"
echo "Push complete. GitHub Actions should now be deploying your site."
echo "Check the Actions tab in your GitHub repository for progress."
echo "--------------------------------------------------"
