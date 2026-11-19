"""Optik: Übersicht und Unterseiten."""
from lib import (img, src, icon, btn, page, write, page_hero, locations_html, default_cta, gallery, split,
                 cards, downloads, OPTIK_SUB, TEL_OPTIK, PHONE_OPTIK, escape)

CONTACT_BTNS = [btn("Termin vereinbaren", "/kontakt/#termin"),
                f'<a class="btn btn-ghost" href="tel:{TEL_OPTIK}">{icon("phone")}{PHONE_OPTIK}</a>']


def related(current, items, label):
    chips = "".join(
        f'<a class="chip" href="{h}"{" aria-current=page" if h == current else ""}>{escape(t)}</a>'
        for t, h in items if h != current)
    return f'''
<section class="section--tight section--line" style="padding-block:56px">
  <div class="container">
    <p class="kicker rv" style="margin-bottom:18px">{escape(label)}</p>
    <div class="chips rv" style="--d:.06s">{chips}</div>
  </div>
</section>'''


def sub_page(cfg):
    """Gemeinsames Muster für Unterseiten (Optik und Hörakustik)."""
    crumbs = cfg["crumbs"]
    hero = page_hero(cfg["eyebrow"], cfg["h1"], cfg["intro"], image=cfg.get("hero"), alt=cfg.get("hero_alt", ""),
                     crumbs=crumbs, buttons=cfg.get("buttons", CONTACT_BTNS))
    main_img = f'<div class="frame frame--square">{img(cfg["img"], cfg["img_alt"])}</div>' if cfg.get("img") else ""
    sec = ""
    if cfg.get("h2"):
        text = f'''<span class="eyebrow">{escape(cfg.get("h2_eyebrow", cfg["eyebrow"]))}</span>
<h2 class="h-lg" style="margin:20px 0 26px">{cfg["h2"]}</h2>
<div class="prose">{cfg["h2_text"]}</div>'''
        sec = f'<section class="section"><div class="container">{split(text, main_img, rev=cfg.get("rev", False))}</div></section>'
    extra_top = cfg.get("extra_top", "")
    c = ""
    if cfg.get("cards"):
        c = f'''<section class="section section--line"><div class="container">{cards(cfg["cards"], cols=cfg.get("cols", 2), icons=cfg.get("icons"))}</div></section>'''
    extra = cfg.get("extra", "")
    rel = related(cfg["path"], cfg["siblings"], cfg["siblings_label"]) if cfg.get("siblings") else ""
    body = hero + sec + extra_top + c + extra + rel + default_cta()
    return page(cfg["path"], cfg["title"], cfg["desc"], body, og=cfg.get("og", cfg.get("hero")), crumbs=crumbs)


def P(*ps):
    return "".join(f"<p>{p}</p>" for p in ps)


OPTIK_CRUMB = [("Home", "/"), ("Optik", "/optik/")]


def optik():
    tiles = [
        ("9aJKUOZ7", "Fassungen", "/optik/fassungen/", "Brillenfassung"),
        ("dvW72NXB", "Sonnenbrillen", "/optik/sonnenbrillen/", "Sonnenbrillen"),
        ("rIyGRU4j", "Sport-, Schieß- und Tauchbrillen", "/optik/sport--schiess--und-tauchbrillen/", "Sportbrillen"),
        ("pRXlywUb", "Kinderbrillen", "/optik/kinderbrillen/", "Kinderbrillen"),
        ("XtqhwYns", "Gleitsicht- und Bildschirmbrillen", "/optik/gleitsicht--und-bildschirmbrillen/", "Gleitsichtbrille"),
        ("HPjHozSQ", "Sehhilfen", "/optik/sehhilfen/", "Sehhilfen"),
        ("Gv8pyj0e", "Kontaktlinsen", "/optik/kontaktlinsen/", "Kontaktlinse"),
    ]
    spans = ["span-5", "span-7", "span-4", "span-4", "span-4", "span-6", "span-6"]
    t = "".join(f'''<a class="tile tile--shade {spans[i]} spot rv" style="--d:{(i % 3) * .08:.2f}s" href="{h}">
  <div class="tile__bg">{img(p, a)}</div>
  <span class="kicker">Optik</span>
  <h3 class="h-md" style="display:flex;justify-content:space-between;align-items:end;gap:20px">{escape(n)}<span class="btn btn-ghost btn-sm" aria-hidden="true" style="flex-shrink:0;width:42px;padding:0">{icon('arrow')}</span></h3>
</a>''' for i, (p, n, h, a) in enumerate(tiles))

    body = page_hero(
        "Optik", "Kompetent beraten bei Ihrem <em>Optiker</em> in Innsbruck",
        P("Als Ihr Optikerfachgeschäft mit jahrzehntelanger Tradition stehen wir Ihnen in unserem Geschäft im Herzen von Innsbruck mit einem vielfältigen Sortiment an Fassungen, optischen Brillen, Sonnen- und Sportbrillen sowie Kontaktlinsen zur Verfügung. Besuchen Sie uns und lassen Sie sich von unserem geschulten Team beraten!"),
        image="8ctIQgZ5", alt="Frau mit Brille", crumbs=OPTIK_CRUMB, buttons=CONTACT_BTNS) + f'''
<section class="section">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><span class="eyebrow">Sortiment</span><h2 class="h-lg">Für jede <em>Sehsituation</em> die passende Lösung.</h2></div>
    </div>
    <div class="bento">{t}</div>
  </div>
</section>
<section class="section section--line">
  <div class="container">
    <div class="split">
      <div class="rv">
        <span class="eyebrow">Werkstatt</span>
        <h2 class="h-lg" style="margin:20px 0 26px">Ihr Weg zur <em>perfekten</em> Brille</h2>
        <div class="prose"><p>Eine optimal an Ihre Dioptrien angepasste Brille garantiert ein bestmögliches Seherlebnis in jeder Situation. In unserer hauseigenen Werkstätte wird Ihre Brille nach erfolgtem Sehtest in fachmännischer Handarbeit eingeschliffen. Wir bieten Ihnen auch einen Express-Service, damit Sie auf raschestem Weg zu Ihrer perfekt angepassten Brille kommen!</p></div>
      </div>
      <div class="rv" style="--d:.1s">
        <figure class="quote">
          <blockquote>„Dein Blick, unser Fokus“</blockquote>
          <figcaption><p style="margin:0">Ganz egal, ob neue Brille, Anpassung oder Brillenreparatur: Bei uns sind Sie immer bestens beraten. Dabei setzen wir bei den Brillen auf höchste Qualität und führen eine Vielzahl an Brillen österreichischer Hersteller. Profitieren auch Sie von unserer jahrelangen Erfahrung und unserem hervorragenden Kundenservice und besuchen Sie unser Geschäft in Innsbruck!</p></figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>
{locations_html()}
{default_cta()}'''
    return page("/optik/", "Ihr Optiker in Innsbruck | Optik Gaertner",
                "Als Optiker in Innsbruck bietet Optik Gaertner Ihnen alles von Brillenfassungen über Sport- und Sonnenbrillen bis hin zu Kontaktlinsen.",
                body, og="8ctIQgZ5", crumbs=OPTIK_CRUMB)


def kontaktlinsen():
    form = f'''
<section class="section section--line" id="nachbestellung" aria-labelledby="nb">
  <div class="container">
    <div class="split split--top">
      <div class="rv">
        <span class="eyebrow">Nachbestellung</span>
        <h2 class="h-lg" id="nb" style="margin:20px 0 22px">Kontaktlinsen <em>nachbestellen</em></h2>
        <p class="lead">Füllen Sie das Formular aus – wir melden uns zur Bestätigung. Lieferung per Post (5 € Versand) oder Abholung im Geschäft.</p>
        <div style="margin-top:34px">
          <p class="kicker" style="margin-bottom:14px">Harte und weiche Kontaktlinsen von Ihrem Optiker</p>
          <p class="muted">Erfahren Sie mehr über „Die Welt der Kontaktlinsen“</p>
          {downloads([("OPTICON Kontaktlinsen-Wegweiser", "opticon-kontaktlinsen-wegweiser.pdf", "Die Welt der Kontaktlinsen")])}
        </div>
      </div>
      <form class="card form rv" style="--d:.1s" name="kontaktlinsen-nachbestellung" method="POST" action="/danke/" data-netlify="true" netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="kontaktlinsen-nachbestellung">
        <p class="hp"><label>Nicht ausfüllen: <input name="bot-field"></label></p>
        <div class="field"><label for="nb-anrede">Anrede*</label><select id="nb-anrede" name="anrede" required><option value="">Bitte wählen</option><option>Frau</option><option>Herr</option><option>Divers</option><option>Keine Angabe</option></select></div>
        <div class="field"><label for="nb-geb">Geburtsdatum</label><input id="nb-geb" name="geburtsdatum" type="date"></div>
        <div class="field"><label for="nb-vn">Vorname*</label><input id="nb-vn" name="vorname" required autocomplete="given-name"></div>
        <div class="field"><label for="nb-nn">Nachname*</label><input id="nb-nn" name="nachname" required autocomplete="family-name"></div>
        <div class="field"><label for="nb-tel">Telefonnummer</label><input id="nb-tel" name="telefon" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="nb-mail">E-Mail-Adresse*</label><input id="nb-mail" name="email" type="email" required autocomplete="email"></div>
        <div class="field full"><label for="nb-ra">Rechnungsadresse*</label><input id="nb-ra" name="rechnungsadresse" required autocomplete="street-address"></div>
        <div class="field full"><label for="nb-la">Lieferadresse</label><input id="nb-la" name="lieferadresse" placeholder="Falls von Rechnungsadresse abweichend"></div>
        <div class="field full"><label for="nb-prod">Welche/s Produkt/e möchten Sie nachbestellen?</label><textarea id="nb-prod" name="produkte"></textarea></div>
        <div class="field full"><label for="nb-ver">Wie möchten Sie Ihre Bestellung erhalten?*</label><select id="nb-ver" name="versand" required><option value="">Option wählen</option><option>Lieferung per Post (5€ Versand)</option><option>Im Geschäft abholen</option></select></div>
        <label class="check full"><input type="checkbox" name="datenschutz" required> <span>Es werden personenbezogene Daten übermittelt und für die in der <a href="/datenschutz/">Datenschutzseite</a> beschriebenen Zwecke verwendet. *</span></label>
        <div class="full"><button class="btn btn-primary" type="submit">Nachbestellung absenden{icon('arrow')}</button></div>
      </form>
    </div>
  </div>
</section>'''
    gal = f'''<section class="section section--line"><div class="container">{gallery("linsen", [("IOnv6V6A", "Untersuchung für Kontaktlinsen"), ("jeaOoSmA", "Kontaktlinsenanpassung"), ("QAgfMLD5", "Kontaktlinsen beim Sport"), ("3WvmUbHj", "Kontaktlinsen im Alltag"), ("CccDpoEy", "Kontaktlinsen einsetzen"), ("6kTfwfyX", "Kontaktlinsenpflege")], "rail")}</div></section>'''
    return sub_page(dict(
        path="/optik/kontaktlinsen/", crumbs=OPTIK_CRUMB + [("Kontaktlinsen", "/optik/kontaktlinsen/")],
        title="Kontaktlinsen in Innsbruck | Optik Gaertner",
        desc="Optik Gaertner ist Ihr Partner, wenn es um Kontaktlinsen in Innsbruck geht. Hier erfahren Sie mehr über unsere Kontaktlinsen.",
        eyebrow="Kontaktlinsen", h1="Ihr kompetenter Ansprechpartner für <em>Kontaktlinsen</em> in Innsbruck",
        intro=P("Nicht immer ist eine Brille die optimale Sehhilfe. Für viele Menschen sind Kontaktlinsen oder eine Kombination aus Kontaktlinsen und Brille die bessere Alternative. Insbesondere die uneingeschränkte Rundumsicht und die klare Sicht auch beim Sport und im Wasser sind als Vorteile der Kontaktlinsen ins Treffen zu führen. Ihr Optiker berät Sie gerne!"),
        hero="9SwxnaT0", hero_alt="Kontaktlinsen",
        buttons=[btn("Linsen nachbestellen", "#nachbestellung"), btn("Termin vereinbaren", "/kontakt/#termin", "ghost")],
        img="wj2Wfg9m", img_alt="Kontaktlinse",
        h2="Was sind <em>Kontaktlinsen</em>?",
        h2_text=P("Kontaktlinsen sind kleine, auf der Tränenflüssigkeit „schwimmende“ Kunststoffschalen, die eine Fehlsichtigkeit korrigieren. Wie Brillengläser lassen sie auf der Netzhaut ein scharfes Bild entstehen. Während Brillen aufgrund des Abstandes zum Auge alle Gegenstände stark vergrößern oder verkleinern, sind diese Effekte bei Kontaktlinsen wesentlich geringer ausgeprägt. Eine präzise Anpassung der Kontaktlinsen an Ihre Sehstärke ist erforderlich."),
        cards=[("Harte und weiche Kontaktlinsen von Ihrem Optiker", P("Wir führen alle Arten von Kontaktlinsen und helfen Ihnen mit persönlicher Beratung, die passende Linse zu finden. Harte (formstabile) Kontaktlinsen sind besonders langlebig und gleiten beim Blinzeln auf dem Auge, sodass der Tränenfilm kontinuierlich erneuert wird und das Auge mit frischem Sauerstoff versorgt wird. Weiche Linsen bieten einen besonders hohen Tragekomfort. Bei uns erhalten Sie Ihre Linsen als Tages-, Monats und Jahreskontaktlinsen – lassen Sie sich von uns zu den Vor- und Nachteilen der verschiedenen Lösungen beraten!")),
               ("Alles rund um Kontaktlinsen und Pflege bei uns in Innsbruck", P("Neben individuell angepassten Kontaktlinsen bieten wir Ihnen auch alles, was Sie für die Pflege und Reinigung Ihrer Linsen benötigen. Besuchen Sie unser Optikerfachgeschäft in Innsbruck – unser kompetentes Team ist gerne für Sie da!"))],
        icons=["eye", "drop"],
        extra=gal + form,
        siblings=OPTIK_SUB, siblings_label="Weitere Themen in der Optik",
    ))


def gleitsicht():
    return sub_page(dict(
        path="/optik/gleitsicht--und-bildschirmbrillen/", crumbs=OPTIK_CRUMB + [("Gleitsicht- und Bildschirmbrillen", "/optik/gleitsicht--und-bildschirmbrillen/")],
        title="Gleitsichtbrillen vom Optiker in Innsbruck | Optik Gaertner",
        desc="Hier erfahren Sie mehr über Gleitsichtbrillen vom Optiker Optik Gaertner in Innsbruck. Wir nehmen uns Zeit und werden Sie gerne beraten.",
        eyebrow="Gleitsichtbrillen", h1="Bester Sehkomfort mit <em>Gleitsichtbrillen</em> vom Optiker in Innsbruck",
        intro=P("Eine Gleitsichtbrille vereint zwei Sehlösungen in einer: Sie ermöglicht sowohl Korrektion für das Sehen in der Ferne als auch für das Lesen. Zudem ist mit einer Gleitsichtbrille auch auf alle Distanzen dazwischen scharfe Sicht gewährleistet: Die Korrektion geht stufenlos von oben nach unten von der Fern- in die Nahsicht über. Als Ihr Optiker bieten wir Ihnen perfekt angepasste Gleitsichtbrillen für ein optimales Seherlebnis!"),
        hero="WAY9RGSS", hero_alt="Gleitsichtbrille",
        img="h0xYbXwo", img_alt="Gleitsichtbrille",
        h2="Für wen ist eine <em>Gleitsichtbrille</em> geeignet?",
        h2_text=P("Sind Sie es als Alterssichtiger leid, ständig die Lesebrille auf- und abzusetzen? Oder kommt zu Ihrer Kurzsichtigkeit, Weitsichtigkeit oder Hornhautverkrümmung eine Alterssichtigkeit hinzu? Dann könnte eine Gleitsichtbrille die optimale Sehlösung für Sie sein. Ihr Optiker berät Sie gerne!"),
        cards=[("Individuell angepasste Brillen von Ihrem Optiker", P("Für eine optimale Sicht braucht es qualitativ hochwertige Brillengläser, die individuell an Ihre Sehstärke angepasst sind. Wir nehmen uns Zeit, das optimale Glas für Ihre Bedürfnisse zu finden, und sorgen für eine präzise Anpassung. Vertrauen Sie auf unsere jahrelange Erfahrung und unser umfangreiches Fachwissen.")),
               ("Fragen? Wir sind für Sie da!", P("Haben Sie Fragen zum Thema Gleitsichtbrille oder möchten Sie sich von uns persönlich beraten lassen? Wir sind gerne für Sie da und freuen uns auf Ihren Besuch in unserem Optikerfachgeschäft in Innsbruck."))],
        icons=["eye", "chat"],
        siblings=OPTIK_SUB, siblings_label="Weitere Themen in der Optik",
    ))


def sport():
    gal = f'''<section class="section section--line"><div class="container">{gallery("sport", [("DGhEy4x6", "Sportbrille beim Golfen"), ("vCoMzAgu", "Golfbrille"), ("ZEejC8P0", "Sportbrille am Golfplatz"), ("rblnPZNZ", "Radbrille"), ("dKq8jNV3", "Sportbrille beim Radfahren"), ("vqMWdy0n", "Sonnenbrille beim Wandern")], "rail")}</div></section>'''
    return sub_page(dict(
        path="/optik/sport--schiess--und-tauchbrillen/", crumbs=OPTIK_CRUMB + [("Sport-, Schieß- und Tauchbrillen", "/optik/sport--schiess--und-tauchbrillen/")],
        title="Sportbrillen vom Optiker in Innsbruck | Optik Gaertner",
        desc="Sie suchen eine passende Sportbrille vom Optiker? Dann sind Sie bei Optik Gaertner in Innsbruck genau richtig.",
        eyebrow="Sportbrillen", h1="Hochwertige <em>Sportbrillen</em> vom Optiker in Innsbruck",
        intro=P("Ob beim Laufen, Radfahren oder Skifahren: Beim Sport ist eine klare und unbeeinträchtigte Sicht grundlegende Voraussetzung für Sicherheit und optimale Leistung. In unserem Optikerfachgeschäft erwarten Sie robuste, bruchsichere und biegsame Sonnen- und Sportbrillen mit kratzfesten Gläsern, mit denen Sie für alle Situationen bestens gerüstet sind!"),
        hero="jKjdFFJr", hero_alt="Sportler mit Sportbrille",
        img="MPbDRrxA", img_alt="Sportbrillen",
        h2="Qualitätsbrillen für <em>jede Sportart</em>",
        h2_text=P("Unsere große Auswahl an hochwertigen Sportbrillen lässt keine Wünsche offen. Ganz egal, ob Sie eine Laufbrille mit perfektem Sitz und Windschutz bei gleichzeitig optimaler Belüftung oder eine Golfbrille für natürliches Sehen bei allen Lichtverhältnissen und kontraststeigernder Wirkung suchen: Bei uns werden Sie fündig!"),
        cards=[("Die passende Brille für Ihre Anforderung", P("Die Sportausübung stellt besondere Anforderungen an eine Sonnenbrille. Daher ist es wichtig, die Sonnenbrille präzise nach der Sportart auszuwählen – insbesondere, was die Tönung der Gläser betrifft. So sind etwa beim Laufen gelbe Gläser für kontrastreiches Sehen und schnelles Erfassen von Unebenheiten ideal. Bei Sport auf Schnee oder Wasser hingegen muss die Brille für bestmögliche Sicherheit an die stärkere Reflexion der Sonnenstrahlen angepasst sein.")),
               ("Wir beraten Sie gerne!", P("Besuchen Sie unser Optikerfachgeschäft in Innsbruck, lassen Sie sich von unserem kompetenten Team verschiedene Modelle zeigen und umfassend über die Unterschiede und Eigenschaften informieren. Wir helfen Ihnen, die perfekte Brille für Ihre Sportausübung zu finden!"))],
        icons=["spark", "chat"],
        extra=gal,
        siblings=OPTIK_SUB, siblings_label="Weitere Themen in der Optik",
    ))


def kinder():
    return sub_page(dict(
        path="/optik/kinderbrillen/", crumbs=OPTIK_CRUMB + [("Kinderbrillen", "/optik/kinderbrillen/")],
        title="Kinderbrillen vom Optiker in Innsbruck | Optik Gaertner",
        desc="Optik Gaertner bietet Ihnen eine Vielzahl an Kinderbrillen vom Optiker in Innsbruck. Besuchen Sie uns - wir werden Sie gerne beraten.",
        eyebrow="Kinderbrillen", h1="Modische <em>Kinderbrillen</em> von Ihrem Optiker in Innsbruck",
        intro=P("Gutes Sehen ist eine wichtige Grundlage dafür, dass ein Kind adäquat mit seiner Umwelt interagieren und sich optimal entwickeln kann. Als Ihr Optikerfachgeschäft bieten wir Ihnen bestens angepasste Kinderbrillen mit bruchsicheren Gläsern und Fassungen."),
        hero="EeQ7WmX3", hero_alt="Kinder mit Brillen",
        img="pRXlywUb", img_alt="Kinderbrillen",
        h2="Qualitätsbrillen für <em>Kinder</em>",
        h2_text=P("Kinder nehmen die Welt vorwiegend mit ihren Augen wahr – scharfe und klare Sicht ist daher besonders wichtig, damit ein Kind Freude daran hat, zu lernen und die Welt zu erkunden. Bei uns erwartet Sie eine große Auswahl an qualitativ hochwertigen Kinderbrillen, die auch beim wilden Toben und Spielen nicht zum Sicherheitsrisiko werden!"),
        cards=[("Eine Brille, die auch Ihrem Kind gefällt", P("Benötigt Ihr Kind eine Brille, so sollte auf guten Sitz, biegsame und leichte Fassungen sowie bruchsichere Gläser geachtet werden. Doch damit das Kind die Brille auch gerne trägt, spielt das Design ebenfalls eine wichtige Rolle. Bei uns finden Sie zahlreiche verschiedene Modelle von schlicht über bunt bis zum Lieblingscomic – lassen Sie Ihr Kind selbst aussuchen!")),
               ("Wir sind für Sie und Ihr Kind da", P("Eine Sehschwäche ist beim Kind oft schwer zu erkennen. Nehmen Sie daher regelmäßige Kontrolluntersuchungen beim Augenarzt in Anspruch! Wird eine Sehschwäche festgestellt, so stehen wir Ihnen mit unserer Expertise rund um die Brille gerne zur Verfügung!"))],
        icons=["heart", "users"],
        siblings=OPTIK_SUB, siblings_label="Weitere Themen in der Optik",
    ))


def fassungen():
    return sub_page(dict(
        path="/optik/fassungen/", crumbs=OPTIK_CRUMB + [("Fassungen", "/optik/fassungen/")],
        title="Brillenfassung in Innsbruck | Optik Gaertner",
        desc="Hier erfahren Sie mehr über die Brillenfassungen von Optik Gaertner in Innsbruck. Vereinbaren Sie einen Termin - wir freuen uns auf Sie.",
        eyebrow="Fassungen", h1="Ihre modische <em>Brillenfassung</em> vom Augenoptiker in Innsbruck",
        intro=P("So unterschiedlich BrillenträgerInnen sind, so vielfältig und variabel sind auch Brillenfassungen. Brillen sind heute viel mehr als nur Sehbehelf – sie sind modisches Accessoire und drücken Persönlichkeit aus. In unserem Geschäft in Innsbruck erwartet Sie eine Vielzahl an Möglichkeiten und Variationen."),
        hero="Nt3znHfI", hero_alt="Verkaufsraum mit Brillenfassungen bei Gaertner Optik",
        img="E8jTa2Xn", img_alt="Frau mit schöner Brillenfassung",
        h2="Brillenfassungen aus <em>hochwertigen</em> Materialien",
        h2_text=P("Brillen sind in vielen verschiedenen Materialien und Ausführungen erhältlich. Ob Kunststoff, Titan, Holz, Leder oder Horn: Wir haben auch für Ihren Geschmack die passende Brille. Bei den Stilen können Sie zwischen runden und eckigen Brillen, großen und kleinen Gläsern, klassisch, modern oder trendig wählen. Ob bunt und extravagant oder schlicht und dezent: Bringen Sie mit einer attraktiven Brillenfassung vom Optiker Ihre Persönlichkeit zum Ausdruck!"),
        cards=[("Individuell beraten bei Ihrem Optiker", P("Mit unserer fachkundigen Beratung finden Sie garantiert die passende Brille. Unser großes Sortiment an Top-Marken lässt keine Wünsche offen und steht für höchste Qualität und Sicherheit! Selbstverständlich gehen wir auch auf Ihre individuellen Bedürfnisse ein und haben auch das passende Modell für Nickel- oder Kunststoffallergiker!")),
               ("Perfekt angepasste Brille von Optik Gaertner", P("Um ein optimales Seherlebnis zu gewährleisten, sollten Sie auf individuell angepasste Brillen von Ihrem Optiker setzen. Unser hervorragend geschultes und erfahrenes Team weiß, worauf es dabei ankommt."))],
        icons=["chat", "tool"],
        siblings=OPTIK_SUB, siblings_label="Weitere Themen in der Optik",
    ))


def sonnen():
    return sub_page(dict(
        path="/optik/sonnenbrillen/", crumbs=OPTIK_CRUMB + [("Sonnenbrillen", "/optik/sonnenbrillen/")],
        title="Sonnenbrille vom Optiker in Innsbruck | Optik Gaertner",
        desc="Hier erfahren Sie mehr über die Sonnenbrille vom Optiker Optik Gaertner in Innsbruck. Wir beraten Sie gerne - rufen Sie uns an.",
        eyebrow="Sonnenbrillen", h1="Optimal geschützt mit Ihrer <em>Sonnenbrille</em> vom Optiker in Innsbruck",
        intro=P("Ganz egal, ob Sommer oder Winter: Sonnenlicht blendet nicht nur unangenehm, sondern kann Ihre Augen durch die stärker werdende UV-Strahlung auch dauerhaft schädigen. Mit einer hochwertigen Sonnenbrille von Ihrem Optiker sind Sie in jeder Situation bestens geschützt."),
        hero="Dhm8N1JE", hero_alt="Sonnenbrille",
        img="F7tCbmDB", img_alt="Sonnenbrille",
        h2="Sonnenbrillen in <em>höchster</em> Qualität",
        h2_text=P("In unserem Optikerfachgeschäft erwartet Sie eine große Auswahl an modischen und hochwertigen Sonnenbrillen. Wichtige Qualitätskriterien sind dabei das CE-Zeichen, die Bügelaufschrift EN 1836:1997 sowie 100% UV-Schutz. Unser Team weiß genau, welche Sonnenbrille für welche Situation passt, und berät Sie fachkundig. Gerne können Sie bei uns auch Ihre Sonnenbrille auf ihren UV-Schutz testen lassen."),
        cards=[("Sonnenschutz in jeder Situation", P("Nicht jede Sonnenbrille eignet sich für jede Situation: Ob beim Sport, Autofahren, Relaxen oder im Schnee – überall werden andere Anforderungen an die Brille gestellt. Wir führen eine breite Palette an modischen Sonnenbrillen in höchster Qualität und helfen Ihnen gerne, das passende Modell zu finden.")),
               ("Qualitätsbrillen vom Optiker", P("Bei Dunkelheit wird die Pupille weiter, um mehr Licht ins Auge eintreten zu lassen – bei Helligkeit hingegen verkleinert sich die Pupille. Sonnenbrillen minderer Qualität verfügen oft über zu dunkle Gläser, die diesen natürlichen Schutzmechanismus außer Kraft setzen und zu viel Licht ins Auge lassen. Mit unseren hochwertigen Brillen sind Sie auf der sicheren Seite."))],
        icons=["spark", "shield"],
        siblings=OPTIK_SUB, siblings_label="Weitere Themen in der Optik",
    ))


def sehhilfen():
    return sub_page(dict(
        path="/optik/sehhilfen/", crumbs=OPTIK_CRUMB + [("Sehhilfen", "/optik/sehhilfen/")],
        title="Sehhilfen vom Optiker in Innsbruck | Optik Gaertner",
        desc="Sie benötigen Sehhilfen vom Optiker? Dann sind Sie bei Optik Gaertner in Innsbruck genau richtig. Besuchen Sie uns - wir freuen uns auf Sie.",
        eyebrow="Sehhilfen", h1="Hochwertige <em>Sehhilfen</em> von Ihrem Optiker in Innsbruck",
        intro=P("Reichen normale Brillen nicht mehr aus, so bedarf es besonderer Sehhilfen. Als Ihr Optikerfachgeschäft bieten wir Ihnen vielfältige Sehhilfen, die Ihnen den Alltag erleichtern – ob Lupensystem oder komplette Arbeitsplatzausstattung mit Vergrößerungssoftware und Sprachausgabe für Computer."),
        hero="bn8iBcmT", hero_alt="Sehhilfen und Lupen",
        img="D6DBfzJI", img_alt="Lupe als Sehhilfe beim Lesen",
        h2="Kompetent beraten bei Ihrem <em>Fachmann</em>",
        h2_text=P("Eine fundierte Beratung spielt eine zentrale Rolle, wenn es um die Auswahl der passenden Sehhilfe oder Spezialoptik geht. Mit unserer jahrelangen Erfahrung in diesem Bereich haben wir für jeden Anwendungs- oder Aufgabenbereich das passende Produkt und helfen Ihnen, die optimale Lösung für Ihr Anforderungsprofil zu finden."),
        cards=[("Wir haben die passende Sehlösung für Sie", P("Welche Sehhilfe für Sie am besten geeignet ist, hängt vor allem vom Vergrößerungsbedarf ab. Im Idealfall kommen Sie mit einer Lesevorlage zu uns, damit wir die passende Spezialoptik für Sie finden können. Ob Videolupen, Standleseglas, Pocket Viewer, Laborbrille oder Kantenfilterbrille – wir haben die Sehhilfe, die Sie bestmöglich unterstützt.")),
               ("Lassen Sie sich von uns beraten", P("Als Ihr Optiker verfügen wir über ein umfangreiches Know-how in Sachen Sehhilfen und helfen Ihnen gerne bei der Auswahl. Schauen Sie in unserem Geschäft in Innsbruck vorbei und lassen Sie sich von unserem kompetenten und freundlichen Team beraten – wir sind gerne für Sie da."))],
        icons=["eye", "chat"],
        siblings=OPTIK_SUB, siblings_label="Weitere Themen in der Optik",
    ))


def build():
    write("/optik/", optik())
    write("/optik/kontaktlinsen/", kontaktlinsen())
    write("/optik/gleitsicht--und-bildschirmbrillen/", gleitsicht())
    write("/optik/sport--schiess--und-tauchbrillen/", sport())
    write("/optik/kinderbrillen/", kinder())
    write("/optik/fassungen/", fassungen())
    write("/optik/sonnenbrillen/", sonnen())
    write("/optik/sehhilfen/", sehhilfen())
