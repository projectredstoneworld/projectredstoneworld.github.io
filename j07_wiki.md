---
title: RW Wiki
layout: wiki
permalink: /wiki/
redirect_from: /j07_wiki.html
wiki: true
wiki_home: true
description: The official archive and guide to Project Redstoneworld Reborn.
---

<section class="wiki-hero">
  <div class="wiki-hero__content">
    <p class="wiki-kicker">Project archive · Established 2013</p>
    <h1>Project Redstoneworld Wiki</h1>
    <p>Explore the world’s sectors, infrastructure, history, staff, and development record.</p>
    <label class="wiki-search wiki-search--hero">
      <span class="sr-only">Search the wiki</span>
      <svg aria-hidden="true" viewBox="0 0 24 24"><path d="m21 21-4.3-4.3m2.3-5.2A7.5 7.5 0 1 1 4 11.5a7.5 7.5 0 0 1 15 0Z"/></svg>
      <input type="search" data-wiki-search placeholder="Search the wiki" autocomplete="off">
      <span class="wiki-search-results" data-wiki-results hidden></span>
    </label>
  </div>
</section>

<section class="wiki-intro">
  <p><strong>Project Redstoneworld</strong> is a long-running Minecraft project started by TheJoCraft on January 18, 2013. Ij began continuing the world in 2016 through the BTCC approach—bugfix, translate, continue, and complete—and it remains an active archive of redstone engineering, large-scale construction, and collaborative storytelling.</p>
</section>

<section class="wiki-section" aria-labelledby="browse-wiki">
  <div class="wiki-section__heading">
    <p class="wiki-kicker">Browse the archive</p>
    <h2 id="browse-wiki">Wiki pages</h2>
  </div>
  <div class="wiki-card-grid">
  {% assign wiki_pages = site.wiki | sort: "order" %}
  {% for article in wiki_pages %}
    <a class="wiki-card" href="{{ article.url | relative_url }}">
      <span class="wiki-card__number">0{{ forloop.index }}</span>
      <span class="wiki-card__body">
        <strong>{{ article.title }}</strong>
        <span>{{ article.description }}</span>
      </span>
      <span class="wiki-card__arrow" aria-hidden="true">→</span>
    </a>
  {% endfor %}
  </div>
</section>

<section class="wiki-quickfacts" aria-label="Quick information">
  <div><span>Server</span><strong>mc.theredstoneworld.net</strong></div>
  <div><span>Current version</span><strong>Java 1.20.4</strong></div>
  <div><span>Project founded</span><strong>January 18, 2013</strong></div>
</section>

<script src="{{ '/assets/js/wiki-search.js' | relative_url }}" defer></script>
