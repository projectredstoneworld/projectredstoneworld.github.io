(function () {
  "use strict";

  var searchers = document.querySelectorAll("[data-wiki-search]");
  if (!searchers.length) return;

  var indexPromise = fetch("/wiki/search.json")
    .then(function (response) {
      if (!response.ok) throw new Error("Wiki search index unavailable");
      return response.json();
    })
    .catch(function () { return []; });

  function escapeHtml(value) {
    return value.replace(/[&<>"']/g, function (character) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[character];
    });
  }

  searchers.forEach(function (input) {
    var results = input.parentElement.querySelector("[data-wiki-results]");

    function closeResults() {
      results.hidden = true;
      results.innerHTML = "";
    }

    input.addEventListener("input", function () {
      var query = input.value.trim().toLowerCase();
      if (!query) return closeResults();

      indexPromise.then(function (pages) {
        var matches = pages.filter(function (page) {
          return (page.title + " " + page.description).toLowerCase().indexOf(query) !== -1;
        }).slice(0, 6);

        results.innerHTML = matches.length
          ? matches.map(function (page) {
              return '<a href="' + page.url + '"><strong>' + escapeHtml(page.title) + '</strong><span>' + escapeHtml(page.description) + "</span></a>";
            }).join("")
          : '<span class="wiki-search-empty">No matching wiki pages</span>';
        results.hidden = false;
      });
    });

    input.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closeResults();
        input.blur();
      }
      if (event.key === "Enter") {
        var first = results.querySelector("a");
        if (first) window.location.href = first.href;
      }
    });

    document.addEventListener("click", function (event) {
      if (!input.parentElement.contains(event.target)) closeResults();
    });
  });
}());
