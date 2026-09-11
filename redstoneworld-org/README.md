# Redstoneworld.org example

This is a standalone static companion to the Project Redstoneworld Wiki. Open
`index.html` directly to preview it.

## Cloudflare Pages settings

- Repository: `projectredstoneworld/projectredstoneworld.github.io`
- Production branch: `main`
- Framework preset: None
- Build command: leave blank (use `exit 0` only if Cloudflare requires a value)
- Build output directory: `redstoneworld-org`

After the first deployment, attach `redstoneworld.org` under the Pages project's
custom domains. The supplied screenshots are stored as compressed WebP files in
`assets/images` so the page remains self-contained and space-efficient.

The included `_redirects` file preserves the existing `/intro` shortcut without
using a Cloudflare Page Rule.
