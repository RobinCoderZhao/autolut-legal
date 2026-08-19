(function () {
  const supported = ["en", "zh-Hans"];

  function normalizedLanguage(value) {
    if (!value) return null;
    const lower = value.toLowerCase();
    if (lower.startsWith("zh")) return "zh-Hans";
    if (lower.startsWith("en")) return "en";
    return null;
  }

  function selectedLanguage() {
    const fromQuery = normalizedLanguage(new URLSearchParams(window.location.search).get("lang"));
    if (fromQuery) return fromQuery;
    return normalizedLanguage(navigator.language) || "en";
  }

  function applyLanguage(language, updateURL) {
    const resolved = supported.includes(language) ? language : "en";
    document.documentElement.lang = resolved;

    document.querySelectorAll("[data-language]").forEach((section) => {
      section.hidden = section.dataset.language !== resolved;
    });

    document.querySelectorAll("[data-language-button]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.languageButton === resolved));
    });

    document.querySelectorAll("[data-language-link]").forEach((link) => {
      const target = new URL(link.getAttribute("href"), window.location.href);
      target.searchParams.set("lang", resolved);
      link.setAttribute("href", target.href);
    });

    if (updateURL) {
      const url = new URL(window.location.href);
      url.searchParams.set("lang", resolved);
      history.replaceState(null, "", url);
    }
  }

  window.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-language-button]").forEach((button) => {
      button.addEventListener("click", () => applyLanguage(button.dataset.languageButton, true));
    });
    applyLanguage(selectedLanguage(), false);
  });
})();
