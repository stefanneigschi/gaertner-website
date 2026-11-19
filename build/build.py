"""Erzeugt die statische Website in ./dist  —  Aufruf: python3 build/build.py"""
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pages_home, pages_optik, pages_hoer, pages_misc  # noqa: E402
from lib import DIST, SITE  # noqa: E402

PAGES = [
    "/", "/ueber-uns/", "/optik/", "/optik/kontaktlinsen/", "/optik/gleitsicht--und-bildschirmbrillen/",
    "/optik/sport--schiess--und-tauchbrillen/", "/optik/kinderbrillen/", "/optik/fassungen/",
    "/optik/sonnenbrillen/", "/optik/sehhilfen/", "/hoerakustik/", "/hoerakustik/hoergeraete/",
    "/hoerakustik/hoergeraete-mit-app-verbinden/", "/hoerakustik/tinnitus/",
    "/hoerakustik/zubehoer-und-reinigung/", "/gehoerschutz/", "/kontakt/", "/impressum/", "/datenschutz/",
]


def main():
    for mod in (pages_home, pages_optik, pages_hoer, pages_misc):
        mod.build()
    today = date.today().isoformat()
    urls = "".join(
        f"<url><loc>{SITE}{p}</loc><lastmod>{today}</lastmod><priority>{'1.0' if p == '/' else '0.7'}</priority></url>"
        for p in PAGES)
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"User-agent: *\nAllow: /\nDisallow: /danke/\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(PAGES)} Seiten + Danke/404 nach {DIST} geschrieben.")


if __name__ == "__main__":
    main()
