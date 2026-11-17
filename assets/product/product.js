(() => {
  const frame = document.querySelector("[data-compare]");
  if (frame) {
    const divider = frame.querySelector("input");
    divider.hidden = false;
    document.querySelector("[data-compare-hint]").hidden = false;
    const left = frame.querySelector(".frame-left");
    const right = frame.querySelector(".frame-right");
    const updateComparison = () => {
      const percentage = divider.valueAsNumber;
      frame.style.setProperty("--split", percentage + "%");
      left.hidden = percentage < 25;
      right.hidden = percentage > 75;
      divider.setAttribute("aria-valuetext", left.textContent + " " + percentage + "%");
    };
    divider.addEventListener("input", updateComparison);
    updateComparison();
  }
  const source = new URLSearchParams(location.search).get("src");
  const campaigns = new Map([
    ["bili", "hueo_bili_luna"],
    ["youtube", "hueo_youtube_luna"],
  ]);
  if (campaigns.has(source)) {
    for (const link of document.querySelectorAll("[data-store]")) {
      const url = new URL(link.href);
      url.searchParams.set("ct", campaigns.get(source));
      link.href = url.href;
    }
    for (const link of document.querySelectorAll("[data-product-link]")) {
      const url = new URL(link.href);
      url.searchParams.set("src", source);
      link.href = url.href;
    }
  }
  const mobileNav = document.querySelector(".mobile-nav");
  mobileNav.addEventListener("click", event => {
    if (event.target.closest("a")) mobileNav.open = false;
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && mobileNav.open) {
      mobileNav.open = false;
      mobileNav.querySelector("summary").focus();
    }
  });
})();
