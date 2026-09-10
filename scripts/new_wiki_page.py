#!/usr/bin/env python3
"""Create a safe, unpublished wiki page with the standard front matter."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "_wiki"


def prompt(label: str, *, required: bool = False) -> str:
    while True:
        value = input(f"{label}: ").strip()
        if value or not required:
            return value
        print(f"{label} is required.")


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title)
    ascii_title = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_title).strip("-")
    return slug or "wiki-page"


def next_order() -> int:
    orders: list[int] = []
    for page in WIKI_DIR.glob("*.md"):
        match = re.search(r"(?m)^order:\s*(\d+)\s*$", page.read_text(encoding="utf-8"))
        if match:
            orders.append(int(match.group(1)))
    return max(orders, default=0) + 1


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def main() -> int:
    print("Create a new Project Redstoneworld wiki page")
    print("The page starts unpublished, so it will not appear on the live website yet.\n")

    title = prompt("Page title", required=True)
    section = prompt("Section (optional)")
    description = prompt("Short description", required=True)
    slug = slugify(title)
    destination = WIKI_DIR / f"{slug}.md"

    if destination.exists():
        print(f"\nNot created: {destination.relative_to(ROOT)} already exists.", file=sys.stderr)
        return 1

    frontmatter = [
        "---",
        f"title: {yaml_string(title)}",
        f"order: {next_order()}",
    ]
    if section:
        frontmatter.append(f"section: {yaml_string(section)}")
    frontmatter.extend(
        [
            f"description: {yaml_string(description)}",
            "published: false",
            "---",
            "",
            "Write the introduction here.",
            "",
            "## First section",
            "",
            "Start writing here.",
            "",
        ]
    )

    WIKI_DIR.mkdir(exist_ok=True)
    destination.write_text("\n".join(frontmatter), encoding="utf-8")

    relative = destination.relative_to(ROOT)
    print(f"\nCreated {relative}")
    print("Preview it locally, then remove 'published: false' when it is ready for the live site.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
