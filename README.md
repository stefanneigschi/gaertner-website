# Gaertner Innsbruck – Website (Relaunch 2026)

Modernisierte, statische Website für **Gaertner – Optiker & Hörakustiker in Innsbruck**.
Branding, Fotos und Texte stammen von www.gaertner-innsbruck.at; Design und Technik sind neu.

## Struktur

```
build/            Generator (Python 3, keine Abhängigkeiten)
  build.py        Einstieg: erzeugt alle Seiten nach ./dist
  lib.py          Layout, Navigation, Footer, Standorte, Komponenten
  pages_*.py      Inhalte je Bereich (Start/Über uns, Optik, Hörakustik, Kontakt/Rechtliches)
  images.json     Bild-IDs der Altseite -> optimierte WebP-Dateien
dist/             Auslieferbare Website (wird von Netlify veröffentlicht)
  assets/css/site.css   Design-System
  assets/js/site.js     Interaktionen (Navigation, Reveal, Lightbox, Tabs)
  assets/img/           alle Fotos als WebP
  assets/fonts/         Manrope + Fraunces, lokal eingebunden (keine Google-Server)
  assets/downloads/     PDF-Broschüren
netlify.toml      Hosting-Konfiguration (publish = dist)
```

Texte ändern: in `build/pages_*.py` bearbeiten, dann `python3 build/build.py` ausführen.
CSS und JS werden direkt in `dist/assets/` gepflegt.

## Lokale Vorschau

```bash
python3 build/build.py
cd dist && python3 -m http.server 8080
```

## URLs

Alle bisherigen Adressen bleiben erhalten (z. B. `/optik/kontaktlinsen`, `/hoerakustik/tinnitus`),
damit Google-Rankings und bestehende Links weiter funktionieren. `/seesophie` leitet auf seesophie.at weiter.

## Formulare (Netlify Forms)

- `terminanfrage` (Kontakt)
- `kontaktlinsen-nachbestellung` (Kontaktlinsen)

Nach dem ersten Deploy in Netlify unter *Forms → Form notifications* die Empfänger-E-Mail eintragen.

## Vor dem Livegang

- [ ] Datenschutzerklärung rechtlich prüfen (neu verfasst für die statische Site; der alte Text wurde dynamisch nachgeladen und war nicht übernehmbar)
- [ ] Netlify-Formular-Benachrichtigungen einrichten
- [ ] Domain umstellen, danach Sitemap in der Google Search Console einreichen
