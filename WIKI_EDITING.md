# Editing the Project Redstoneworld Wiki

Wiki articles are Markdown files in `_wiki`. The shared layout automatically supplies the page title, wiki navigation, search, and table of contents.
Wiki can be edited at https://github.com/projectredstoneworld/projectredstoneworld.github.io if you are not an added user please use pull requests for your changes.

## Preview locally

Open the repository in its Dev Container and press `Ctrl+Shift+B`. Draft pages are included in this local preview but remain absent from the deployed website.

## Edit an existing page

Write normal Markdown. Headings automatically appear in the table of contents:

```markdown
## What is the server IP?

The server IP is `mc.theredstoneworld.net`.
```

Explicit IDs imported from Fandom remain supported and are used by the automatic table of contents:

```markdown
##### Admin Room {#admin-room}
```

Set `toc: false` in the page's front matter only when a page should have no table of contents.

## Create a page

In VS Code, select **Terminal → Run Task → Create new wiki page** and answer the prompts. The task creates the correct filename and front matter with:

```yaml
published: false
```

That page is available in the local preview but excluded from the public site. Remove `published: false` when the page is ready. The wiki index, search data, sitemap, and automatic links update during the next build.

## Link to another wiki page

Use the wiki link helper:

```liquid
{% include wiki-link.html title="Tower 1" %}
```

If the corresponding page does not exist, it appears as “not available yet.” Once `_wiki/tower-1.md` is published, it automatically becomes a link. To display different text, add `text`:

```liquid
{% include wiki-link.html title="Redstone Tower Complex (RTC) Sector" text="RTC" %}
```

## Add an inline image

Upload the image to `wiki/assets/images`, then add one line:

```liquid
{% include wiki-image.html file="example.png" caption="Description of the image." %}
```

Images appear on the right by default. Use `side="left"` or `side="full"` when needed:

```liquid
{% include wiki-image.html file="example.png" caption="Description." side="left" %}
{% include wiki-image.html file="wide-example.png" caption="Wide image." side="full" %}
```

The caption is also used as alternative text by default. When the visual description should differ from the visible caption, provide `alt="..."` separately.

## Front matter reference

A typical page begins with:

```yaml
---
title: "Page title"
order: 8
section: "World guide"
description: "A short summary used on the wiki index and by search engines."
published: false
---
```

Optional cover images and information boxes continue to work:

```yaml
image: "/wiki/assets/images/cover.webp"
image_alt: "Description of the cover image"
infobox:
  Started: "January 1, 2026"
  Main creators: "Ij, Huddo"
  Type: "Primary Sector"
```
