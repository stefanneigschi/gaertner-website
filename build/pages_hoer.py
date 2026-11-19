"""Hörakustik: Übersicht, Unterseiten und Gehörschutz."""
from lib import (img, src, icon, btn, page, write, page_hero, locations_html, default_cta, gallery, split,
                 cards, downloads, brands_marquee, HOER_SUB, escape)
from pages_optik import sub_page, P, related

HOERTEST = "https://digitalhearingtest.com/de-AT/Gaertner/1"
HOER_CRUMB = [("Home", "/"), ("Hörakustik", "/hoerakustik/")]
HOER_BTNS = [btn("Termin vereinbaren", "/kontakt/#termin"), btn("Online-Hörtest", HOERTEST, "ghost", "ext")]
HOER_SIB = HOER_SUB + [("Gehörschutz", "/gehoerschutz/")]

STEPS = [
    ("Höranalyse und Anamnese", ["Erhebung der persönlichen Hörhistorie und medizinischen Vorgeschichte.", "Durchführung eines Hörtests (Audiometrie) zur Feststellung des Hörverlusts."]),
    ("Beratung und Zielsetzung", ["Besprechung der Hörtestergebnisse und Erklärung des Hörverlusts.", "Festlegen individueller Ziele und Erwartungen an das Hörgerät."]),
    ("Auswahl des Hörgeräts", ["Beratung über verschiedene Hörgerätemodelle und -technologien.", "Berücksichtigung von ästhetischen Präferenzen, Funktionalität und Budget."]),
    ("Anpassung des Hörgeräts", ["Individuelle Einstellung des Hörgeräts basierend auf der Audiogrammdaten.", "Anpassung an die persönliche Gehörumgebung mittels Feineinstellungen."]),
    ("Einweisung und Erstnutzung", ["Erklärung der Bedienung, Pflege und Wartung des Hörgeräts.", "Erlernen des korrekten Einsetzens und Entfernens des Geräts."]),
    ("Probephase und Nachjustierung", ["Testen des Hörgeräts in alltäglichen Situationen.", "Durchführung von Feinanpassungen, basierend auf Feedback und Erfahrungen."]),
    ("Abschlussgespräch und Langzeitbetreuung", ["Besprechung der endgültigen Einstellungen und Zufriedenheit.", "Vereinbarung regelmäßiger Kontrolltermine zur Wartung und weiteren Anpassung."]),
    ("Kontinuierliche Betreuung", ["Reinigung und Pflege des Geräts bei Bedarf.", "Gelegentliche Software-Updates oder technische Anpassungen."]),
]


def hoerakustik():
    steps = "".join(
        f'<article class="step spot rv" style="--d:{(i % 4) * .07:.2f}s"><span class="step__n">{i + 1:02d}</span><h3>{escape(h)}</h3><ul>{"".join(f"<li>{escape(x)}</li>" for x in li)}</ul></article>'
        for i, (h, li) in enumerate(STEPS))
    svc = [
        ("/hoerakustik/hoergeraete/", "dHGrTzTI", "Hörgeräte", "Hörgeräte"),
        ("/hoerakustik/tinnitus/", "RdRQ3BVL", "Tinnitus", "Tinnitus"),
        ("/hoerakustik/zubehoer-und-reinigung/", "68nS3pT5", "Zubehör & Reinigung", "Reinigung von Hörgeräten"),
    ]
    svc_html = "".join(f'''<a class="tile tile--shade span-4 spot rv" style="--d:{i * .08:.2f}s;min-height:380px" href="{h}">
  <div class="tile__bg">{img(p, a)}</div><span class="kicker">Leistung</span>
  <h3 class="h-md" style="display:flex;justify-content:space-between;align-items:end;gap:20px">{escape(t)}<span class="btn btn-ghost btn-sm" aria-hidden="true" style="width:42px;padding:0">{icon('arrow')}</span></h3></a>'''
                       for i, (h, p, t, a) in enumerate(svc))

    body = page_hero(
        "Hörakustik", "Ihr verlässlicher Partner in Sachen <em>Hörakustik</em> in Innsbruck",
        P("Das Hören ist unser wichtigstes Sinnesorgan, auf das wir nicht verzichten können. Umso wichtiger ist es, Anzeichen von Hörschwäche zu erkennen und Maßnahmen dagegen zu ergreifen.",
          "Mit zunehmendem Alter nimmt der Gehörsinn bei vielen Menschen ab, aber auch junge Menschen können an einer Hörschwäche leiden. Der Hörsinn spielt aber bei der Bewältigung des Alltags und insbesondere im Austausch mit anderen Menschen eine zentrale Rolle – eine nicht behandelte Hörschwäche kann mit sich bringen, dass Betroffene sich sozial isoliert fühlen. Als Ihr Hörakustiker in Innsbruck stehen wir Ihnen mit maßgeschneiderten Hörlösungen zur Verfügung."),
        image="bHR2vwHT", alt="Leuchtende Ohr-Skulptur aus Moos", crumbs=HOER_CRUMB, buttons=HOER_BTNS) + f'''
<section class="section">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><span class="eyebrow">Was wir für Sie tun können</span><h2 class="h-lg">Was wir für Sie im Bereich <em>Hörakustik</em> tun können</h2></div>
    </div>
    {cards([
        ("Top-Service bei Ihrem Hörakustiker in Innsbruck", P("Bei uns genießen Sie einen hervorragenden Service rund um Ihr Hörgerät. Wir bieten Ihnen individuelle Anpassung, Schnellreparaturen innerhalb von 10 Minuten sowie direkte Abrechnung mit Ihrer Krankenkasse! Als freier Akustiker sind wir nicht an eine bestimmte Marke gebunden und können Ihnen Beratung und Wartung für Geräte aller Hersteller bieten. Sie haben einen Akustiker als Vertrauensperson, der stets für Sie da ist und Ihnen individuelle Beratung abgestimmt auf Ihren persönlichen Bedarf bietet!")),
        ("Zusammenhang von Hörverlust und Demenz", P("Hörverlust und Demenz stehen in einem engen Zusammenhang, wie zahlreiche Studien zeigen. Menschen mit unbehandeltem Hörverlust haben ein höheres Risiko, eine Demenz zu entwickeln. Dies könnte darauf zurückzuführen sein, dass das Gehirn bei Hörverlust stärker belastet wird, um unklare Signale zu verarbeiten. Diese dauerhafte Überforderung kann zu einem Abbau kognitiver Fähigkeiten führen. Zusätzlich begünstigt ein Hörverlust soziale Isolation, da Betroffene oft Gespräche meiden, was wiederum das Risiko für Demenz erhöht.", "Eine frühzeitige Diagnose und Versorgung mit Hörgeräten kann diesem Prozess entgegenwirken. Durch die Wiederherstellung des Hörvermögens bleiben Betroffene aktiv am sozialen Leben beteiligt, und die geistige Gesundheit wird gefördert. Daher ist die Behandlung von Hörverlust nicht nur für das Hören, sondern auch für die allgemeine Gesundheit von großer Bedeutung.")),
        ("Modernste Technologie für ein optimales Hörerlebnis", P("Hörgeräte werden immer kleiner, dezenter und technologisch ausgereifter. Sie erleichtern Menschen mit eingeschränktem Hörsinn den Alltag wesentlich und können zum Teil sogar mit Fernseher, Radio, Telefon und anderen bluetoothfähigen Geräten verbunden werden. Außerdem passen sich moderne Geräte automatisch auf veränderte Hörumgebungen an und sorgen so für bestmögliches Hören in jeder Situation!")),
        ("Lassen Sie sich von unserem Team beraten!", P("Als Ihr Hörakustiker stehen wir Ihnen mit jahrelanger Erfahrung und einer breiten Palette an hochwertigen Hörgeräten zur Verfügung. Besuchen Sie unser Geschäft und lassen Sie sich von uns beraten – wir sind gerne für Sie da!") + f'<p style="margin-top:22px">{btn("Jetzt Termin vereinbaren", "/kontakt/#termin")}</p>'),
    ], cols=2, icons=["tool", "heart", "spark", "chat"])}
  </div>
</section>

<section class="section section--line">
  <div class="container">
    <div class="sec-head"><div class="rv"><span class="eyebrow">Leistungen</span><h2 class="h-lg">Unsere Leistungen für <em>Hörakustik</em></h2></div></div>
    <div class="bento">{svc_html}</div>
  </div>
</section>

<section class="section section--line" aria-labelledby="ablauf">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><span class="eyebrow">In acht Schritten</span><h2 class="h-lg" id="ablauf">Ablauf <em>Hörgeräteanpassung</em></h2></div>
      <p class="lead rv" style="--d:.1s">Von der ersten Höranalyse bis zur kontinuierlichen Betreuung – so begleiten wir Sie.</p>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="section section--line">
  <div class="container">
    {split(f"""<span class="eyebrow">Perzentilanalyse</span>
<h2 class="h-lg" style="margin:20px 0 26px">Individuelle Anpassung mittels <em>Perzentilanalyse</em></h2>
<div class="prose"><p><strong>Die Perzentilanalyse basierend auf NAL ermöglicht eine gezielte und damit besonders präzise Einstellung von Hörsystemen.</strong></p>
<p>Dadurch lässt sich das Sprachverstehen deutlich verbessern. Verschiedene Höreigenschaften des Hörsystems werden dabei genau analysiert, sodass wir bei Gaertner Auditiv gezielt erkennen, welche Töne und Sprachanteile für Sie hörbar sind und optimal unterstützt werden können. Das Ergebnis ist ein individuell angepasstes Hörgerät, das Ihr vorhandenes Hörvermögen bestmöglich nutzt und Ihnen wieder mehr Hörqualität im Alltag schenkt.</p></div>""",
           f'<div class="frame frame--square">{img("eNo8zseQ", "Hörtest")}</div>')}
  </div>
</section>

<section class="section section--line" id="hoertest" aria-labelledby="ht">
  <div class="container">
    <div class="split split--top">
      <div class="rv">
        <span class="eyebrow">Hörtest</span>
        <h2 class="h-lg" id="ht" style="margin:20px 0 26px">Hörtest bei GAERTNER – Hören <em>neu</em> erleben</h2>
        <div class="prose"><p>Gutes Hören bedeutet Lebensqualität. Ein professioneller Hörtest zeigt nicht nur, wie gut Sie hören, sondern kann auch frühzeitig Hinweise auf Veränderungen des Hörvermögens geben. Viele Menschen bemerken schleichende Hörverluste erst spät – etwa wenn Gespräche anstrengender werden, Stimmen undeutlich wirken oder Hintergrundgeräusche zunehmend stören.</p></div>
        <div class="btn-row" style="margin:30px 0 14px">{btn("Online-Hörtest starten", HOERTEST, "primary", "ext")}</div>
        <p class="dim" style="font-size:.88rem">Der Online-Hörtest ersetzt keinen Besuch bei einem Hörakustiker und stellt keine medizinische Diagnose dar.</p>
      </div>
      <div class="card spot rv" style="--d:.1s">
        <h3 class="h-sm" style="margin-bottom:22px">Warum ein persönlicher Hörtest wichtig ist</h3>
        <ul class="ticks">
          <li>Frühzeitiges Erkennen von Hörverlust</li>
          <li>Mehr Lebensqualität und besseres Sprachverstehen</li>
          <li>Entlastung für Gehirn und Konzentration</li>
          <li>Moderne Hörlösungen heute nahezu unsichtbar und intelligent</li>
          <li>Individuelle Beratung statt Standardlösungen</li>
        </ul>
        <hr style="border:0;border-top:1px solid var(--line);margin:28px 0">
        <h3 class="h-sm" style="margin-bottom:14px">Unser Anspruch bei GAERTNER</h3>
        <p>Wir verbinden modernste Hörakustik mit persönlicher Betreuung und Premium-Service. Unser Ziel ist nicht nur besseres Hören – sondern ein natürliches, entspanntes und vernetztes Hörerlebnis für Alltag, Beruf und Freizeit.</p>
        <p>Vereinbaren Sie jetzt Ihren persönlichen Hörtest bei GAERTNER und entdecken Sie, wie modern Hören heute sein kann.</p>
        <p style="margin-top:22px">{btn("Jetzt Termin vereinbaren", "/kontakt/#termin")}</p>
      </div>
    </div>
  </div>
</section>

<section class="section--tight section--line">
  <div class="container">
    <p class="kicker rv" style="margin-bottom:18px">Broschüren zum Download</p>
    {downloads([("Gaertner Akustik-Wegweiser", "gaertner-akustik-wegweiser.pdf", "Opticon"), ("Oticon Technologien im Überblick", "oticon-technologien-ueberblick.pdf", "Oticon")])}
  </div>
</section>

<section class="section--tight section--line" aria-label="Hörgeräte-Marken">
  <div class="container"><p class="kicker rv" style="text-align:center;margin-bottom:34px;color:var(--dim)">Hörsysteme aller namhaften Hersteller</p></div>
  {brands_marquee()}
</section>
{locations_html()}
{default_cta()}'''
    return page("/hoerakustik/", "Hörakustik in Innsbruck | Optik Gaertner",
                "Ob Hörgeräte, Hilfe bei Tinnitus oder Zubehör & Reinigung für Hörgeräte - Optik Gaertner ist Ihr Partner für Hörakustik in Innsbruck.",
                body, og="bHR2vwHT", crumbs=HOER_CRUMB)


def feature_rows(rows):
    out = []
    for i, (pid, alt, h, body) in enumerate(rows):
        text = f'<h2 class="h-md" style="margin-bottom:18px">{h}</h2><div class="prose">{body}</div>'
        media = f'<div class="frame frame--square">{img(pid, alt)}</div>'
        out.append(f'<div style="margin-top:{0 if i == 0 else "clamp(60px,8vw,110px)"}">{split(text, media, rev=i % 2 == 1)}</div>')
    return "".join(out)


def hoergeraete():
    rows = feature_rows([
        ("DHSmTYAa", "Im-Ohr-Hörgeräte", "Im-Ohr-Geräte <em>(IO-Geräte)</em>", P("IO-Hörgeräte werden individuell an Ihr Ohr angepasst und eignen sich bei leichtem bis mittlerem Hörverlust. Je nach Modell sitzen sie entweder bequem in der Ohrmuschel oder direkt im Gehörgang und sind dadurch kaum sichtbar. Ihr Hörakustiker hilft Ihnen gerne dabei, das passende Hörgerät für Ihre Bedürfnisse zu finden.")),
        ("9WuOHd5l", "Hinter-dem-Ohr-Hörgerät", "Hinter-dem-Ohr-Geräte <em>(HDO-Geräte)</em>", P("HDO-Geräte werden hinter dem Ohr getragen und sind mittels Schlauch mit dem Ohrstück verbunden. Ihr Hörakustiker nimmt eine individuelle Anpassung des Gerätes an Ihre Ohren vor. Diese aufgrund technologischer Weiterentwicklung immer kleiner werdenden Geräte sind überaus leistungsstark und können auch bei starker Hörbeeinträchtigung erfolgreich eingesetzt werden! Bei der RIC-Methode (Receiver in the Canal) sitzt der Lautsprecher direkt im Gehörgang, während das eigentliche Hörgerät unauffällig hinter dem Ohr getragen wird – für natürlichen Klang und hohen Tragekomfort.")),
        ("Tk8fkzcK", "Hörgeräte mit Akku", "Hörgeräte mit <em>Akku</em>", P("Vergessen Sie den Batteriewechsel! Mit modernen Hörgeräten mit Akku genießen Sie höchste Klangqualität und volle Leistung – den ganzen Tag. Einfach über Nacht laden und morgens einsatzbereit starten. Ideal für Menschen, die Wert auf Komfort, Nachhaltigkeit und Technik legen.")),
        ("HuxgNGgf", "Hörgeräte mit KI", "Hörgeräte mit <em>KI</em> (künstlicher Intelligenz)", P("Künstliche Intelligenz verändert das Hören: Hörgeräte mit KI passen sich automatisch an Ihre Umgebung an, filtern Störgeräusche und optimieren Sprache – ganz ohne manuelles Nachjustieren. Für ein natürliches Hörerlebnis, das mitdenkt.")),
    ])
    extra = f'''
<section class="section section--line"><div class="container">{rows}</div></section>
<section class="section section--line"><div class="container">
  {gallery("zeal", [("VNrnN1xY", "Menschen tanzen – Hörgeräte im Alltag"), ("bAR3VIQz", "Hörgeräte mit Ladeschale in der Hand"), ("1Z00JMYe", "Hörgerät in der Hand"), ("p3ecqC2i", "Nahezu unsichtbares Hörgerät"), ("6D46XEB2", "Hörgerät auf der Fingerspitze"), ("m6r73A5s", "Hörgerät mit Smartwatch und Kaffee")], "rail")}
  <div style="margin-top:40px"><p class="kicker rv" style="margin-bottom:18px">Broschüren zum Download</p>
  {downloads([("Hörgeräte-Tipps von Gaertner", "gaertner-hoergeraete-tipps.pdf", "Folder"), ("Oticon Real – souverän durch die reale Welt", "oticon-real-broschuere.pdf", "Oticon")])}</div>
</div></section>'''
    return sub_page(dict(
        path="/hoerakustik/hoergeraete/", crumbs=HOER_CRUMB + [("Hörgeräte", "/hoerakustik/hoergeraete/")],
        title="Hörgeräte in Innsbruck | Optik Gaertner",
        desc="Im-Ohr-Geräte und Hinter-dem-Ohr-Geräte - hier erfahren Sie mehr über Hörgeräte von Optik Gaertner in Innsbruck.",
        eyebrow="Hörgeräte", h1="Ihr Spezialist für <em>Hörgeräte</em> in Innsbruck",
        intro=P("Unser Hörorgan ist unser wichtigstes Sinnesorgan, daher ist es besonders wichtig, Anzeichen von Hörverlust schon frühzeitig zu erkennen. Denn nur so kann man rechtzeitig Gegenmaßnahmen ergreifen, damit Ihnen das Gehör noch lange erhalten bleibt.",
                "Jeder Hörverlust ist individuell und kann unterschiedliche Ursachen haben. Daher muss ein Hörsystem stets perfekt auf den Träger oder die Trägerin abgestimmt werden! Als Ihr Hörakustiker in Innsbruck finden wir gemeinsam mit Ihnen heraus, welches Gerät für Sie am besten passt."),
        hero="R6g1rVkC", hero_alt="Hörgeräte", buttons=HOER_BTNS,
        img="0MODTYxw", img_alt="Hörgerät",
        h2_eyebrow="So gewöhnen Sie sich an Ihr Hörgerät",
        h2="Endlich neue <em>Lebensqualität!</em>",
        h2_text=P("<strong>So gewöhnen Sie sich an Ihr Hörgerät</strong>",
                  "Um die Eingewöhnung zu fördern, ist es wichtig, dass das Hörgerät viel getragen wird. Sie können bei uns das gewünschte Hörgerät kostenlos probetragen. Achten Sie im Alltag darauf, wo und in welcher Form Probleme und Wünsche auftauchen. Beim nächsten gemeinsamen Termin justieren wir nach, um Ihren individuellen Trage- und Hörkomfort zu optimieren. Die Einstellung des Hörsystems ist wesentlich und sollte nicht vernachlässigt werden. Wir nehmen uns Zeit für Sie und sind erst zufrieden, wenn Sie es sind.",
                  "Wir zeigen Ihnen gerne Übungen, mit denen Sie Geräusche in der Umgebung wieder besser wahrnehmen können!"),
        extra=extra,
        siblings=HOER_SIB, siblings_label="Weitere Themen in der Hörakustik",
    ))


def app():
    return sub_page(dict(
        path="/hoerakustik/hoergeraete-mit-app-verbinden/", crumbs=HOER_CRUMB + [("Hörgeräte mit App verbinden", "/hoerakustik/hoergeraete-mit-app-verbinden/")],
        title="Hörgeräte mit App verbinden – einfach erklärt",
        desc="Erfahren Sie hier, wie Sie Ihr Hörgerät ganz einfach per App steuern können. Hörakustik & Optik Gaertner in Innsbruck.",
        eyebrow="Hörgeräte mit App", h1="Hörgeräte einfach mit dem <em>Smartphone</em> verbinden",
        intro=P("Moderne Hörgeräte lassen sich heute problemlos mit dem Smartphone koppeln. Die Verbindung erfolgt in der Regel kabellos über Bluetooth und ist mit wenigen Schritten eingerichtet. Einmal gekoppelt, erkennen sich beide Geräte automatisch wieder und verbinden sich künftig selbstständig. So wird Ihr Hörgerät zu einem smarten Begleiter im Alltag."),
        hero="GGz5GwAB", hero_alt="Hörgerät und Smartphone", buttons=HOER_BTNS,
        img="BgnrLK5D", img_alt="Steuerung des Hörgeräts mit App",
        h2="Steuerung per App – mehr <em>Kontrolle</em> im Alltag",
        h2_text=P("Mit der passenden App des Herstellers können Sie Ihre Hörgeräte bequem über das Smartphone steuern. Lautstärke, Programme oder individuelle Einstellungen lassen sich schnell und diskret anpassen – ganz ohne zusätzliche Handgriffe am Gerät. Das sorgt für mehr Komfort und ermöglicht eine präzise Anpassung an jede Hörsituation."),
        cards=[("Direktes Streaming für klaren Klang", P("Ein großer Vorteil der Verbindung ist das direkte Audio-Streaming. Telefonate, Musik oder andere Medien werden ohne Umwege direkt in die Hörgeräte übertragen. Dadurch profitieren Sie von einer klaren Klangqualität und verstehen Sprache auch in schwierigen Situationen deutlich besser.")),
               ("Mehr Lebensqualität durch smarte Funktionen", P("Die Kombination aus Hörgerät und App eröffnet zahlreiche zusätzliche Möglichkeiten. Neben der einfachen Bedienung können Funktionen wie Fernanpassung, Gerätesuche oder individuelle Klangprofile genutzt werden. So wird Ihr Hörsystem noch flexibler und unterstützt Sie optimal in Ihrem täglichen Leben."))],
        icons=["wave", "smartphone"],
        siblings=HOER_SIB, siblings_label="Weitere Themen in der Hörakustik",
    ))


def tinnitus():
    quote = f'''<section class="section--tight"><div class="container"><figure class="quote rv" style="max-width:900px">
<blockquote>„Da Tinnitus oft mit Ablehnung, also negativen Emotionen, behaftet ist, kann versucht werden, den Tinnitus auch in positiven Situationen aktiv herbeizurufen (Natur, Meditation, Treffen mit Freunden), da es dadurch leichter zu einer Akzeptanz kommen kann.“</blockquote>
<figcaption>Was Johannes über den Tinnitus sagt – Johannes Grimm, Meisterhörakustiker</figcaption></figure></div></section>'''
    dl = f'''<section class="section--tight section--line"><div class="container"><p class="kicker rv" style="margin-bottom:18px">Ratgeber zum Download</p>{downloads([("Wissenswertes über Tinnitus", "oticon-tinnitus-ratgeber.pdf", "Oticon Ratgeber")])}</div></section>'''
    return sub_page(dict(
        path="/hoerakustik/tinnitus/", crumbs=HOER_CRUMB + [("Tinnitus", "/hoerakustik/tinnitus/")],
        title="Hilfe bei Tinnitus vom Hörakustiker in Innsbruck | Optik Gaertner",
        desc="Sie leiden unter Tinnitus? Hörakustiker Optik Gaertner in Innsbruck bietet Ihnen Hilfe bei Tinnitus.",
        eyebrow="Tinnitus", h1="Hilfe bei <em>Tinnitus</em> vom Hörakustiker in Innsbruck",
        intro=P("Ein vorübergehendes Auftreten von Ohrgeräuschen hat fast jeder Mensch schon einmal erlebt. Hält das Pfeifen, Brummen oder Zischen im Ohr aber länger an oder tritt immer wieder auf, so spricht man von Tinnitus. Diese Ohrgeräusche können für Betroffene – abhängig von der Ausprägung – oft sehr belastend sein und auch mit einer Minderung des Hörvermögens einhergehen."),
        hero="BjOcVIsR", hero_alt="Tinnitus", buttons=HOER_BTNS,
        img="SATOiHqS", img_alt="Mann mit Ohrgeräuschen",
        h2="Gezielte <em>Tinnitusbehandlung</em> bei Ihrem Hörakustiker",
        h2_text=P("Als Ihr Hörakustiker sind wir mit dem Beschwerdebild vertraut und stellen Ihnen gerne verschiedene Lösungen zur Behandlung Ihrer Symptomatik vor. Im Idealfall lassen Sie Ihren Tinnitus im Vorfeld beim HNO-Arzt abklären, sodass wir Ihnen eine maßgeschneiderte Lösung für Ihr Problem anbieten können."),
        extra_top=quote,
        cards=[("Ohrgeräusche mit Hörgeräten mildern", P("Insbesondere wenn der Tinnitus mit einem Hörverlust einhergeht, können mit einem Hörgerät sehr gute Erfolge erzielt werden. Hörgeräte mit einem sogenannten Tinnitus-Masker erzeugen ein weißes Rauschen, das nicht bewusst wahrgenommen wird, aber die Wahrnehmung der Ohrgeräusche vermindert. Viele Betroffene erleben dadurch subjektiv ein vollständiges Verschwinden ihres Tinnitus.")),
               ("Ihr Hörakustiker berät Sie gerne", P("Leiden Sie unter Tinnitus und fühlen Sie sich im Alltag dadurch beeinträchtigt? Reduzieren die Ohrgeräusche vielleicht sogar Ihr Hörvermögen? Ihr Hörakustiker steht Ihnen gerne mit einer umfassenden Erfahrung und Expertise auf diesem Gebiet zur Verfügung und berät Sie gerne."))],
        icons=["wave", "chat"],
        extra=dl,
        siblings=HOER_SIB, siblings_label="Weitere Themen in der Hörakustik",
    ))


def zubehoer():
    groups = [
        ("reinigung", "Reinigung", [("kncDv9Z5", "Reinigungstabs"), ("fhcySVlN", "Reinigungstücher 30 Stück"), ("kACwl2bn", "Reinigungstücher 100 Stück"), ("bjvrUGLn", "Reinigungstücher einzeln verpackt"), ("RVBWD3qn", "Reinigungsspray")]),
        ("tools", "Tools", [("H1JYkTZp", "Cerumenschlinge"), ("u7E7xfOq", "Cerumenstäbchen"), ("2OTnzz9i", "Cerumenbürste"), ("JStukOH6", "Reinigungsbecher"), ("c22SsJs9", "Tubereiniger"), ("1oyDKNjg", "Ventreiniger")]),
        ("trocknung", "Trocknung", [("F3pZQulp", "Trockenbox"), ("iBeWfo9W", "Trockenkapseln"), ("udzX8y8k", "Schallkanalpuster")]),
        ("pflege", "Pflege", [("4rKW9tA1", "Pflege-Creme")]),
    ]
    tabs = "".join(
        f'<button role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{"true" if i == 0 else "false"}">{t}</button>'
        for i, (k, t, _) in enumerate(groups))
    panels = "".join(
        f'<div class="products" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}>' +
        "".join(f'<button type="button" class="product" data-lb="p-{k}" data-full="{src(p)}" aria-label="{escape(a)}">{img(p, a)}</button>' for p, a in items) +
        "</div>" for i, (k, t, items) in enumerate(groups))

    extra = f'''
<section class="section section--line">
  <div class="container">
    {split(f"""<span class="eyebrow">OSKAR TV</span>
<h2 class="h-lg" style="margin:20px 0 22px">OSKAR TV</h2>
<p class="lead" style="margin-bottom:20px">Der Ton des Fernsehers genau da wo Sie ihn brauchen</p>
<div class="prose"><p>Dieser unkomplizierte kabellose Lautsprecher mit innovativer Technologie zur Stimmoptimierung lässt sich einfach an den Fernseher anschließen. So können Sie beispielsweise genau die Lautstärke wählen, die Sie möchten, ohne dabei andere Zuschauer im Raum zu beeinträchtigen. Da das Setup so unkompliziert und einfach ist, können Sie sofort loslegen.</p></div>""",
           f'<div class="frame frame--square">{img("oIv863tc", "Oskar TV Lautsprecher")}</div>', rev=True)}
  </div>
</section>
<section class="section section--line" aria-labelledby="reinigung">
  <div class="container">
    <div class="sec-head"><div class="rv"><span class="eyebrow">Pflege</span><h2 class="h-lg" id="reinigung">Reinigung von <em>Hörgeräten</em></h2></div></div>
    <div class="split split--top">
      <div class="rv">
        <article class="card spot" style="margin-bottom:18px">
          <div class="card__icon">{icon('tool')}</div>
          <h3 class="h-sm">Reinigung beim Spezialisten</h3>
          {P("Ihr Hörgerät ist ein präzises High-Tech-Gerät und benötigt regelmäßige Pflege, um maximale Leistung und Langlebigkeit zu gewährleisten. Besonders nach dem Sport oder bei hohen Temperaturen ist eine gründliche Reinigung essenziell.", "Mit professionellen Verfahren wie Ultraschallbädern, desinfizierenden Mitteln und Trocknungsgeräten entfernen wir Bakterien und Ablagerungen. Bringen Sie Ihr Hörgerät alle drei Monate zu uns – wir verfügen über die passenden Werkzeuge und Mittel.")}
        </article>
        <div class="frame frame--wide">{img("dHGrTzTI", "Hörgeräte-Reinigung")}</div>
      </div>
      <article class="card spot rv" style="--d:.1s">
        <div class="card__icon">{icon('drop')}</div>
        <h3 class="h-sm">Reinigung zu Hause</h3>
        <p>Neben der regelmäßigen professionellen Reinigung ist auch die tägliche Pflege Ihrer Hörgeräte zu Hause unerlässlich. Planen Sie etwas Zeit ein, um Hautpartikel und Ohrenschmalz gründlich zu entfernen und die Lebensdauer Ihres Hörgeräts zu verlängern.</p>
        <p style="color:var(--text);font-weight:600;margin:22px 0 14px">Schritte zur einfachen Reinigung:</p>
        <ul class="ticks">
          <li>Legen Sie eine weiche Unterlage bereit, um Schäden durch Herunterfallen zu vermeiden.</li>
          <li>Achten Sie darauf, dass Ihre Hände sauber und trocken sind.</li>
          <li>Reinigen Sie das Ohrpassstück vorsichtig mit einem desinfizierenden Feuchttuch.</li>
          <li>Verwenden Sie niemals Wasser, Spül- oder Reinigungsmittel für das Hörgerät.</li>
          <li>Lagern Sie das Hörgerät über Nacht in einer Trockenbox, um Feuchtigkeit zu entfernen.</li>
          <li>Nehmen Sie das Gerät vor dem Duschen ab.</li>
          <li>Vermeiden Sie Make-up-Auftrag in der Nähe des Hörgeräts.</li>
        </ul>
        <p style="margin-top:22px">Für weitere Pflegehinweise und passende Reinigungsprodukte stehen wir Ihnen gerne zur Seite!</p>
      </article>
    </div>
  </div>
</section>
<section class="section section--line" aria-labelledby="produkte">
  <div class="container">
    <div class="sec-head"><div class="rv"><span class="eyebrow">Sortiment</span><h2 class="h-lg" id="produkte">Pflegeprodukte im <em>Geschäft</em></h2></div></div>
    <div class="rv"><div class="tabs" role="tablist" aria-label="Produktkategorien">{tabs}</div>{panels}</div>
  </div>
</section>'''
    return sub_page(dict(
        path="/hoerakustik/zubehoer-und-reinigung/", crumbs=HOER_CRUMB + [("Zubehör und Reinigung", "/hoerakustik/zubehoer-und-reinigung/")],
        title="Zubehör für Hörgeräte & Hörgerätereinigung in Innsbruck | Optik Gaertner",
        desc="Hier erfahren Sie mehr über Zubehör für Hörgeräte & Hörgerätereinigung von Optik Gaertner in Innsbruck. Bei Fragen beraten wir Sie gerne.",
        eyebrow="Zubehör & mehr", h1="<em>Zubehör</em> für Hörgeräte und Hörgerätereinigung bei Ihrem Hörakustiker in Innsbruck",
        intro=P("Eine fachgerechte und regelmäßige Reinigung Ihres Hörgeräts trägt zu einer langen Lebensdauer und einwandfreiem Funktionieren bei. In unserem Geschäft in Innsbruck finden Sie nicht nur alles, was Sie für die Reinigung Ihres Hörgeräts brauchen, sondern auch eine vielfältige Auswahl an Zubehör, das Ihnen den Alltag erleichtert."),
        hero="QqXw6DJF", hero_alt="Reinigung von Hörgeräten", buttons=HOER_BTNS,
        img="YD09NizD", img_alt="Zubehör für Hörgeräte",
        h2="Zubehör: Praktische <em>Alltagshelfer</em> bei Ihrem Hörakustiker",
        h2_text=P("Eine Hörminderung kann das Alltagsleben und die Teilnahme am sozialen Leben erschweren. Ihr Hörakustiker bietet Ihnen vielfältige Lösungen rund ums Hören – von der Verbindung Ihres Hörgeräts zu verschiedenen Endgeräten bis hin zu Lichtsignalen, die dafür sorgen, dass Sie auch bei Schwerhörigkeit die Türglocke oder das Telefon nicht überhören."),
        extra=extra,
        siblings=HOER_SIB, siblings_label="Weitere Themen in der Hörakustik",
    ))


def gehoerschutz():
    crumbs = [("Home", "/"), ("Gehörschutz", "/gehoerschutz/")]
    topics = ["Otoplastik", "ICP (Hörgeräte am Lärm-Arbeitsplatz)", "IEM-Produkte (InEar-Monitoring)", "Schlafschutz", "Schwimmschutz", "Gesetzlichem Arbeitnehmerschutz"]
    chips = "".join(f'<span class="chip">{icon("check")}{escape(t)}</span>' for t in topics)
    prod_gal = [("3o5nF0mV", "Gehörschutz mit Helm"), ("2QM9IFlY", "Gehörschutz unter dem Helm"), ("0OKCLcXE", "Gehörschutz am Bau"),
                ("QUoQzlxw", "Gehörschutz bei der Arbeit"), ("v4ecfElm", "Gehörschutz in der Werkstatt"), ("yUu7F2Kv", "Gehörschutz an der Maschine"),
                ("OWETZN1Y", "Gehörschutz in der Forstarbeit"), ("mNRxtQNF", "Gehörschutz im Wald"), ("AmLEB4SM", "Forstarbeiter mit Gehörschutz"),
                ("T739BWFg", "ISOtunes Gehörschutz"), ("yiGsL9l7", "ISOtunes Gehörschutz bei der Arbeit"), ("2ltG8mVz", "ISOtunes Kapselgehörschutz"),
                ("EbLhmIln", "In-Ear-Monitoring bei der Moderation"), ("c4DJRgS8", "Kommunikations-Otoplastik"), ("MFH89bKI", "Moderation mit In-Ear"),
                ("tIdx8Ol3", "Security mit Kommunikations-Otoplastik"), ("cxGEYd4l", "Security mit In-Ear"), ("5mRvgj1h", "Snug Gehörschutz"),
                ("caBLqa5s", "Gehörschutz beim Klettern"), ("75WLjz57", "Kletterer mit Gehörschutz"), ("6IpA8KPA", "Gehörschutz in der Halle"),
                ("QMFenQ2K", "Gehörschutz beim Sport"), ("JL5sBYsP", "Gehörschutz im Alltag"), ("AyVrtVDk", "Gehörschutz-Otoplastik")]
    lab_gal = [("DDbhJjP3", "Labor"), ("rY7eKU8B", "Arbeit im Labor"), ("ISQIjF5R", "Otoplastik-Fertigung"), ("gDxTjUaP", "Abformung"),
               ("D4lBPZjz", "Bearbeitung einer Otoplastik"), ("sLlvj5yV", "Feinarbeit im Labor"), ("b0wZbBC2", "Fertigung im Labor"),
               ("zp9IiUYm", "Otoplastiken"), ("t696h20X", "Laborarbeitsplatz"), ("yGxkTdex", "Qualitätsprüfung"), ("OAWqG5R2", "Otoplastik-Varianten"),
               ("jBAooPyV", "Labor-Ausstattung"), ("OKutVxT6", "Farbpalette für Otoplastiken"), ("p61zJ8fy", "Gehörschutz-Muster"),
               ("WxnhSDYo", "Gaertner Labor – TirolQ")]
    swim_gal = [("0FoV8lIJ", "Schwimmschutz in roter Dose"), ("WZTZLyNg", "Schwimmschutz"), ("SM0IKEvz", "Bunter Schwimmschutz"),
                ("5ZRKSqxl", "Schwimmschutz-Otoplastik"), ("tKKbkBiG", "Schwimmschutz mit Halteband"), ("wKjifmy6", "Muster für Schwimmschutz")]

    body = page_hero(
        "Gehörschutz", "Ihr Fachmann für <em>Gehörschutz</em> in Innsbruck",
        P("Ob in der Arbeit oder Freizeit: Lärm bedeutet für unser Gehör Stress und geht stets mit Gefahr einher. Auch Spritzwasser kann für empfindliche Ohren mit Ohrenschmerzen und Infektionsgefahr einhergehen. Als Ihr Hörakustiker sind wir Ihr Ansprechpartner in Sachen Gehörschutz und bieten Ihnen für jede Lebenslage das passende Schutzprodukt."),
        image="JE0b3EEE", alt="Gehörschutz", crumbs=crumbs,
        buttons=[btn("Termin vereinbaren", "/kontakt/#termin"), f'<a class="btn btn-ghost" href="tel:+43512570159">{icon("phone")}+43 512 57 01 59</a>']) + f'''
<section class="section">
  <div class="container">
    {split(f"""<span class="eyebrow">Made in Tirol</span>
<h2 class="h-lg" style="margin:20px 0 26px">Gehörschutz auf <em>höchstem</em> Niveau</h2>
<div class="prose"><p>Wir bieten maßgeschneiderten Gehörschutz für jede Anforderung – made in Tirol. Vom einfachen Gehörschutz bis hin zu speziellen Bedürfnissen wie Jägergehörschutz oder In-Ear-Monitoring für Musiker. Dank unseres eigenen Akustiklabors garantieren wir präzise Anpassung und höchste Qualität. Egal, ob Sie Ihre Ohren vor Maschinenlärm, Schussknall oder lauten Bühnensounds schützen möchten – wir entwickeln Lösungen, die Komfort und Schutz perfekt kombinieren.</p></div>
<p class="kicker" style="margin:30px 0 14px">Wir beraten Sie zu:</p><div class="chips">{chips}</div>""",
           f'<div class="frame frame--square">{img("FS9RypWc", "Maßgefertigter Gehörschutz")}</div>')}
  </div>
</section>
<section class="section section--line">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><span class="eyebrow">Langzeitschutz</span><h2 class="h-lg">Mit hochwertigem Gehörschutz <em>rundum sicher</em></h2></div>
      <p class="lead rv" style="--d:.1s">Wird das Gehör immer wieder einer starken Lärmbelastung ausgesetzt, so kann es zu Langzeitschäden kommen. Disco, laute Konzerte, aber auch ein lautes Arbeitsumfeld können auf lange Sicht zu einer Hörminderung führen, wenn Sie Ihre Ohren nicht adäquat schützen. Lassen Sie sich von uns zum Thema Hörschutz beraten – wir sind gerne für Sie da.</p>
    </div>
    <div class="rv">{gallery("gs", prod_gal)}</div>
  </div>
</section>
<section class="section section--line" aria-labelledby="labor">
  <div class="container">
    <div class="sec-head">
      <div class="rv"><span class="eyebrow">Eigenes Akustiklabor</span><h2 class="h-lg" id="labor"><em>Labor</em></h2></div>
      <p class="lead rv" style="--d:.1s">In unserem hauseigenen Labor fertigen wir individuellen Gehörschutz nach höchsten Qualitätsstandards – exakt abgestimmt auf Ihre Bedürfnisse. Jedes Produkt wird von Hand hergestellt und präzise geprüft, bevor es unser Haus verlässt. So stellen wir sicher, dass Sie zuverlässigen Schutz und maximalen Tragekomfort erhalten – ganz gleich, in welcher Situation Sie Ihr Gehör schonen oder unterstützen möchten.</p>
    </div>
    <div class="rv">{gallery("lab", lab_gal, "rail")}</div>
  </div>
</section>
<section class="section section--line">
  <div class="container">
    <div style="margin-bottom:clamp(60px,8vw,110px)">
    {split(f"""<span class="eyebrow">Schlafschutz</span>
<h2 class="h-lg" style="margin:20px 0 26px"><em>Schlafschutz</em></h2>
<div class="prose"><p>Erholsamer Schlaf ist essenziell für Gesundheit und Wohlbefinden. Ein maßgefertigter Schlafschutz sorgt für ungestörte Ruhe, indem er störende Geräusche wie Schnarchen, Verkehr oder Umgebungslärm effektiv dämpft – wichtige Signale wie Wecker, Telefon, Rauchmelder oder das Schreien eines Kindes bleiben dabei weiterhin wahrnehmbar.</p>
<p>Ob zu Hause, im Urlaub, in Berghütten oder beim Camping: Der individuell angepasste Gehörschutz passt sich jeder Schlafumgebung an und kann auch die Konzentration fördern. Gefertigt aus besonders weichem Silikon bietet er hohen Tragekomfort, auch für Seitenschläfer. Dank präziser Anpassung sitzt er sicher und druckfrei – so leicht, dass man ihn kaum spürt.</p></div>""",
           f'<div class="frame frame--wide">{img("etu7QxAk", "Schlafschutz")}</div>')}
    </div>
    {split(f"""<span class="eyebrow">Schwimmschutz</span>
<h2 class="h-lg" style="margin:20px 0 26px"><em>Schwimmschutz</em></h2>
<div class="prose"><p>Ein maßgefertigter Spritzwasserschutz sorgt für unbeschwerten Wasserspaß – im Schwimmbad, am Meer oder beim Duschen. Gefertigt aus hochwertigem, schwimmfähigem Silikon hält er Wasser zuverlässig vom Gehörgang fern und schützt zusätzlich vor Bakterien und Infektionen. Besonders geeignet ist er für empfindliche Ohren oder zur Vorbeugung von Entzündungen, auch bei Kindern.</p>
<p>Die individuelle Anpassung gewährleistet einen sicheren Sitz ohne Verrutschen, während das weiche, hautfreundliche Material hohen Tragekomfort bietet. Ein praktischer Griff erleichtert das Einsetzen und Herausnehmen, optional sind Halteband und verschiedene Farben erhältlich.</p>
<p>Für aktive Wassersportler gibt es zudem Varianten mit Spezialfilter, die Wasser abhalten und gleichzeitig Sprache sowie Umgebungsgeräusche gut hörbar lassen – für mehr Sicherheit beim Training und Wettkampf. <strong>Nicht geeignet für Sporttauchen.</strong></p></div>""",
           f'<div class="frame frame--tall">{img("DGNY7neN", "Schwimmschutz in verschiedenen Farben am Pool")}</div>', rev=True)}
    <div class="rv" style="margin-top:50px">{gallery("swim", swim_gal, "rail")}</div>
  </div>
</section>
{related("/gehoerschutz/", HOER_SIB, "Weitere Themen in der Hörakustik")}
{default_cta()}'''
    return page("/gehoerschutz/", "Professioneller Gehörschutz in Innsbruck | Optik Gaertner",
                "Optik Gaertner bietet Ihnen professionellen Gehörschutz, InEars & Otoplastik in Innsbruck. Wir nehmen uns gerne Zeit für Sie.",
                body, og="JE0b3EEE", crumbs=crumbs)


def build():
    write("/hoerakustik/", hoerakustik())
    write("/hoerakustik/hoergeraete/", hoergeraete())
    write("/hoerakustik/hoergeraete-mit-app-verbinden/", app())
    write("/hoerakustik/tinnitus/", tinnitus())
    write("/hoerakustik/zubehoer-und-reinigung/", zubehoer())
    write("/gehoerschutz/", gehoerschutz())
