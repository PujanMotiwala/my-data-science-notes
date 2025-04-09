# My Data Science Notes

[![Deploy MkDocs Site](https://github.com/pujanmotiwala/my-data-science-notes/actions/workflows/deploy.yml/badge.svg)](https://github.com/pujanmotiwala/my-data-science-notes/actions/workflows/deploy.yml)

Welcome to my personal collection of notes covering various topics within the field of Data Science. This repository contains the source files (primarily Markdown) for a website built using MkDocs. Think of it as a digital garden or a living document capturing my learning journey.

---

➡️ **[View the Live Site Here](https://pujanmotiwala.github.io/my-data-science-notes/)** ⬅️

---

## Overview

This site includes notes on:

*   Foundational Mathematics (Probability, Statistics, Linear Algebra, Calculus)
*   Data Collection and Processing
*   Feature Engineering
*   Data Visualization
*   Machine Learning (Supervised, Unsupervised, Evaluation, Tuning)
*   Deep Learning (Neural Networks, CNNs, RNNs, Transformers, Advanced Topics)
*   Big Data Technologies
*   Ethics, Bias, and Responsible AI
*   Related tools and techniques (Python, Git, SQL, etc.)

The notes originate from my personal knowledge base, often maintained using [Obsidian](https://obsidian.md/), and are rendered into a static website for easy access and sharing.

## Features (Website)

The generated website includes:

*   **Clean & Responsive Design:** Uses the excellent [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.
*   **Dark/Light Mode:** User-selectable theme preference.
*   **Fast Search:** Built-in client-side search functionality.
*   **Code Syntax Highlighting:** Supports highlighting for various programming languages.
*   **Diagram Rendering:** Integrates [Kroki](https://kroki.io/) for rendering diagrams (including Excalidraw).
*   **Navigation:** Sidebar navigation mirroring the note structure.
*   **Obsidian Link Compatibility:** Uses plugins (like `mkdocs-roamlinks-plugin`) to handle `[[WikiLink]]` style linking where possible.

## Technology Stack

*   **Note Source:** [Obsidian](https://obsidian.md/) & Markdown (`.md`) files.
*   **Static Site Generator:** [MkDocs](https://www.mkdocs.org/)
*   **Theme:** [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
*   **Key MkDocs Plugins:**
    *   `mkdocs-material` (Theme provides many features)
    *   `mkdocs-kroki-plugin` (For diagram rendering)
    *   `mkdocs-roamlinks-plugin` (To resolve `[[WikiLinks]]`)
    *   `mkdocs-exclude` (If used for excluding specific files/folders)
    *   Various `pymdown-extensions` for enhanced Markdown rendering (Admonitions, Tasklists, MathJax, etc.)
*   **Hosting:** [GitHub Pages](https://pages.github.com/)
*   **CI/CD:** [GitHub Actions](https://github.com/features/actions)

## Local Development

To run this site locally for development or exploration:

1.  **Prerequisites:**
    *   [Git](https://git-scm.com/)
    *   [Python](https://www.python.org/) (Version 3.8+ recommended, ideally matching the version used in GitHub Actions, e.g., 3.10)
    *   `pip` (Python package installer, usually comes with Python)

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/pujanmotiwala/my-data-science-notes.git
    cd my-data-science-notes
    ```

3.  **Set up Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # Activate the environment:
    # Linux/macOS:
    source venv/bin/activate
    # Windows (Git Bash/WSL):
    # source venv/Scripts/activate
    # Windows (Command Prompt/PowerShell):
    # .\venv\Scripts\activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Development Server:**
    ```bash
    mkdocs serve
    ```

6.  **View Locally:** Open your web browser and navigate to `http://127.0.0.1:8000`. The site will automatically reload when you save changes to Markdown files or `mkdocs.yml`.

7.  **Stop the Server:** Press `Ctrl+C` in the terminal.

## Deployment

This site is automatically deployed via GitHub Actions using the workflow defined in [`.github/workflows/deploy.yml`](./.github/workflows/deploy.yml).

*   Any push to the `main` branch triggers the workflow.
*   The workflow installs dependencies, runs `mkdocs build` to generate the static site into the `site/` directory.
*   The contents of the `site/` directory are then deployed to the `gh-pages` branch (handled automatically by the `actions/deploy-pages` action), which GitHub Pages serves.

The included `deploy.sh` script is a simple helper to add, commit, and push changes from the local machine, effectively triggering the CI/CD pipeline.

## Contributing

These are primarily my personal notes. However, if you spot errors, typos, or have suggestions, feel free to open an [Issue](https://github.com/pujanmotiwala/my-data-science-notes/issues) on this repository.

## License

*(Optional: Choose a License)*

Example:
The content of this project (the notes themselves) is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

The underlying code used to generate the site (e.g., `mkdocs.yml`, workflow files) is licensed under the [MIT License](./LICENSE.md). *(You would need to create a LICENSE.md file with the MIT license text if you choose this)*.

*If you don't want to specify a license, you can remove this section, but be aware that default copyright laws apply.*
