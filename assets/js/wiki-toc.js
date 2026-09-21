(() => {
  const article = document.querySelector(".wiki-article__body");
  const tocs = document.querySelectorAll("[data-wiki-toc]");

  if (!article || !tocs.length) return;

  const headings = Array.from(
    article.querySelectorAll("h2, h3, h4, h5, h6")
  ).filter((heading) => heading.textContent.trim());

  if (!headings.length) {
    tocs.forEach((toc) => {
      toc.hidden = true;
    });
    return;
  }

  const slugify = (text) => text
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[’']/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "") || "section";

  const usedIds = new Set(
    Array.from(document.querySelectorAll("[id]"))
      .map((element) => element.id)
  );

  const entries = headings.map((heading) => {
    if (!heading.id) {
      const base = slugify(heading.textContent.trim());
      let id = base;
      let suffix = 2;

      while (usedIds.has(id)) {
        id = `${base}-${suffix}`;
        suffix += 1;
      }

      heading.id = id;
      usedIds.add(id);
    }

    return {
      id: heading.id,
      title: heading.textContent.trim(),
      level: heading.tagName.substring(1)
    };
  });

  tocs.forEach((toc) => {
    const list = toc.querySelector("[data-wiki-toc-list]");
    if (!list) return;

    list.replaceChildren();

    entries.forEach((entry) => {
      const item = document.createElement("li");
      const link = document.createElement("a");

      item.className = `wiki-toc__level-${entry.level}`;
      link.href = `#${entry.id}`;
      link.textContent = entry.title;

      item.appendChild(link);
      list.appendChild(item);
    });

    toc.hidden = false;
  });
})();