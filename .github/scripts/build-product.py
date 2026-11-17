"""Render only the four HUEO marketing pages and their sitemap. Standard library only."""
import json
from html import escape
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://robincoderzhao.github.io/autolut-legal/"
APP = "https://apps.apple.com/app/apple-store/id6804096727"
GUIDE = "guide/luna-i-log/"
FORMATS = (
    ("Apple", "Apple Log / Apple Log 2"), ("Insta360", "I-Log"),
    ("Nikon", "N-Log"), ("Sony", "S-Log3"),
    ("DJI", "D-Log / D-Log2"), ("Canon", "Canon Log 2 / 3"),
    ("Fujifilm", "F-Log / F-Log2"),
)


def render(language, guide):
    c = json.loads((ROOT / ".github" / "product" / f"{language}.json").read_text())
    zh = language == "zh"
    other = "en" if zh else "zh"
    suffix = GUIDE if guide else ""
    path = f"{language}/{suffix}"
    prefix = "../" * len(Path(path).parts)
    media = prefix + "assets/product/media/"
    home = "../../" if guide else "./"
    other_page = prefix + f"{other}/{suffix}"
    query = f"?lang={c['lang']}"
    url = APP + "?" + urlencode({"pt": "129079916", "ct": "hueo_web_" + language, "mt": "8"})
    title = c["guideTitle" if guide else "title"]
    description = c["guideDescription" if guide else "description"]

    def store_button(compact=False):
        label = c["shortDownload" if compact else "download"]
        style = "store-small" if compact else "store-button"
        return f'<a class="{style}" href="{escape(url)}" data-store>{escape(label)} <span aria-hidden="true">↗</span></a>'

    def links():
        return "".join(f'<a data-product-link href="{home}#{key}">{escape(c[label])}</a>'
                       for key, label in (("workflow", "workflow"), ("formats", "formats"), ("pro", "plan")))

    other_lang = "en" if zh else "zh-Hans"
    brand = f'<a class="brand" data-product-link href="{home}" aria-label="{escape(c["guideBack"])}"><img src="{media}hueo-icon.png" width="34" height="34" alt=""><span>HUEO</span></a>'
    locale = f'<a class="locale" href="{other_page}" lang="{other_lang}" hreflang="{other_lang}" aria-label="{escape(c["languageLabel"])}" data-product-link>{c["language"]}</a>'
    header = f'''<a class="skip" href="#content">{c["skip"]}</a>
<header class="mast"><div class="wrap mast-inner">{brand}
  <nav class="desktop-nav" aria-label="{c["nav"]}">{links()}</nav>
  <div class="mast-controls">{locale}{store_button(True)}
    <details class="mobile-nav"><summary>{c["menu"]}</summary><nav aria-label="{c["nav"]}">{links()}</nav></details>
  </div>
</div></header>'''
    footer = f'''<footer class="footer"><div class="wrap footer-inner">{brand}
  <nav aria-label="{c["footer"]}"><a href="{prefix}{query}">{c["support"]}</a><a href="{prefix}privacy/{query}">{c["privacy"]}</a><a href="{prefix}privacy/terms.html{query}">{c["terms"]}</a></nav>
</div></footer>'''
    demo_video = f'''<div class="demo-player"><video width="1280" height="720" controls playsinline preload="none" poster="{media}walkthrough-{language}-poster.webp" aria-label="{escape(c["demoTitle"])}">
      <source src="{media}walkthrough-{language}.mp4" type="video/mp4">
      <track kind="captions" src="{media}walkthrough-{language}.vtt" srclang="{c["lang"]}" label="{'简体中文' if zh else 'English'}">
      <a href="{media}walkthrough-{language}.mp4">{escape(c["watch"])}</a>
    </video><p>{escape(c["demoCaption"])}</p>
    <details><summary>{escape(c["demoTranscript"])}</summary><p>{escape(c["demoSummary"])}</p></details></div>'''
    if guide:
        steps = []
        for i, (heading, lead, detail) in enumerate(c["guideSteps"]):
            picture = ""
            if i in (1, 3):
                phone = i == 1
                image_name = "phone-restore" if phone else "export"
                alt = c["phoneAlt" if phone else "exportAlt"]
                caption = c["phoneCaption" if phone else "exportCaption"]
                size = 'width="600" height="1265"' if phone else 'width="1280" height="890"'
                picture = f'<figure class="guide-photo {"portrait" if phone else ""}"><a href="{media}{image_name}-{language}.webp" aria-label="{escape(c["viewFull"])} · {escape(caption)}"><img src="{media}{image_name}-{language}.webp" {size} loading="lazy" alt="{escape(alt)}"></a><figcaption>{caption}</figcaption></figure>'
            steps.append(f'<li><h2>{escape(heading)}</h2><p>{escape(lead)}</p><p>{escape(detail)}</p>{picture}</li>')
        content = f'''<main id="content" class="guide">
  <header class="guide-head wrap"><a data-product-link class="back" href="{home}">← {escape(c["guideBack"])}</a>
    <h1>{escape(c["guideHeading"])}</h1><p class="lede">{escape(c["guideIntro"])}</p></header>
  <section class="demo wrap" id="demo" aria-label="{escape(c["demoTitle"])}">
    {demo_video}
  </section>
  <div class="paper"><div class="guide-layout wrap"><ol class="guide-steps">{"".join(steps)}</ol></div></div>
  <section class="wrap guide-cta"><div><h2>{escape(c["guideEnding"])}</h2><p>{escape(c["guideFree"])}</p></div>{store_button()}</section>
</main>'''
    else:
        steps = "".join(f'<li><div><h3>{escape(h)}</h3><p>{escape(p)}</p></div></li>' for h, p in c["steps"])
        formats = "".join(f'<div><dt>{maker}</dt><dd>{profile}</dd></div>' for maker, profile in FORMATS)
        first, second = ("还原页预览", "导出页预览") if zh else ("Restoration preview", "Export preview")
        compare_alt = "清真寺和海岸的同一帧，分界线左边为还原页预览，右边为导出页预览" if zh else "The same waterfront frame, with the restoration preview on the left and export preview on the right"
        compare_caption = "iPad · 两个面板中的同一帧实拍" if zh else "iPad · The same frame from two panels"
        compare_control = "移动预览分界线" if zh else "Move the preview divider"
        content = f'''<main id="content">
  <section class="hero wrap"><div class="hero-copy"><h1>{escape(c["heroTitle"][0])}<br><em>{escape(c["heroTitle"][1])}</em></h1>
    <p class="lede">{escape(c["heroText"])}</p><div class="hero-actions">{store_button()}<a class="watch" href="#demo">{escape(c["watch"])} <span aria-hidden="true">→</span></a></div><p class="platforms">{escape(c["platforms"])}</p></div>
    <figure class="hero-figure"><div class="mat"><div class="compare" data-compare>
      <img src="{media}compare-export.webp" width="1280" height="720" alt="{compare_alt}" fetchpriority="high">
      <img class="comparison-left" src="{media}compare-restore.webp" width="1280" height="720" alt="">
      <div class="divider" aria-hidden="true"><span>‹ ›</span></div>
      <span class="frame-label frame-left" aria-hidden="true">{first}</span><span class="frame-label frame-right" aria-hidden="true">{second}</span>
      <input hidden type="range" min="0" max="100" value="50" aria-label="{compare_control}">
    </div></div><figcaption><span>{compare_caption}</span><span class="format" data-compare-hint hidden>{'拖动分界线对照' if zh else 'Drag the divider to compare'}</span></figcaption></figure>
  </section>
  <section class="paper" id="workflow"><div class="wrap workflow">
    <div class="workflow-copy"><h2>{escape(c["workflowHeading"])}</h2><ol class="steps">{steps}</ol>
      <a data-product-link class="ink-link" href="{GUIDE}">{escape(c["readGuide"])} <span aria-hidden="true">→</span></a></div>
    <figure class="phone-figure"><img src="{media}phone-restore-{language}.webp" width="600" height="1265" loading="lazy" alt="{escape(c["phoneAlt"])}"><figcaption>{escape(c["phoneCaption"])}</figcaption></figure>
  </div></section>
  <section class="proof wrap" id="demo"><div class="proof-text"><h2>{escape(c["demoTitle"])}</h2>
    <a class="watch" data-product-link href="{GUIDE}">{escape(c["readGuide"])} <span aria-hidden="true">→</span></a></div>{demo_video}</section>
  <section class="studio" id="formats"><div class="wrap">
    <div class="formats"><div><h2>{escape(c["formatHeading"])}</h2><p>{escape(c["formatText"])}</p></div><dl>{formats}</dl></div>
    <div class="desktop"><div class="desktop-intro"><h2>{escape(c["workspaceHeading"])}</h2><p>{escape(c["workspaceText"])}</p></div>
      <figure><a href="{media}desktop-grade-{language}.webp" aria-label="{escape(c["viewFull"])} · {escape(c["workspaceCaption"])}"><img loading="lazy" src="{media}desktop-grade-{language}.webp" width="1440" height="904" alt="{escape(c["desktopAlt"])}"></a><figcaption>{escape(c["workspaceCaption"])}</figcaption></figure>
    </div>
  </div></section>
  <section class="wrap plans" id="pro"><h2>{escape(c["planHeading"])}</h2><div class="plans-grid">
    <div><h3>{escape(c["freeName"])}</h3><p class="amount">{escape(c["freeHeading"])}</p><p>{escape(c["freeText"])}</p></div>
    <div><h3>HUEO Pro</h3><p class="amount">{escape(c["proHeading"])}</p><p>{escape(c["proText"])}</p></div>
  </div>{store_button()}</section>
</main>'''
    canonical = SITE + path
    data = {
        "@context": "https://schema.org",
        "@type": "Article" if guide else "SoftwareApplication",
        "name": title if guide else "HUEO",
        "inLanguage": c["lang"], "url": canonical,
        "description": description,
    }
    if guide:
        data["headline"] = c["guideHeading"]
    else:
        data.update(applicationCategory="MultimediaApplication",
                    operatingSystem="iOS, iPadOS, macOS", downloadUrl=APP)
    cover_url = SITE + "assets/product/media/social-cover-" + language + ".jpg"
    html = f'''<!doctype html>
<html lang="{c["lang"]}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title><meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{SITE}en/{suffix}"><link rel="alternate" hreflang="zh-Hans" href="{SITE}zh/{suffix}">
  <link rel="alternate" hreflang="x-default" href="{SITE}en/{suffix}">
  <meta property="og:type" content="{"article" if guide else "website"}"><meta property="og:site_name" content="HUEO">
  <meta property="og:locale" content="{c["locale"]}"><meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{cover_url}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#131416">
  <link rel="icon" href="{media}favicon-32.png"><link rel="apple-touch-icon" href="{media}hueo-icon.png">
  <link rel="stylesheet" href="{prefix}assets/product/product.css"><script src="{prefix}assets/product/product.js" defer></script>
  <script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>
</head>
<body>{header}
{content}
{footer}
</body></html>
'''
    directory = ROOT / path
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    for language in ("en", "zh"):
        for guide in (False, True):
            render(language, guide)
    paths = ("", "privacy/", "privacy/terms.html", "en/", "zh/", "en/" + GUIDE, "zh/" + GUIDE)
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap.extend(f"  <url><loc>{SITE}{path}</loc></url>" for path in paths)
    (ROOT / "sitemap.xml").write_text("\n".join([*sitemap, "</urlset>", ""]), encoding="utf-8")
