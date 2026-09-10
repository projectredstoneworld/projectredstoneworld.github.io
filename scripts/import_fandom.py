#!/usr/bin/env python3
"""Convert the latest article revisions in a MediaWiki XML export to Jekyll pages."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote


ARTICLE_METADATA = {
    "Project Redstoneworld Reborn Wiki": {
        "title": "Project Redstoneworld Reborn",
        "order": 1,
        "section": "Project overview",
        "description": "The origins, continuation, server information, and purpose of Project Redstoneworld Reborn.",
        "image": "/img/default_2024-06-14_13-05-31-17.denoised.png",
        "image_alt": "A wide view across Project Redstoneworld",
    },
    "Redstone Tower Complex (RTC) Sector": {
        "order": 2,
        "section": "Sector 707",
        "description": "The towers, RCorp bridge, and reactor complex that form the Redstone Tower Complex.",
        "image": "/wiki/assets/images/rw-all-sector-render-rtc-bias.webp",
        "image_alt": "The main Redstone Tower Complex towers, bridge, and surrounding sectors",
    },
    "Founding Island Bunker": {
        "order": 3,
        "section": "Sector 101-B / 505",
        "description": "History, rooms, security, and infrastructure inside the Founding Island Bunker.",
        "image": "/wiki/assets/images/fi-bunker-shaders.webp",
        "image_alt": "A view of the redstone above the Founding Island Bunker's Blue Zone",
    },
    "Sectors": {
        "order": 4,
        "section": "World guide",
        "description": "How Project Redstoneworld organizes its primary sectors, mini-sectors, and regions.",
        "image": "/img/default_2024-06-14_13-05-31-17.denoised.png",
        "image_alt": "A wide view across Project Redstoneworld",
    },
    "Staff": {
        "order": 5,
        "section": "Community",
        "description": "Staff ranks, responsibilities, the Coalition, and the current Redstoneworld team.",
    },
    "Ij's devlogs": {
        "order": 6,
        "section": "Development history",
        "description": "A chronological index of official devlogs, specials, and anniversary videos.",
    },
    "Frequently Asked Questions": {
        "order": 7,
        "section": "Visitor guide",
        "description": "Answers about joining the server, supported editions, downloads, and staff applications.",
    },
}

HOME_TITLES = {"Project Redstoneworld Reborn Wiki", "Main Page"}

IMAGE_PATHS = {
    "rw all sector render (rtc bias).webp": "/wiki/assets/images/rw-all-sector-render-rtc-bias.webp",
    "2016 shelter.png": "/wiki/assets/images/2016-shelter.webp",
    "early fi bunker.png": "/wiki/assets/images/early-fi-bunker.webp",
    "fi bunker 1 interior.png": "/wiki/assets/images/fi-bunker-1-interior.webp",
    "fi bunker catalyst.png": "/wiki/assets/images/fi-bunker-catalyst.webp",
    "fi bunker shaders.png": "/wiki/assets/images/fi-bunker-shaders.webp",
}


def slugify(value: str) -> str:
    value = unquote(value).replace("’", "'")
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = value.lower().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def heading_id(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"'{2,5}", "", value)
    return slugify(html.unescape(value))


def split_template(value: str) -> list[str]:
    parts, buffer, depth = [], [], 0
    for character in value:
        if character == "{" or character == "[":
            depth += 1
        elif character == "}" or character == "]":
            depth = max(0, depth - 1)
        if character == "|" and depth == 0:
            parts.append("".join(buffer))
            buffer = []
        else:
            buffer.append(character)
    parts.append("".join(buffer))
    return parts


def extract_infobox(text: str) -> tuple[str, dict[str, str]]:
    match = re.search(r"\{\{\s*RW[_ ]Sector\s*\|(.*?)\}\}", text, flags=re.I | re.S)
    if not match:
        return text, {}
    fields = {}
    for part in split_template(match.group(1)):
        if "=" in part:
            key, value = part.split("=", 1)
            fields[key.strip().lower()] = value.strip()
    labels = {
        "date_started": "Started",
        "main_creators": "Main creators",
        "type": "Type",
    }
    infobox = {labels[key]: fields[key] for key in labels if fields.get(key)}
    return text[: match.start()] + text[match.end() :], infobox


def clean_inline_markup(value: str) -> str:
    value = re.sub(r"<nowiki>(.*?)</nowiki>", r"\1", value, flags=re.I | re.S)
    value = re.sub(r"<small>(.*?)</small>", r"<small>\1</small>", value, flags=re.I | re.S)
    value = re.sub(r"<big>(.*?)</big>", r"\1", value, flags=re.I | re.S)
    value = re.sub(r"<u>(.*?)</u>", r"\1", value, flags=re.I | re.S)
    value = re.sub(r"'''''(.*?)'''''", r"<strong><em>\1</em></strong>", value, flags=re.S)
    value = re.sub(r"'''(.*?)'''", r"<strong>\1</strong>", value, flags=re.S)
    value = re.sub(r"''(.*?)''", r"<em>\1</em>", value, flags=re.S)
    return value


class Converter:
    def __init__(self, article_titles: set[str]):
        self.article_titles = article_titles
        self.title_lookup = {title.lower(): title for title in article_titles}
        self.slug_lookup = {title: slugify(title) for title in article_titles}

    def internal_link(self, match: re.Match[str]) -> str:
        raw = match.group(1).strip()
        if raw.lower().startswith(("file:", "image:", "category:")):
            return ""
        pieces = raw.split("|", 1)
        target = unquote(pieces[0].strip()).replace("_", " ")
        label = pieces[1].strip() if len(pieces) > 1 else target
        label = clean_inline_markup(label)
        if target.startswith("#"):
            return f'<a href="#{heading_id(target[1:])}">{label}</a>'
        page_target, separator, fragment = target.partition("#")
        normalized = self.title_lookup.get(page_target.lower())
        if page_target in HOME_TITLES or page_target.lower() in {x.lower() for x in HOME_TITLES}:
            url = "/wiki/"
        elif normalized:
            url = f"/wiki/{self.slug_lookup[normalized]}/"
        else:
            return f'<span class="wiki-redlink" title="This page is not available yet">{label}</span>'
        if separator:
            url += f"#{heading_id(fragment)}"
        return f'<a href="{url}">{label}</a>'

    def inline(self, value: str) -> str:
        value = re.sub(r"\[\[(.+?)\]\]", self.internal_link, value)
        external_links = []
        def save_external_link(match: re.Match[str]) -> str:
            external_links.append(
                f'<a href="{match.group(1)}">{clean_inline_markup(match.group(2) or match.group(1))}</a>'
            )
            return f"@@EXTERNALLINK{len(external_links) - 1}@@"
        value = re.sub(
            r"\[(https?://[^\s\]]+)(?:\s+([^\]]+))?\]",
            save_external_link,
            value,
        )
        def bare_link(match: re.Match[str]) -> str:
            url = match.group(0).rstrip(".,")
            suffix = match.group(0)[len(url):]
            return f'<a href="{url}">{url}</a>{suffix}'
        value = re.sub(r"https?://[^\s<]+", bare_link, value)
        for index, link in enumerate(external_links):
            value = value.replace(f"@@EXTERNALLINK{index}@@", link)
        value = clean_inline_markup(value)
        return value

    def table(self, block: str) -> str:
        lines = block.splitlines()[1:-1]
        caption, headers, rows, current, current_id = "", [], [], [], ""
        for raw in lines:
            line = raw.strip()
            if not line:
                continue
            if line == "|}":
                continue
            if line.startswith("|+"):
                caption = line[2:].strip()
            elif line.startswith("!" ):
                headers.extend(x.strip() for x in line[1:].split("!!"))
            elif line.startswith("|-"):
                if current:
                    rows.append((current_id, current))
                    current = []
                id_match = re.search(r'id=["\']?([^"\'\s]+)', line, flags=re.I)
                current_id = heading_id(id_match.group(1)) if id_match else ""
            elif line.startswith("|"):
                current.extend(x.strip() for x in line[1:].split("||"))
        if current:
            rows.append((current_id, current))
        output = ['<div class="wiki-table-wrap">', "<table>"]
        if caption:
            output.append(f"<caption>{self.inline(caption)}</caption>")
        if headers:
            output.append("<thead><tr>" + "".join(f"<th>{self.inline(cell)}</th>" for cell in headers) + "</tr></thead>")
        output.append("<tbody>")
        for row_id, row in rows:
            cells = []
            for cell in row:
                cell = cell.strip('"')
                if re.fullmatch(r"https?://[^\s<>]+", cell):
                    rendered = f'<a href="{cell}">Watch</a>'
                else:
                    rendered = self.inline(cell)
                cells.append(f"<td>{rendered}</td>")
            id_attribute = f' id="{row_id}"' if row_id else ""
            output.append(f"<tr{id_attribute}>" + "".join(cells) + "</tr>")
        output.extend(["</tbody>", "</table>", "</div>"])
        return "\n".join(output)

    def convert(self, text: str) -> tuple[str, list[dict[str, object]], dict[str, str]]:
        text, infobox = extract_infobox(text)
        text = text.replace("\r\n", "\n")
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        text = re.sub(r"<mainpage-[^>]+>", "", text, flags=re.I)
        text = re.sub(r"</?div(?:\s+[^>]*)?>", "", text, flags=re.I)
        text = re.sub(r"\{\{(?:DISPLAYTITLE|DEFAULTSORT):.*?\}\}", "", text, flags=re.I)
        text = re.sub(r"\[\[Category:.*?\]\]", "", text, flags=re.I)
        text = re.sub(r"__(?:INDEX|NEWSECTIONLINK|NOTOC)__", "", text, flags=re.I)
        text = re.sub(r"\{\{SITENAME\}\}", "Project Redstoneworld Reborn Wiki", text, flags=re.I)
        text = re.sub(r"\{\{[^{}]*\}\}", "", text, flags=re.S)

        images = []
        def save_image(match: re.Match[str]) -> str:
            filename = match.group(1).strip().replace("_", " ")
            source = IMAGE_PATHS.get(filename.lower())
            if not source:
                return ""
            options = [part.strip() for part in (match.group(2) or "").split("|") if part.strip()]
            formatting = {"thumb", "thumbnail", "left", "right", "center", "frameless", "frame"}
            caption = next(
                (
                    option for option in reversed(options)
                    if option.lower() not in formatting and not re.fullmatch(r"\d+px", option.lower())
                ),
                "",
            )
            alignment = "left" if any(option.lower() == "left" for option in options) else "right"
            rendered_caption = self.inline(caption) if caption else ""
            alt = html.escape(re.sub(r"<[^>]+>", "", rendered_caption) or Path(filename).stem, quote=True)
            figure = [
                f'<figure class="wiki-inline-image wiki-inline-image--{alignment}">',
                f'  <img src="{source}" alt="{alt}" loading="lazy">',
            ]
            if rendered_caption:
                figure.append(f"  <figcaption>{rendered_caption}</figcaption>")
            figure.append("</figure>")
            images.append("\n".join(figure))
            return f"\n@@WIKIIMAGE{len(images) - 1}@@\n"
        text = re.sub(
            r"\[\[(?:File|Image):([^\]|]+)(?:\|([^\]]*))?\]\]",
            save_image,
            text,
            flags=re.I,
        )
        text = re.sub(r"\[\[(?:File|Image):[^\]]+\]\]\s*", "", text, flags=re.I)

        tables = []
        def save_table(match: re.Match[str]) -> str:
            tables.append(self.table(match.group(0)))
            return f"\n@@WIKITABLE{len(tables) - 1}@@\n"
        text = re.sub(r"^\{\|.*?^\|\}\s*", save_table, text, flags=re.M | re.S)

        toc = []
        converted = []
        for line in text.splitlines():
            heading = re.match(r"^(={2,6})\s*(.*?)\s*\1\s*$", line)
            if heading:
                level = len(heading.group(1))
                title = clean_inline_markup(heading.group(2)).strip()
                plain_title = re.sub(r"<[^>]+>", "", title)
                identifier = heading_id(plain_title)
                toc.append({"level": level, "title": html.unescape(plain_title), "id": identifier})
                converted.append(f'{"#" * level} {title} {{#{identifier}}}')
            else:
                line = re.sub(r"^([*#]+)(?=\S)", r"\1 ", line)
                converted.append(self.inline(line))
        text = "\n".join(converted)
        for index, table_html in enumerate(tables):
            text = text.replace(f"@@WIKITABLE{index}@@", table_html)
        for index, image_html in enumerate(images):
            text = text.replace(f"@@WIKIIMAGE{index}@@", image_html)
        text = re.sub(r"(?m)^(?![*#] )(.*\S)\n(?=[*#] )", r"\1\n\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
        return text, toc, infobox


def load_pages(xml_path: Path) -> list[dict[str, str]]:
    root = ET.parse(xml_path).getroot()
    namespace = {"m": root.tag.split("}")[0].lstrip("{")}
    pages = []
    for page in root.findall("m:page", namespace):
        if page.findtext("m:ns", default="", namespaces=namespace) != "0":
            continue
        title = page.findtext("m:title", default="", namespaces=namespace)
        revisions = page.findall("m:revision", namespace)
        if not revisions:
            continue
        revision = revisions[-1]
        contributor = revision.find("m:contributor", namespace)
        username = ""
        if contributor is not None:
            username = contributor.findtext("m:username", default="", namespaces=namespace)
            username = username or contributor.findtext("m:ip", default="", namespaces=namespace)
        pages.append({
            "title": title,
            "text": revision.findtext("m:text", default="", namespaces=namespace) or "",
            "timestamp": revision.findtext("m:timestamp", default="", namespaces=namespace),
            "contributor": username,
        })
    return pages


def yaml_value(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("xml", type=Path)
    parser.add_argument("--output", type=Path, default=Path("_wiki"))
    args = parser.parse_args()

    pages = load_pages(args.xml)
    article_pages = [page for page in pages if page["title"] in ARTICLE_METADATA]
    article_titles = {page["title"] for page in article_pages}
    converter = Converter(article_titles)

    if args.output.exists():
        shutil.rmtree(args.output)
    args.output.mkdir(parents=True)

    for page in article_pages:
        metadata = ARTICLE_METADATA[page["title"]]
        content, toc, infobox = converter.convert(page["text"])
        frontmatter = {
            "title": page["title"],
            **metadata,
            "last_modified": page["timestamp"],
            "contributor": page["contributor"],
            "toc": toc,
        }
        if infobox:
            frontmatter["infobox"] = infobox
        lines = ["---"]
        for key, value in frontmatter.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
            else:
                lines.append(f"{key}: {yaml_value(value)}")
        lines.extend(["---", "", content])
        (args.output / f"{slugify(page['title'])}.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Imported {len(article_pages)} articles into {args.output}")


if __name__ == "__main__":
    main()
