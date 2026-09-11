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

{% assign wiki_pages = site.wiki | sort: "order" %}
{% assign wiki_number = 0 %}

<div class="wiki-home-layout">
  <main class="wiki-directory" aria-labelledby="wiki-directory-heading">
    <header class="wiki-directory__header">
      <div>
        <p class="wiki-directory__label">Browse the archive</p>
        <h2 id="wiki-directory-heading">All wiki pages</h2>
      </div>
      <span>{{ wiki_pages.size }} articles</span>
    </header>

    <section class="wiki-directory-group" aria-labelledby="wiki-world-heading">
      <header class="wiki-directory-group__header">
        <span>World</span>
        <h3 id="wiki-world-heading">The project and its world</h3>
      </header>
      <ol class="wiki-index">
        {% for article in wiki_pages %}
          {% if article.section == "Project overview" or article.section == "World guide" %}
            {% assign wiki_number = wiki_number | plus: 1 %}
            <li>
              <a href="{{ article.url | relative_url }}">
                <span class="wiki-index__number">{% if wiki_number < 10 %}0{% endif %}{{ wiki_number }}</span>
                <span class="wiki-index__entry">
                  <span class="wiki-index__section">{{ article.section | default: "Wiki article" }}</span>
                  <strong>{{ article.title }}</strong>
                  {% if article.description %}<span class="wiki-index__description">{{ article.description }}</span>{% endif %}
                </span>
              </a>
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>

    <section class="wiki-directory-group" aria-labelledby="wiki-places-heading">
      <header class="wiki-directory-group__header">
        <span>Places</span>
        <h3 id="wiki-places-heading">Sectors and infrastructure</h3>
      </header>
      <ol class="wiki-index">
        {% for article in wiki_pages %}
          {% if article.section contains "Sector" or article.section contains "Reactor" %}
            {% assign wiki_number = wiki_number | plus: 1 %}
            <li>
              <a href="{{ article.url | relative_url }}">
                <span class="wiki-index__number">{% if wiki_number < 10 %}0{% endif %}{{ wiki_number }}</span>
                <span class="wiki-index__entry">
                  <span class="wiki-index__section">{{ article.section | default: "Wiki article" }}</span>
                  <strong>{{ article.title }}</strong>
                  {% if article.description %}<span class="wiki-index__description">{{ article.description }}</span>{% endif %}
                </span>
              </a>
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>

    <section class="wiki-directory-group" aria-labelledby="wiki-records-heading">
      <header class="wiki-directory-group__header">
        <span>Records</span>
        <h3 id="wiki-records-heading">People, development, and help</h3>
      </header>
      <ol class="wiki-index">
        {% for article in wiki_pages %}
          {% unless article.section == "Project overview" or article.section == "World guide" %}
            {% unless article.section contains "Sector" %}
              {% assign wiki_number = wiki_number | plus: 1 %}
              <li>
                <a href="{{ article.url | relative_url }}">
                  <span class="wiki-index__number">{% if wiki_number < 10 %}0{% endif %}{{ wiki_number }}</span>
                  <span class="wiki-index__entry">
                    <span class="wiki-index__section">{{ article.section | default: "Wiki article" }}</span>
                    <strong>{{ article.title }}</strong>
                    {% if article.description %}<span class="wiki-index__description">{{ article.description }}</span>{% endif %}
                  </span>
                </a>
              </li>
            {% endunless %}
          {% endunless %}
        {% endfor %}
      </ol>
    </section>
  </main>

  <aside class="wiki-home-rail" aria-label="About Project Redstoneworld">
    <section>
      <p class="wiki-home-rail__label">Welcome</p>
      <h2>A record of the world</h2>
      <p><strong>Project Redstoneworld</strong> began with TheJoCraft on January 18, 2013. Ij continued the world in 2016 through the BTCC approach: bugfix, translate, continue, and complete.</p>
      <p>The wiki records the world’s sectors, infrastructure, history, staff, and development.</p>
    </section>

    <dl class="wiki-home-facts">
      <div><dt>Founded</dt><dd>January 18, 2013</dd></div>
      <div><dt>Reborn</dt><dd>March 15, 2016</dd></div>
      <div><dt>Server</dt><dd>mc.theredstoneworld.net</dd></div>
      <div><dt>Version</dt><dd>Java 1.20.4</dd></div>
    </dl>
  </aside>
</div>

<script src="{{ '/assets/js/wiki-search.js' | relative_url }}" defer></script>
