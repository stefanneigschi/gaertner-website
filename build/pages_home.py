"""Startseite und Über uns."""
from lib import (img, src, icon, btn, page, write, locations_html, default_cta, cta, brands_marquee,
                 gallery, certs_html, OPTIK_SUB, HOER_SUB, TEL_OPTIK, PHONE_OPTIK, escape)

REVIEWS = [
    ("Paul F.", "Mir ist eine Kontaktlinse gerissen, für meinen Beruf ein absoluter Notfall. Habe angerufen und sofort eine Ersatzlinse bekommen, obwohl ich nicht mal Kunde dort bin! Vielen Danke an euch!😃"),
    ("Madina A.", "Seit Jahren Stammkundin und sehr zufrieden👍🏻alles tip top …"),
    ("Rinaldo E.", "Sehr kompetent. Sehr freundlich. Sehr zufrieden."),
    ("Matthias Z.", "Vielen Dank für den tollen Service und eure Unterstützung!"),
    ("Istki", "Beste fachliche Beratung und sehr herzlicher Umgang mit den Kunden, so kommt man zu einer perfekten Brille."),
    ("lulu g.", "Tolles Team. Super Chefin. Mega Nice. Daumen hoch. Die Akustik ist auch nicht von schlechten Eltern."),
]


def review_card(name, text, hidden=False):
    stars = "".join(icon("star") for _ in range(5))
    ah = ' aria-hidden="true"' if hidden else ""
    return f'''<figure class="review"{ah}>
  <div class="review__stars" aria-label="5 von 5 Sternen">{stars}</div>
  <p>{escape(text)}</p>
  <footer><span class="review__av">{escape(name[0].upper())}</span><span><b>{escape(name)}</b>Google-Bewertung · 14.01.2025</span></footer>
</figure>'''


def reviews_html():
    a = REVIEWS[:3] + REVIEWS[3:]
    row1 = "".join(review_card(n, t) for n, t in a)
    row1d = "".join(review_card(n, t, True) for n, t in a)
    b = REVIEWS[3:] + REVIEWS[:3]
    row2 = "".join(review_card(n, t, True) for n, t in b)
    return f'''
<section class="section section--line" aria-labelledby="bewertungen">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><h2 class="h-lg" id="bewertungen">Was unsere <em>Kundinnen und Kunden</em> sagen.</h2></div>
      <p class="lead rv" style="--d:.1s">Auszüge aus Google-Bewertungen für Gaertner in Innsbruck.</p>
    </div>
  </div>
  <div class="marquee rv" style="--dur:70s"><div class="marquee__track">{row1}{row1d}</div></div>
  <div class="marquee marquee--rev rv" style="--dur:80s;margin-top:18px"><div class="marquee__track">{row2}{row2}</div></div>
</section>'''


def home():
    optik_chips = "".join(f'<a class="chip" href="{h}">{escape(t)}</a>' for t, h in OPTIK_SUB)
    hoer_chips = "".join(f'<a class="chip" href="{h}">{escape(t)}</a>' for t, h in HOER_SUB)
    orbit = [("ASx0CzHt", "Otoplastik-Aufträge im Labor"), ("FDH0e586", "Lackierung einer Otoplastik"),
             ("Qj6mg6fy", "Otoplastik-Varianten"), ("ZsBSi6g0", "Tauchvorgang bei der Otoplastik-Fertigung"),
             ("k0mqDGka", "Bearbeitung einer Otoplastik"), ("o3eZSKIP", "Laser in der Otoplastik-Fertigung"),
             ("44Fr6nHT", "Werkstatt für Brillen")]
    n = len(orbit)
    orbit_html = "".join(
        f'<li style="--a:{round(360 / n * i)}deg">{img(p, a)}</li>' for i, (p, a) in enumerate(orbit))

    body = f'''
<section class="hero">
  <div class="hero__media">
    <picture>
      {img('b8B1MNaU', 'Luchs mit grünen Augen – Symbol für geschärfte Sinne', eager=True)}
    </picture>
  </div>
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container hero__content">
    <h1 class="hero__h1 rv" style="--d:.08s">Gaertner – Optiker &amp; Hörakustiker mit Herz in Innsbruck</h1>
    <p class="h-display hero__claim rv" style="--d:.16s">Ihre Sinne<br>in <em class="grad">Bestform.</em></p>
    <p class="hero__sub rv" style="--d:.24s">Präzision für <em>Augen</em> &amp; <em>Ohren</em>.</p>
    <div class="btn-row rv" style="--d:.32s;margin-bottom:clamp(40px,6vw,72px)">
      {btn('Termin vereinbaren', '/kontakt/#termin')}
      {btn('Online-Hörtest', 'https://digitalhearingtest.com/de-AT/Gaertner/1', 'ghost', 'ext')}
    </div>
    <div class="hero__stats rv" style="--d:.4s">
      <div class="stat"><b><span data-count="45">45</span><sup>+</sup></b><span>Jahre Erfahrung</span></div>
      <div class="stat"><b><span data-count="3">3</span></b><span>Fachgeschäfte in Innsbruck</span></div>
      <div class="stat"><b><span data-count="10">10</span><sup>min</sup></b><span>Schnellreparatur Hörgeräte</span></div>
      <div class="stat"><b>Meister</b><span>Betrieb mit eigenem Labor</span></div>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true">Scrollen</div>
</section>

<section class="section">
  <div class="container">
    <p class="statement" data-words>Gutes Sehen und gutes Hören bedeuten Lebensfreude, Sicherheit und echte Nähe zu anderen Menschen. Genau dafür nehmen wir uns bei Gaertner Zeit.</p>
    <div class="split" style="margin-top:clamp(60px,8vw,110px)">
      <div class="rv prose">
        <p>Als Optiker und Hörakustiker in Innsbruck begleiten wir Sie persönlich auf dem Weg zu besserem Sehen und Hören – mit maßgeschneiderten Lösungen, ehrlicher Beratung und viel Erfahrung.</p>
        <p>Als traditionelles Familienunternehmen stehen wir für Qualität, Handwerk und echte Menschlichkeit. Bei uns sind Sie keine Nummer, sondern ein Mensch mit individuellen Bedürfnissen – und genau darauf stimmen wir Ihre Seh- und Hörlösungen ab.</p>
        <p style="margin-top:28px"><a class="link-arrow" href="/ueber-uns/">Mehr über unseren Familienbetrieb {icon('arrow')}</a></p>
      </div>
      <div class="split__media rv" style="--d:.1s">
        <div class="frame frame--wide">{img('84dzbumg', 'Johannes Grimm, Sophie Grimm-Gaertner und Joseph Gaertner')}</div>
        <div class="badge-float">{img('jTRADTBl', 'Meisterbetrieb')}<div><b>Meisterbetrieb</b><span>Johannes Grimm, Sophie Grimm-Gaertner, Joseph Gaertner</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--line" aria-labelledby="leistungen">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><h2 class="h-lg" id="leistungen">Für <em>Auge</em> und <em>Ohr</em> – alles aus einer Hand.</h2></div>
      <p class="lead rv" style="--d:.1s">Zwei Fachbereiche, ein Anspruch: präzise Anpassung, geprüfte Qualität und Beratung, die sich nach Ihnen richtet.</p>
    </div>
    <div class="bento">
      <article class="tile tile--xl tile--shade span-7 spot rv">
        <div class="tile__bg">{img('9aJKUOZ7', 'Mann mit Brille')}</div>
        {img('QDyy9G7F', '', 'tile__icon', extra='aria-hidden="true"')}
        <h2 class="h-md">Brillen vom Optiker</h2>
        <p>In unserem Optikerfachgeschäft dreht sich alles um Ihr bestes Sehen – und um Ihren persönlichen Stil. Von der Alltagsbrille über Sport- und Sonnenbrillen bis hin zu Kontaktlinsen finden Sie bei uns eine große Auswahl hochwertiger Produkte. Modische Fassungen bekannter Marken, präzise angepasste Brillengläser und verschiedene Beschichtungen für mehr Komfort und Langlebigkeit sorgen dafür, dass Sie nicht nur gut sehen, sondern sich auch rundum wohlfühlen.</p>
        <div class="chips"><a class="chip" href="/optik/">Alles zur Optik {icon('arrow')}</a>{optik_chips}</div>
      </article>
      <article class="tile tile--xl tile--shade span-5 spot rv" style="--d:.1s">
        <div class="tile__bg">{img('9WuOHd5l', 'Hörgeräte mit Ladestation')}</div>
        {img('iDq0d80Y', '', 'tile__icon', extra='aria-hidden="true"')}
        <h2 class="h-md">Alles rund ums Hören</h2>
        <p>In unserem Hörgerätefachgeschäft in Innsbruck dreht sich alles um Ihr bestes Hören – und um Ihre Lebensqualität. Von modernen Hörsystemen für den Alltag über innovative Lösungen für anspruchsvolle Hörsituationen bis hin zu individuellem Gehörschutz finden Sie bei uns eine große Auswahl hochwertiger Produkte.</p>
        <div class="chips"><a class="chip" href="/hoerakustik/">Alles zur Hörakustik {icon('arrow')}</a>{hoer_chips}</div>
      </article>
      <article class="tile tile--shade span-4 spot rv">
        <div class="tile__bg">{img('8kZmBk5n', 'Auge in Nahaufnahme')}</div>
        <h3 class="h-sm">Harte und weiche Linsen, individuell angepasst</h3>
        <div class="chips"><a class="chip" href="/optik/kontaktlinsen/">Kontaktlinsen {icon('arrow')}</a></div>
      </article>
      <article class="tile tile--shade span-4 spot rv" style="--d:.08s">
        <div class="tile__bg">{img('tL1u498S', 'Jäger mit maßgefertigtem Gehörschutz')}</div>
        <h3 class="h-sm">Maßgefertigt in unserem eigenen Labor – made in Tirol</h3>
        <div class="chips"><a class="chip" href="/gehoerschutz/">Gehörschutz {icon('arrow')}</a></div>
      </article>
      <article class="tile tile--shade span-4 spot rv" style="--d:.16s">
        <div class="tile__bg">{img('BuBDRg7l', 'Großmutter liest mit ihren Enkelkindern ein Buch')}</div>
        <p style="color:#fff">Diskrete und leistungsstarke Hörgeräte namhafter Hersteller, präzise Anpassungen durch modernste Messtechnik.</p>
        <div class="chips"><a class="chip" href="/hoerakustik/hoergeraete/">Hörgeräte {icon('arrow')}</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--line" aria-labelledby="labor">
  <div class="container lab">
    <div>
      <h2 class="h-lg rv" id="labor" style="--d:.06s;margin:20px 0 28px">Hauseigenes <em>Labor</em> &amp; <em>Werkstatt</em></h2>
      <div class="cards-2" style="grid-template-columns:1fr">
        <article class="card spot rv" style="--d:.1s">
          <div class="card__icon">{icon('ear')}</div>
          <h3 class="h-sm">Labor</h3>
          <p>In unserem hauseigenen Labor verbinden wir modernes Know-how mit echter Handwerkskunst.</p>
          <p>Gehörschutz, Schutz-Otoplastiken und Hörgeräte-Otoplastiken fertigen wir direkt bei uns – maßgeschneidert, präzise und in höchster Qualität. So entstehen individuelle Lösungen, die optimal sitzen, schützen und langfristig Schäden vorbeugen.</p>
        </article>
        <article class="card spot rv" style="--d:.16s">
          <div class="card__icon">{icon('tool')}</div>
          <h3 class="h-sm">Werkstatt</h3>
          <p>In unserer hauseigenen Werkstatt verbinden wir präzises Handwerk mit langjähriger Erfahrung.</p>
          <p>Brillen fertigen wir individuell nach Maß, passen sie exakt an und kümmern uns mit größter Sorgfalt um Reparaturen, Lötungen und Kunststoffbearbeitungen. Auch bestehende Gläser können wir fachgerecht in neue Fassungen einsetzen – für nachhaltige und passgenaue Lösungen, die Komfort und Qualität vereinen.</p>
        </article>
      </div>
    </div>
    <div class="lab__rings rv" style="--d:.1s" aria-label="Eindrücke aus Labor und Werkstatt">
      <div class="lab__center">{img('fasN55il', 'Gerät im hauseigenen Labor')}</div>
      <ul class="lab__orbit">{orbit_html}</ul>
    </div>
  </div>
</section>

<section class="section--tight section--line" aria-label="Hörgeräte-Marken">
  <div class="container"><p class="kicker rv" style="text-align:center;margin-bottom:34px;color:var(--dim)">Markenunabhängige Beratung – Hörsysteme namhafter Hersteller</p></div>
  {brands_marquee()}
</section>

{reviews_html()}
{locations_html()}
{default_cta()}
'''
    return page("/", "Optiker & Hörakustiker in Innsbruck | Optik Gaertner",
                "Optik Gaertner ist seit vielen Jahren Ihr Optiker & Hörakustiker in Innsbruck. Nehmen Sie Kontakt mit uns auf - wir helfen Ihnen gerne weiter.",
                body)


# ======================================================================
AWARDS = [
    ("Ing. Sophie Grimm-Gaertner B.Sc", [], [("hhTSstRF", "Sophie Grimm-Gaertner"), ("BoNkEomO", "Urkunde"), ("obDBP1uZ", "Urkunde Gesundheitsberufe"), ("2MCcN4Wa", "Bachelor-Urkunde")], ""),
    ("Zertifizierung zur Sportoptometristin (FH)", ["Sophie Grimm-Gaertner ist jetzt auch Sportoptometristin (FH). Nach der Zertifizierung zur klinischen Optometristin hat Sophie Grimm-Gaertner nun auch den weiterbildenden Zertifikatskurs zur Sportoptometristin an der Ernst-Abbe-Hochschule Jena erfolgreich abgeschlossen."], [("533d8Bir", "Zertifikat Sportoptometristin")], ""),
    ("Zertifizierung zur klinischen Optometristin (FH)", ["Sophie Grimm-Gaertner ist ab sofort klinische Optometristin (FH). Anfang des Jahres hat sie den weiterbildenden Kurs im Fachbereich SciTec an der Ernst-Abbe-Hochschule in Jena erfolgreich abgeschlossen."], [("GR6FnZNt", "Zertifizierung zur klinischen Optometristin (FH)")], ""),
    ("Auszeichnung mit der goldenen Ehrennadel", ["Im Dezember 2023 wurde KommR MMSt Joseph Gaertner von der Bundesinnung der Gesundheitsberufe die höchste Anerkennung für seine herausragenden Beiträge zur Aus- und Weiterbildung im Bereich der Hörakustik verliehen. Die aktuellen Ausbildungsrichtlinien für Hörakustiker in Österreich sind maßgeblich von den wegweisenden Leistungen geprägt, die Joseph Gaertner zu seiner Zeit erbracht hat."], [("6fmAG7SC", "Auszeichnung"), ("vHyfCRTT", "Goldene Ehrennadel"), ("FHEQhXv6", "Joseph Gaertner mit Urkunde")], ""),
    ("34-Jähriges Jubiläum als Partnerbetrieb bei OPTICON", ["Optik Gaertner wurde für seine herausragenden Leistungen und langjährige Partnerschaft während der jährlichen Tagung am 3. Juni 2023 im Schloss Mondsee geehrt. Die OPTICON Handels GmbH würdigte damit die bedeutende Zusammenarbeit und den wertvollen Beitrag von Optik Gaertner als langjährigen Partnerbetrieb. Übergeben wurden eine Urkunde sowie ein Jubiläumsgeschenk."], [("qfwVOsik", "Urkunde OPTICON")], ""),
    ("Ehrenmitgliedschaft im Verband der Hörakustiker Österreichs (VHÖ)", ["Österreich: Der ehemalige Landesinnungsmeister der Tiroler Augenoptiker, Kommerzialrat Joseph Gaertner, ist jetzt Ehrenmitglied im Verband der Hörakustiker Österreichs (VHÖ). Überreicht wurde die Urkunde von VHÖ-Präsident Thomas Aigner am Vorabend des Frühjahrsseminars des Verbands in Salzburg. Mit der Ehrenmitgliedschaft würdigt der Verband unter anderem die Verdienste Gaertners um die Lehrlings- und Meisterausbildung der Hörakustiker in Österreich in den 1990er-Jahren sowie um die Ausbildung im zweiten Bildungsweg am Wirtschaftsförderungsinstitut Innsbruck der Wirtschaftskammer Tirol Anfang der 2000er-Jahre. Der Unternehmer gilt zudem als einer der wesentlichen Unterstützer für eine Akademisierung der Augenoptik und wurde bereits mit der großen Silbernen Ehrenmedaille der Tiroler Wirtschaftskammer ausgezeichnet."], [("gQHrjYej", "Urkunde Ehrenmitgliedschaft VHÖ")], "Quelle: Fachzeitschrift Hörakustik 05/2023 Median-Verlag von Killisch-Horn GmbH"),
    ("Verband der Hörakustiker Österreichs - Frühjahrstagung 2023", ["Übergabe der Urkunde zur Ehrenmitgliedschaft im VHÖ-Verband von Herrn VHÖ-Präsident Thomas Aigner an Herrn KR Joseph Gaertner."], [("EjnHhBnZ", "Übergabe der Urkunde zur Ehrenmitgliedschaft")], ""),
    ("„Kämpfer“ für meisterliche Ausbildung mit Großer Silberner Ehrenmedaille ausgezeichnet", [
        "Für seine Verdienste, um die Berufsausbildung auf höchstem Niveau wurde Kommerzialrat Joseph Gaertner im Rahmen der „Meistergala“ eine seltene Ehre zuteil. Als erfolgreichem Unternehmer ist die Ausbildung des Berufsnachwuchses seit vielen Jahren ein großes Anliegen von Joseph Gaertner.",
        "Dabei hat er nicht nur selbst zahlreiche Lehrlinge als Augenoptiker und Hörgeräteakustiker ausgebildet, sondern auch innovative Akzente im Ausbildungssystem gesetzt. Unter anderem hat er die Etablierung des Hörakustikers als eigenen Beruf - samt Prüfungsordnung und Berufsbild - maßgeblich geprägt und mit großem persönlichem Einsatze eine einzigartige Ausbildungsstätte im WIFI Innsbruck schaffen können.",
        "Seinem Engagement ist es außerdem zu verdanken, dass die „Europäische Akademie für Hörakustik, Audio-Kommunikation und auditive Informatik (AHAKI)“ von den relevanten Bildungsträgern in Österreich, Schweiz und Deutschland gegründet wurde. Damit war er den heutigen Bestrebungen, international unterschiedliche Qualifikations- und Bildungswege zu harmonisieren, weit voraus. Gaertner ist zudem einer der Motoren für eine Akademisierung der Augenoptiker. Nach der Umsetzung eines Studiengangs für Augenoptik an der UMIT soll bald ein FH Bachelorstudiengang am AZW folgen.",
        "„Der Einsatz von Joseph Gaertner war und ist herausragend. Deshalb freue ich mich, ihm heute eine der höchsten Auszeichnungen, die die Wirtschaftskammer zu vergeben hat - die Große Silberne Ehrenmedaille -, überreichen zu dürfen“, meinte WK-Präsident Christoph Walser in seiner Laudatio für den Geehrten."],
     [("93pIUh1j", "Kommerzialrat Joseph Gaertner (Mitte) mit WIFI-Institutsleiter Paul Vyskovsky und Johannes Huber")],
     "Kommerzialrat Joseph Gaertner (Mitte) wurde mit der „Großen Silbernen Ehrenmedaille“ der Tiroler Wirtschaftskammer ausgezeichnet - dazu gratulierten als langjährige Wegbegleiter unter anderem WIFI-Institutsleiter Paul Vyskovsky (l.) und der Leiter der WK-Bildungsabteilung Johannes Huber (r.)."),
    ("Neue Meister und Ehrungen für einen Ausbildungs-Pionier", [
        "Ausgezeichnet. Im Rahmen des Galaabends der Meister wurde Joseph Gaertner für seine Verdienste um die Aus- und Weiterbildung die Große Silberne Ehrenmedaille der WK Tirol verliehen.",
        "Ein gerechter Lohn für jahrelanges Lernen wurde kürzlich rund 170 Jungmeisterinnen und Jungmeistern aus 28 Berufsgruppen zuteil. Beim „Galaabend der Meister“ im Congress Innsbruck konnten sie in feierlichem Rahmen ihre Meisterbriefe entgegennehmen. Dabei haben Wirtschaftslandesrätin Patrizia Zoller-Frischauf, Wirtschaftskammerpräsident Christoph Walser, Spartenobmann Franz Jirka sowie die jeweiligen Innungsmeister die Urkunden an die Jungmeisterinnen und Jungmeister überreicht. Und auch zahlreiche Bürgermeister waren mit dabei, um den Top-Handwerkern aus ihren Gemeinden zu gratulieren.",
        "Neben der Verleihung der Meisterbriefe an die Jungmeisterinnen und Jungmeister, gab es ein einen weiteren Höhepunkt im Rahmen der Meistergala: Kommerzialrat Joseph Gaertner wurde aufgrund seiner besonderen Verdienste und die berufliche Aus- und Weiterbildung - im Besonderen in der Hörgeräteakustik und der Augenoptik - die Große Silberne Ehrenmedaille der WK Tirol verliehen. „Der Einsatz von Joseph Gaertner war und ist herausragend. Deshalb freue ich mich, ihm heute eine der höchsten Auszeichnungen, die die Wirtschaftskammer zu vergeben hat, überreichen zu dürfen“, meinte WK-Präsident Christoph Walser in seiner Laudatio für den Geehrten."],
     [("riMbQIuy", "Verleihung der Großen Silbernen Ehrenmedaille"), ("BWCfZJvq", "Galaabend der Meister")], ""),
    ("Berufstitel - KOMMERZIALRAT", ["Verliehen vom Bundespräsidenten der Republik Österreich als Innungsmeister der Landesinnung Tirol der Gesundheitsberufe und Obmann-Stellvertreter der Sparte Gewerbe und Handwerk der Wirtschaftskammer Tirol."], [("OPkn45uu", "Kommerzialrat")], ""),
    ("SILBERNE EHRENNADEL der EUHA", ["Europäische Union der Hörakustiker e.V. anlässlich der 25-jährigen Mitgliedschaft"], [("rBy4Q3OX", "Ehrennadel EUHA")], ""),
    ("Verleihung der Ehrennadel in Gold Sept. 1998", [], [("j3rlWVrx", "Ehrennadel in Gold")], ""),
    ("Verleihung des Titels Europa-Hörakustiker durch die AEA Europe", ["Association of the European Hearing Aid Acousticians"], [("O3v28hRv", "Diplom Europa-Hörakustiker")], ""),
]


def about():
    tl = []
    for i, (h, paras, imgs, cap) in enumerate(AWARDS):
        ps = "".join(f"<p>{escape(p)}</p>" for p in paras)
        if cap:
            ps += f'<p class="src">{escape(cap)}</p>'
        ims = "".join(
            f'<button type="button" data-lb="awards" data-full="{src(p)}" aria-label="Bild vergrößern: {escape(a)}">{img(p, a)}</button>'
            for p, a in imgs)
        cls = "tl__card" + ("" if imgs else " no-img")
        tl.append(f'''<article class="tl rv"><div class="card spot {cls}"><div><h3>{escape(h)}</h3>{ps}</div>{f'<div class="tl__imgs">{ims}</div>' if imgs else ''}</div></article>''')

    body = f'''
{page_hero_about()}
<section class="section">
  <div class="container">
    <div class="split split--top">
      <div class="rv">
        <h2 class="h-lg" style="margin:20px 0 28px">Optiker und Hörakustiker mit <em>Tradition</em> und Innovation</h2>
        <div class="prose"><p>Optik Gaertner verbindet die persönliche Note eines Familienbetriebes mit modernster Technologie. In unseren drei Fachgeschäften in Innsbruck finden Sie spezialisierte Schwerpunkte, die optimal auf Ihre Bedürfnisse zugeschnitten sind. Unsere geprüften Hörakustiker und Augenoptiker nehmen sich Zeit für eine markenunabhängige Beratung, bei der immer Ihre Wünsche im Mittelpunkt stehen. Vom handgefertigten Gehörschutz aus unserem eigenen Otoplastik-Labor bis hin zu individuell angepassten Brillen erhalten Sie bei uns alles aus einer Hand – immer geprüft, immer zuverlässig. Dabei gehen wir weit über die reine Kassenleistung hinaus, um Ihnen ein Höchstmaß an Qualität und Komfort zu bieten.</p></div>
      </div>
      <figure class="rv sticky" style="--d:.1s;margin:0">
        <div class="frame frame--wide">{img('84dzbumg', 'Johannes Grimm, Sophie Grimm-Gaertner und Joseph Gaertner')}</div>
        <figcaption class="dim" style="margin-top:14px;font-size:.9rem">Johannes Grimm, Sophie Grimm-Gaertner, Joseph Gaertner</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section section--line">
  <div class="container">
    <div class="split split--rev">
      <div class="rv">
        <h2 class="h-lg" style="margin:20px 0 28px">Persönliche Betreuung für Auge und Ohr in <em>Innsbruck</em></h2>
        <div class="prose"><p>Hören und Sehen bedeutet Lebensqualität – und genau diese machen wir für Sie erlebbar. Unser Meisterhörakustiker Johannes Grimm bringt neben seiner fundierten Ausbildung auch umfassende technische Erfahrung mit. Sein Anspruch: Jeder verdient es, die Welt mit allen Sinnen genießen zu können. Deshalb begleiten wir Sie von der ersten Beratung bis hin zum Service, der ein Hörgeräteleben lang anhält. Bei uns verlassen nur geprüfte Hörgeräte und Otoplastiken das Haus – sei es für Hörgeräte, Schlaf- oder Spritzwasserschutz. Mit Engagement und Leidenschaft sorgen wir dafür, dass Technik nicht verstaubt wirkt, sondern Sie im Alltag aktiv unterstützt. Vertrauen Sie auf Optik Gaertner – Ihren starken Partner für Sehen und Hören in Innsbruck.</p></div>
      </div>
      <div class="split__media rv" style="--d:.1s"><div class="frame frame--wide">{img('Nt3znHfI', 'Verkaufsraum von Gaertner Optik in Innsbruck')}</div></div>
    </div>
  </div>
</section>

<section class="section section--line" aria-labelledby="auszeichnungen">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><h2 class="h-lg" id="auszeichnungen">Ausbildung, Verantwortung, <em>Anerkennung</em>.</h2></div>
      <div class="certs rv" style="--d:.1s">{certs_html()}</div>
    </div>
    <div class="timeline">{"".join(tl)}</div>
  </div>
</section>
{locations_html()}
{default_cta()}
'''
    crumbs = [("Home", "/"), ("Über uns", "/ueber-uns/")]
    return page("/ueber-uns/", "Über uns - Optiker & Hörakustiker in Innsbruck | Optik Gaertner",
                "Hier erfahren Sie mehr über Optik Gaertner - Ihrem Optiker & Hörakustiker in Innsbruck. Bei Fragen nehmen wir uns gerne Zeit für Sie.",
                body, og="84dzbumg", crumbs=crumbs)


def page_hero_about():
    from lib import page_hero
    return page_hero(
        "Über uns", "Über uns – Ihr Optiker und Hörakustiker in <em>Innsbruck</em>",
        "<p>Seit mehr als 45 Jahren steht Optik Gaertner in Innsbruck für Qualität, Vertrauen und persönliche Beratung rund um gutes Sehen und Hören. Als erfahrener Optiker und Hörakustiker begleiten wir Sie mit individueller Betreuung, modernster Technik und dem Anspruch, Ihr Leben durch perfektes Hören und Sehen spürbar zu bereichern. Unsere Kunden schätzen nicht nur die kompetente Beratung, sondern auch die familiäre Atmosphäre, die unser Unternehmen seit Jahrzehnten prägt. Verantwortung, Präzision und Zuverlässigkeit sind die Werte, die uns antreiben – und die wir in jedem einzelnen Gespräch und jeder Anpassung spürbar machen.</p>",
        image="HSLRCqqP", alt="Augenpaar in Schwarz-Weiß",
        crumbs=[("Home", "/"), ("Über uns", "/ueber-uns/")])


def build():
    write("/", home())
    write("/ueber-uns/", about())
