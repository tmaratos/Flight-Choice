/**
 * Flight Choice — Google Business Profile trust (single source of truth).
 * Set ratingText / reviewCountText only when manually verified.
 */
var GOOGLE_BUSINESS_PROFILE = {
  label: "Reviewed by clients on Google",
  url:
    "https://www.google.com/maps/place/Flight+Choice/@35.8107118,-83.9862172,17z/data=!3m1!4b1!4m6!3m5!1s0x1526993ee4e50bed:0x4446191e23b66c11!8m2!3d35.8107118!4d-83.9862172!16s%2Fg%2F11b6hp9ps1?entry=ttu&g_ep=EgoyMDI2MDUxMy4wIKXMDSoASAFQAw%3D%3D",
  ctaLabel: "View Google reviews",
  footerLabel: "Google Business Profile",
  ratingText: "",
  reviewCountText: "",
};

(function () {
  "use strict";

  var cfg = GOOGLE_BUSINESS_PROFILE;

  function hasRating() {
    return Boolean(cfg.ratingText && cfg.ratingText.trim());
  }

  function hasReviewCount() {
    return Boolean(cfg.reviewCountText && cfg.reviewCountText.trim());
  }

  function externalLink(attrs) {
    var a = document.createElement("a");
    a.href = cfg.url;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.className = attrs.className || "google-trust-link";
    if (attrs.ariaLabel) a.setAttribute("aria-label", attrs.ariaLabel);
    a.textContent = attrs.text || cfg.ctaLabel;
    return a;
  }

  function starsEl() {
    if (!hasRating()) return null;
    var wrap = document.createElement("span");
    wrap.className = "google-trust-stars";
    wrap.setAttribute("aria-hidden", "true");
    wrap.innerHTML =
      '<span class="google-trust-stars__glyph">★★★★★</span>';
    return wrap;
  }

  function metaEl() {
    if (!hasRating() && !hasReviewCount()) return null;
    var meta = document.createElement("p");
    meta.className = "google-trust-meta";
    var parts = [];
    if (hasRating()) parts.push(cfg.ratingText);
    if (hasReviewCount()) parts.push(cfg.reviewCountText);
    meta.textContent = parts.join(" · ");
    return meta;
  }

  function renderInline(el) {
    el.className = (el.className + " google-trust-inline").trim();
    var label = document.createElement("span");
    label.className = "google-trust-inline__label";
    label.textContent = cfg.label;
    el.appendChild(label);
    var link = externalLink({
      className: "google-trust-link google-trust-link--inline",
      ariaLabel: cfg.ctaLabel + " (opens Google in a new tab)",
      text: cfg.ctaLabel,
    });
    el.appendChild(document.createTextNode(" "));
    el.appendChild(link);
  }

  function renderSection(el) {
    el.className = (el.className + " google-trust-panel").trim();
    el.innerHTML = "";

    var accent = document.createElement("div");
    accent.className = "google-trust-panel__accent";
    accent.setAttribute("aria-hidden", "true");
    el.appendChild(accent);

    var inner = document.createElement("div");
    inner.className = "google-trust-panel__inner";

    var eyebrow = document.createElement("p");
    eyebrow.className = "eyebrow";
    eyebrow.textContent = "Client Confidence";
    inner.appendChild(eyebrow);

    var h2 = document.createElement("h2");
    h2.className = "h2 google-trust-panel__title";
    h2.id = el.getAttribute("data-heading-id") || "client-confidence";
    h2.textContent = "Trusted private aviation support in Knoxville.";
    inner.appendChild(h2);

    var body = document.createElement("p");
    body.className = "google-trust-panel__body";
    body.textContent =
      "Flight Choice's Google Business Profile provides an additional place for clients to review their experience, location, and service history.";
    inner.appendChild(body);

    var stars = starsEl();
    if (stars) inner.appendChild(stars);
    var meta = metaEl();
    if (meta) inner.appendChild(meta);

    var actions = document.createElement("div");
    actions.className = "google-trust-panel__actions";
    actions.appendChild(
      externalLink({
        className: "btn btn-ghost google-trust-link--section",
        ariaLabel: cfg.ctaLabel + " (opens Google in a new tab)",
        text: cfg.ctaLabel,
      })
    );
    inner.appendChild(actions);

    el.appendChild(inner);
  }

  function renderFooter(el) {
    var link = externalLink({
      className: "google-trust-link google-trust-link--footer",
      ariaLabel: cfg.footerLabel + " (opens Google in a new tab)",
      text: cfg.footerLabel,
    });
    el.appendChild(link);
  }

  function init() {
    document.querySelectorAll("[data-google-trust]").forEach(function (el) {
      var mode = el.getAttribute("data-google-trust");
      if (mode === "inline") renderInline(el);
      else if (mode === "section") renderSection(el);
      else if (mode === "footer") renderFooter(el);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
