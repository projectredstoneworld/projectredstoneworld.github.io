(() => {
  const article = document.querySelector(".wiki-article__body");
  const toc = document.querySelector("[data-wiki-toc]");
  const list = toc?.querySelector("[data-wiki-toc-list]");

  if (!article || !toc || !list) return;

  const headings = Array.from(article.querySelectorAll("h2, h3, h4, h5, h6"))
    .filter((heading) => heading.textContent.trim());

  if (!headings.length) {
    toc.hidden = true;
    return;
  }

  const slugify = (text) => text
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[’']/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "") || "section";

  const reserveUniqueId = (heading) => {
    if (heading.id) return heading.id;

    const base = slugify(heading.textContent.trim());
    let id = base;
    let suffix = 2;

    while (document.getElementById(id)) {
      id = `${base}-${suffix}`;
      suffix += 1;
    }

    heading.id = id;
    return id;
  };

  const fragment = document.createDocumentFragment();

  headings.forEach((heading) => {
    const item = document.createElement("li");
    const link = document.createElement("a");
    const level = heading.tagName.slice(1);

    item.className = `wiki-toc__level-${level}`;
    link.href = `#${reserveUniqueId(heading)}`;
    link.textContent = heading.textContent.trim();
    item.append(link);
    fragment.append(item);
  });

  list.replaceChildren(fragment);
  toc.hidden = false;
})();
