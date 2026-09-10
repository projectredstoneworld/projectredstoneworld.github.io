# theredstoneworld.net

As of 2026 this website is now being developed by the Projekt Redstoneworld Department of Technical Aspects (Director IJD, Deputy Director LLucas). The website was originally started by Lenni-Builder with the 10 year anniversary of the world. Full developments started with the Chapter 7 domain change in summer 2024. In September of 2026 the Fandom wiki was migrated here.

## Previewing changes

It can be helpful to preview the website fully before actually pushing. This can be accomplished in two ways.

### Over the web on GitHub

This can be connected to your personal VSCode so you do not have to edit on the browser, however GitHub usage limits apply (around 60 hours per month of codespaces for free accounts)
Open the repository on GitHub.
Select Code → Codespaces → Create codespace on main.
Wait for the automatic first-time setup.
Select Terminal → Run Task → Preview website.
Open the automatically forwarded preview.

### On personal VSCode using Docker

This one has unlimited usage but is a bit harder to setup, mainly if you do not have docker desktop already installed

Install Docker Desktop using the WSL 2 option.
If Windows says WSL is missing, open PowerShell as administrator and run wsl --install, then restart.
Start Docker Desktop and wait until its engine is running.
Open VS Code.
Install the extension named Dev Containers by Microsoft.

Open the cloned website repository in VS Code.
Press Ctrl+Shift+P.
Run Dev Containers: Reopen in Container.
Wait for the first setup. It will download the container, install Ruby 3.1, and run bundle install automatically.
Select Terminal → Run Task → Preview website.
VS Code should offer to open port 4000 automatically. You can also use Ctrl + Shift + B as a shortcut for this going forward.

## Wiki editing

Please refer to <https://theredstoneworld.net/wiki/editing/>

## Deployment

Please do not push twice back to back as it can break the deployment. Please wait at least around 30 seconds. The status of the GitHub repository is posted on the corresponding channel on the Discord server. If you would like to contribute use pull requests or contact Ij on discord.

## Wiki archive

The pages in `_wiki` were imported from the former Fandom wiki and are published under `/wiki/`. They can be edited directly as normal Markdown files.

To rebuild all imported articles from another MediaWiki XML export:

```sh
python3 scripts/import_fandom.py path/to/export.xml
```

The importer replaces the generated `_wiki` directory, so commit any manual article changes before running it. MediaWiki XML exports do not contain the uploaded image files. Recovered wiki images are stored in `wiki/assets/images`, and their original Fandom filenames are mapped in the importer.
