"""Gemeinsame Bausteine: Layout, Navigation, Footer, Komponenten."""
import json
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
SITE = "https://www.gaertner-innsbruck.at"

with open(os.path.join(os.path.dirname(__file__), "images.json"), encoding="utf-8") as fh:
    IMAGES = json.load(fh)


# ---------------------------------------------------------------- Bilder
def src(pid):
    return "/assets/img/" + IMAGES[pid]["file"]


def img(pid, alt="", cls="", eager=False, sizes=None, extra=""):
    m = IMAGES[pid]
    attrs = [f'src="{src(pid)}"', f'alt="{escape(alt)}"', f'width="{m["w"]}"', f'height="{m["h"]}"']
    if cls:
        attrs.append(f'class="{cls}"')
    attrs.append('fetchpriority="high"' if eager else 'loading="lazy"')
    attrs.append('decoding="async"')
    if extra:
        attrs.append(extra)
    return "<img " + " ".join(attrs) + ">"


# ---------------------------------------------------------------- Icons
ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "ear": '<path d="M6 8.5a6.5 6.5 0 1 1 13 0c0 6-6 6-6 10a3.5 3.5 0 1 1-7 0"/><path d="M15 8.5a2.5 2.5 0 0 0-5 0v1a2 2 0 1 1 0 4"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "tool": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.8 3.8z"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M12 18v-6M9 15l3 3 3-3"/>',
    "train": '<rect x="4" y="3" width="16" height="16" rx="2"/><path d="M4 11h16M12 3v8M8 19l-2 3M16 19l2 3"/><circle cx="8.5" cy="15" r=".5"/><circle cx="15.5" cy="15" r=".5"/>',
    "car": '<path d="M5 17h14M5 17a2 2 0 1 0 4 0M15 17a2 2 0 1 0 4 0M3 17V11l2-5h14l2 5v6"/><path d="M3 11h18"/>',
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z" fill="currentColor" stroke="none"/>',
    "wave": '<path d="M2 12h2M6 8v8M10 5v14M14 8v8M18 10v4M22 12h0"/>',
    "drop": '<path d="M12 2.7s7 7.3 7 12.3a7 7 0 0 1-14 0c0-5 7-12.3 7-12.3z"/>',
    "moon": '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
    "ext": '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14 21 3"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "smartphone": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def btn(label, href, kind="primary", ic="arrow", extra=""):
    ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    i = icon(ic) if ic else ""
    return f'<a class="btn btn-{kind}" href="{href}"{ext}{extra}>{escape(label)}{i}</a>'


# ---------------------------------------------------------------- Stammdaten
PHONE_OPTIK = "+43 512 57 59 74"
TEL_OPTIK = "+43512575974"

LOCATIONS = [
    {
        "key": "gaertner-gmbh", "tag": "Optik", "name": "Gaertner Optik",
        "street": "Leopoldstraße 16", "zip": "6020 Innsbruck",
        "phone": "+43 512 57 59 74", "tel": "+43512575974", "mail": "optik@gaertner-innsbruck.at",
        "hours": [("Montag – Freitag", "09:00 – 18:00"), ("Samstag", "nach Terminvereinbarung")],
        "img": "Hwbk6TzX", "alt": "Geschäftsportal von Gaertner Optik in der Leopoldstraße 16, Innsbruck",
        "schema": "Optician", "oh": [("Mo-Fr", "09:00", "18:00")],
    },
    {
        "key": "gaertner-auditiv", "tag": "Hörakustik", "name": "Gaertner Auditiv – Hörakustik",
        "street": "Heiliggeiststraße 1a", "zip": "6020 Innsbruck",
        "phone": "+43 512 93 53 95", "tel": "+43512935395", "mail": "auditiv@gaertner-innsbruck.at",
        "hours": [("Montag – Freitag", "08:30 – 12:30 und 14:00 – 17:30")],
        "img": "68nriuJW", "alt": "Geschäftsportal von Gaertner Auditiv in der Heiliggeiststraße 1a, Innsbruck",
        "schema": "MedicalBusiness", "oh": [("Mo-Fr", "08:30", "12:30"), ("Mo-Fr", "14:00", "17:30")],
    },
    {
        "key": "gaertner-auditiv2", "tag": "Labor & Gehörschutz", "name": "Gaertner Auditiv 2 – Labor",
        "street": "Heiliggeiststraße 4", "zip": "6020 Innsbruck",
        "phone": "+43 512 57 01 59", "tel": "+43512570159", "mail": "gehoerschutz@gaertner-innsbruck.at",
        "hours": [("Montag – Freitag", "08:30 – 12:30 und 14:00 – 17:30")],
        "img": "srcIkyok", "alt": "Geschäftsportal von Gaertner Auditiv 2 – Labor in der Heiliggeiststraße 4, Innsbruck",
        "schema": "MedicalBusiness", "oh": [("Mo-Fr", "08:30", "12:30"), ("Mo-Fr", "14:00", "17:30")],
    },
    {
        "key": "see-sophie", "tag": "Nach Terminvereinbarung", "name": "See Sophie",
        "street": "Heiliggeiststraße 1b", "zip": "6020 Innsbruck",
        "phone": "+43 664 355 4804", "tel": "+436643554804", "mail": "info@seesophie.at",
        "hours": [("Montag – Freitag", "nach Terminvereinbarung")],
        "img": "bPuRiihV", "alt": "Geschäftsportal von See Sophie in der Heiliggeiststraße 1b, Innsbruck",
        "web": "https://seesophie.at/",
        "schema": "Optician", "oh": [],
    },
]


def maps_url(loc):
    from urllib.parse import quote_plus
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(f"{loc['street']}, {loc['zip']}")


# ---------------------------------------------------------------- Navigation
OPTIK_SUB = [
    ("Kontaktlinsen", "/optik/kontaktlinsen/"),
    ("Gleitsicht- und Bildschirmbrillen", "/optik/gleitsicht--und-bildschirmbrillen/"),
    ("Sport-, Schieß- und Tauchbrillen", "/optik/sport--schiess--und-tauchbrillen/"),
    ("Kinderbrillen", "/optik/kinderbrillen/"),
    ("Fassungen", "/optik/fassungen/"),
    ("Sonnenbrillen", "/optik/sonnenbrillen/"),
    ("Sehhilfen", "/optik/sehhilfen/"),
]
HOER_SUB = [
    ("Hörgeräte", "/hoerakustik/hoergeraete/"),
    ("Hörgeräte mit App verbinden", "/hoerakustik/hoergeraete-mit-app-verbinden/"),
    ("Tinnitus", "/hoerakustik/tinnitus/"),
    ("Zubehör und Reinigung", "/hoerakustik/zubehoer-und-reinigung/"),
]


def _cur(path, href):
    if href == "/":
        return ' aria-current="page"' if path == "/" else ""
    return ' aria-current="page"' if path.startswith(href) else ""


def nav_html(path):
    def sub(items):
        return "".join(f'<li><a href="{h}">{escape(t)}</a></li>' for t, h in items)

    return f'''
<header class="nav" id="top">
  <div class="nav__bar">
    <a class="nav__logo" href="/" aria-label="Gaertner – zur Startseite">
      <img src="{src('aD7O6cIa')}" alt="Gaertner" width="400" height="51" style="height:auto;width:136px">
    </a>
    <nav aria-label="Hauptnavigation">
      <ul class="nav__menu">
        <li class="nav__item"><a class="nav__link" href="/ueber-uns/"{_cur(path, '/ueber-uns/')}>Über uns</a></li>
        <li class="nav__item">
          <a class="nav__link" href="/optik/"{_cur(path, '/optik/')}>Optik {icon('chev')}</a>
          <div class="nav__drop">
            <a class="nav__feature" href="/optik/">{img('8ctIQgZ5', '', extra='aria-hidden="true"')}<strong>Optik</strong><small>Brillen, Kontaktlinsen, Sehhilfen</small></a>
            <ul class="nav__sub">{sub(OPTIK_SUB)}</ul>
          </div>
        </li>
        <li class="nav__item">
          <a class="nav__link" href="/hoerakustik/"{_cur(path, '/hoerakustik/')}>Hörakustik {icon('chev')}</a>
          <div class="nav__drop">
            <a class="nav__feature" href="/hoerakustik/">{img('bHR2vwHT', '', extra='aria-hidden="true"')}<strong>Hörakustik</strong><small>Hörgeräte, Tinnitus, Service</small></a>
            <ul class="nav__sub">{sub(HOER_SUB)}<li><a href="/gehoerschutz/">Gehörschutz</a></li></ul>
          </div>
        </li>
        <li class="nav__item"><a class="nav__link" href="/gehoerschutz/"{_cur(path, '/gehoerschutz/')}>Gehörschutz</a></li>
        <li class="nav__item"><a class="nav__link" href="https://seesophie.at/" target="_blank" rel="noopener">See Sophie</a></li>
        <li class="nav__item"><a class="nav__link" href="/kontakt/"{_cur(path, '/kontakt/')}>Kontakt</a></li>
      </ul>
    </nav>
    <div class="nav__actions">
      <a class="nav__phone" href="tel:{TEL_OPTIK}">{icon('phone')}{PHONE_OPTIK}</a>
      <a class="btn btn-primary btn-sm" href="/kontakt/#termin">Termin vereinbaren</a>
      <button class="nav__burger" aria-label="Menü öffnen" aria-expanded="false" aria-controls="mnav"><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mnav" id="mnav">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/ueber-uns/">Über uns</a></li>
    <li><details><summary>Optik</summary><ul><li><a href="/optik/">Übersicht Optik</a></li>{sub(OPTIK_SUB)}</ul></details></li>
    <li><details><summary>Hörakustik</summary><ul><li><a href="/hoerakustik/">Übersicht Hörakustik</a></li>{sub(HOER_SUB)}</ul></details></li>
    <li><a href="/gehoerschutz/">Gehörschutz</a></li>
    <li><a href="https://seesophie.at/" target="_blank" rel="noopener">See Sophie</a></li>
    <li><a href="/kontakt/">Kontakt</a></li>
  </ul>
  <div class="mnav__foot">
    <a class="btn btn-primary" href="/kontakt/#termin">Termin vereinbaren{icon('arrow')}</a>
    <a class="btn btn-ghost" href="tel:{TEL_OPTIK}">{icon('phone')}{PHONE_OPTIK}</a>
  </div>
</div>'''


CERTS = [
    ("jTRADTBl", "Meisterbetrieb"),
    ("uivYfGF9", "Certified by Austrian Standards"),
    ("toVeh4pW", "Regionaler Fachbetrieb 2024"),
    ("xYZ1eHnP", "Scharfsinn²"),
    ("Jb5B9o7L", "WKO Tirol – Gesundheitsberufe"),
    ("TPCZHUgk", "Zertifizierter Beltone-Partner"),
]
CERT_LINKS = {"xYZ1eHnP": "https://scharfsinn2.at/?suche=gaertner"}


def certs_html(cls="cert"):
    out = []
    for pid, alt in CERTS:
        inner = img(pid, alt)
        if pid in CERT_LINKS:
            out.append(f'<a class="{cls}" href="{CERT_LINKS[pid]}" target="_blank" rel="noopener">{inner}</a>')
        else:
            out.append(f'<span class="{cls}">{inner}</span>')
    return "".join(out)


def footer_html():
    loc_items = "".join(
        f'<li><a href="/kontakt/#{l["key"]}">{escape(l["name"])}</a></li>' for l in LOCATIONS)
    return f'''
<footer class="footer">
  <div class="footer__mtn" aria-hidden="true">{img('U678tAZy', '')}</div>
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="{src('rXpIri9S')}" alt="Gaertner – Für Auge und Ohr" width="400" height="104" loading="lazy" style="width:170px;height:auto">
        <p>Optiker und Hörakustiker in Innsbruck. Familienbetrieb seit mehr als 45 Jahren – mit hauseigenem Labor und eigener Werkstatt.</p>
        <div class="btn-row" style="margin-top:22px">
          <a class="btn btn-ghost btn-sm" href="tel:{TEL_OPTIK}">{icon('phone')}{PHONE_OPTIK}</a>
        </div>
      </div>
      <div>
        <h4>Optik</h4>
        <ul><li><a href="/optik/">Übersicht</a></li>{"".join(f'<li><a href="{h}">{escape(t)}</a></li>' for t, h in OPTIK_SUB)}</ul>
      </div>
      <div>
        <h4>Hörakustik</h4>
        <ul><li><a href="/hoerakustik/">Übersicht</a></li>{"".join(f'<li><a href="{h}">{escape(t)}</a></li>' for t, h in HOER_SUB)}<li><a href="/gehoerschutz/">Gehörschutz</a></li></ul>
      </div>
      <div>
        <h4>Standorte</h4>
        <ul>{loc_items}<li><a href="/ueber-uns/">Über uns</a></li></ul>
      </div>
    </div>
    <div class="footer__certs">{certs_html()}</div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> Gaertner GmbH · Leopoldstraße 16 · 6020 Innsbruck</span>
      <span><a href="/impressum/">Impressum</a> · <a href="/datenschutz/">Datenschutz</a></span>
    </div>
  </div>
  <div class="footer__word" aria-hidden="true">GAERTNER</div>
</footer>'''


# ---------------------------------------------------------------- Strukturierte Daten
def org_schema():
    deps = []
    for l in LOCATIONS:
        d = {
            "@type": l["schema"], "name": l["name"],
            "image": SITE + src(l["img"]),
            "telephone": l["phone"], "email": l["mail"],
            "address": {"@type": "PostalAddress", "streetAddress": l["street"], "postalCode": "6020",
                        "addressLocality": "Innsbruck", "addressCountry": "AT"},
        }
        if l["oh"]:
            d["openingHoursSpecification"] = [
                {"@type": "OpeningHoursSpecification",
                 "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                 "opens": o, "closes": c} for _, o, c in l["oh"]]
        if l.get("web"):
            d["url"] = l["web"]
        deps.append(d)
    return {
        "@context": "https://schema.org", "@type": "Optician", "@id": SITE + "/#organization",
        "name": "Gaertner – Optiker & Hörakustiker", "legalName": "Gaertner GmbH",
        "url": SITE + "/", "logo": SITE + src("rXpIri9S"), "image": SITE + src("b8B1MNaU"),
        "telephone": PHONE_OPTIK, "email": "optik@gaertner-innsbruck.at", "vatID": "ATU77352516",
        "address": {"@type": "PostalAddress", "streetAddress": "Leopoldstraße 16", "postalCode": "6020",
                    "addressLocality": "Innsbruck", "addressCountry": "AT"},
        "geo": {"@type": "GeoCoordinates", "latitude": 47.2622, "longitude": 11.3958},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "09:00", "closes": "18:00"}],
        "department": deps,
    }


def crumb_schema(crumbs):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + h}
                            for i, (n, h) in enumerate(crumbs)],
    }


# ---------------------------------------------------------------- Seitengerüst
def page(path, title, desc, body, og=None, schema=None, robots="index, follow", crumbs=None):
    canonical = SITE + path
    og_img = SITE + src(og or "b8B1MNaU")
    blocks = [org_schema()] if path == "/" else []
    if crumbs:
        blocks.append(crumb_schema(crumbs))
    if schema:
        blocks.extend(schema)
    ld = "".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in blocks)
    return f'''<!doctype html>
<html lang="de-AT" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#080a09">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_AT">
<meta property="og:site_name" content="Gaertner – Optiker & Hörakustiker">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preload" href="/assets/fonts/manrope-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v=1">
{ld}
</head>
<body>
<a class="skip" href="#main">Zum Inhalt springen</a>
{nav_html(path)}
<main id="main">
{body}
</main>
{footer_html()}
<script src="/assets/js/site.js?v=1" defer></script>
</body>
</html>
'''


def write(path, html):
    if path.endswith(".html"):
        out = os.path.join(DIST, path.lstrip("/"))
    else:
        out = os.path.join(DIST, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out


# ---------------------------------------------------------------- Komponenten
def crumbs_html(crumbs):
    items = []
    for i, (n, h) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{escape(n)}</li>')
        else:
            items.append(f'<li><a href="{h}">{escape(n)}</a></li>')
    return f'<nav aria-label="Brotkrümelnavigation"><ol class="crumbs">{"".join(items)}</ol></nav>'


def page_hero(eyebrow, h1, lead_html, image=None, alt="", crumbs=None, buttons=None, plain=False):
    media = f'<div class="phero__media">{img(image, alt, eager=True)}</div>' if image else ""
    cls = "phero" + (" phero--plain" if plain or not image else "")
    b = f'<div class="btn-row rv" style="--d:.3s">{"".join(buttons)}</div>' if buttons else ""
    c = crumbs_html(crumbs) if crumbs else ""
    return f'''
<section class="{cls}">
  {media}
  <div class="container">
    <div class="phero__inner">
      <div class="rv">{c}</div>
      <h1 class="h-xl rv" style="--d:.12s">{h1}</h1>
      <div class="lead rv" style="--d:.2s">{lead_html}</div>
      {b}
    </div>
  </div>
</section>'''


def gallery(name, items, kind="gallery"):
    """items: Liste von (pid, alt)."""
    btns = "".join(
        f'<button type="button" data-lb="{name}" data-full="{src(p)}" aria-label="Bild vergrößern: {escape(a or "Galerie")}">{img(p, a)}</button>'
        for p, a in items)
    if kind == "gallery" and len(items) > 12:
        return (f'<div class="gallery is-collapsed" id="g-{name}">{btns}</div>'
                f'<div style="text-align:center;margin-top:28px"><button type="button" class="btn btn-ghost" data-expand="g-{name}">'
                f'Alle {len(items)} Bilder anzeigen</button></div>')
    return f'<div class="{kind}">{btns}</div>'


def locations_html(heading=True):
    cards = []
    for i, l in enumerate(LOCATIONS):
        hours = "".join(f"<dt>{escape(d)}</dt><dd>{escape(h)}</dd>" for d, h in l["hours"])
        web = (f'<a href="{l["web"]}" target="_blank" rel="noopener">{icon("ext")}seesophie.at</a>'
               if l.get("web") else "")
        cards.append(f'''
<article class="loc spot rv" id="{l['key']}" style="--d:{i * 0.08:.2f}s">
  <div class="loc__img">{img(l['img'], l['alt'])}</div>
  <div class="loc__body">
    <span class="loc__tag">{escape(l['tag'])}</span>
    <h3>{escape(l['name'])}</h3>
    <address>{escape(l['street'])}<br>{escape(l['zip'])}</address>
    <dl>{hours}</dl>
    <div class="loc__links">
      <a href="tel:{l['tel']}">{icon('phone')}{escape(l['phone'])}</a>
      <a href="mailto:{l['mail']}">{icon('mail')}{escape(l['mail'])}</a>
      {web}
      <a href="{maps_url(l)}" target="_blank" rel="noopener">{icon('pin')}Anfahrt planen</a>
    </div>
  </div>
</article>''')
    head = ""
    if heading:
        head = f'''
  <div class="sec-head">
    <div class="rv"><h2 class="h-lg">Vier Adressen.<br><em>Ein Team</em> in Innsbruck.</h2></div>
    <p class="lead rv" style="--d:.1s">Sie erreichen uns in nur 7 Gehminuten vom Hauptbahnhof. Parken können Sie bequem in der „Casino-Garage“, die nur ca. 3 Gehminuten entfernt ist.</p>
  </div>'''
    return f'''
<section class="section section--line" aria-label="Standorte">
  <div class="container">{head}
    <div class="locs">{"".join(cards)}</div>
  </div>
</section>'''


def cta(title_html, text, buttons, bg="U678tAZy"):
    return f'''
<section class="section section--tight">
  <div class="container">
    <div class="cta rv">
      <div class="cta__bg" aria-hidden="true">{img(bg, '')}</div>
      <h2 class="h-lg">{title_html}</h2>
      <p class="lead">{text}</p>
      <div class="btn-row">{"".join(buttons)}</div>
    </div>
  </div>
</section>'''


def default_cta():
    return cta("Wir nehmen uns <em>Zeit</em> für Sie.",
               "Vereinbaren Sie einen Termin in einem unserer Fachgeschäfte in Innsbruck – telefonisch oder über unser Anfrageformular.",
               [btn("Termin vereinbaren", "/kontakt/#termin"),
                f'<a class="btn btn-ghost" href="tel:{TEL_OPTIK}">{icon("phone")}{PHONE_OPTIK}</a>'])


def split(text_html, media_html, rev=False, top=False, sticky=False):
    cls = "split" + (" split--rev" if rev else "") + (" split--top" if top else "")
    st = " sticky" if sticky else ""
    return f'''<div class="{cls}">
  <div class="rv">{text_html}</div>
  <div class="split__media rv{st}" style="--d:.1s">{media_html}</div>
</div>'''


def cards(items, cols=2, icons=None):
    out = []
    for i, (h, body) in enumerate(items):
        ic = f'<div class="card__icon">{icon(icons[i])}</div>' if icons else ""
        out.append(f'<article class="card spot rv" style="--d:{i * 0.08:.2f}s">{ic}<h3 class="h-sm">{h}</h3>{body}</article>')
    return f'<div class="cards-{cols}">{"".join(out)}</div>'


def downloads(items):
    out = "".join(
        f'<a class="dl" href="/assets/downloads/{f}" target="_blank" rel="noopener"><span class="dl__ic">{icon("file")}</span><span><b>{escape(t)}</b><span>PDF · {escape(s)}</span></span></a>'
        for t, f, s in items)
    return f'<div class="dls">{out}</div>'


def brands_marquee():
    logos = [("2xqdZYMV", "Oticon"), ("SGFbXw8q", "Signia"), ("ImKmWfi8", "Starkey"), ("Se05O5Zd", "Widex"),
             ("rQ1ybnao", "ReSound"), ("YhC1uobT", "Beltone"), ("cyNrf3lj", "audifon")]
    one = "".join(f'<span class="lg">{img(p, a)}</span>' for p, a in logos)
    dup = "".join(f'<span class="lg" aria-hidden="true">{img(p, "")}</span>' for p, a in logos)
    return f'<div class="marquee logos" style="--dur:40s"><div class="marquee__track">{one}{dup}</div></div>'
