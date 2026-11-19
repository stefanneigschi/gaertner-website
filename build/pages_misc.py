"""Kontakt, Rechtliches, Danke, 404."""
from lib import (img, src, icon, btn, page, write, page_hero, locations_html, LOCATIONS, TEL_OPTIK, PHONE_OPTIK, escape)


def kontakt():
    crumbs = [("Home", "/"), ("Kontakt", "/kontakt/")]
    opts = "".join(f"<option>{escape(l['name'])}</option>" for l in LOCATIONS)
    body = page_hero(
        "Kontakt", "Kontakt &amp; <em>Anfahrt</em>",
        "<p>Haben Sie Fragen? Rufen Sie uns an – das Team von Optik Gaertner in Innsbruck wird Sie gerne beraten. Sie erreichen uns in nur 7 Gehminuten vom Hauptbahnhof. Parken können Sie bequem in der „Casino-Garage“, die nur ca. 3 Gehminuten entfernt ist.</p>",
        crumbs=crumbs, plain=True,
        buttons=[f'<a class="btn btn-primary" href="tel:{TEL_OPTIK}">{icon("phone")}{PHONE_OPTIK}</a>', btn("Anfrage senden", "#termin", "ghost")]) + \
        locations_html(heading=False) + f'''
<section class="section section--line" id="termin" aria-labelledby="t">
  <div class="container">
    <div class="split split--top">
      <div class="rv">
        <span class="eyebrow">Terminanfrage</span>
        <h2 class="h-lg" id="t" style="margin:20px 0 22px">Schreiben Sie <em>uns</em>.</h2>
        <p class="lead">Wählen Sie das passende Fachgeschäft und nennen Sie uns Ihr Anliegen. Wir melden uns mit einem Terminvorschlag – in der Regel innerhalb eines Werktags.</p>
        <div class="frame frame--wide" style="margin-top:36px">{img('Nt3znHfI', 'Verkaufsraum von Gaertner Optik')}</div>
      </div>
      <form class="card form rv" style="--d:.1s" name="terminanfrage" method="POST" action="/danke/" data-netlify="true" netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="terminanfrage">
        <p class="hp"><label>Nicht ausfüllen: <input name="bot-field"></label></p>
        <div class="field full"><label for="k-standort">Fachgeschäft*</label><select id="k-standort" name="standort" required><option value="">Bitte wählen</option>{opts}</select></div>
        <div class="field"><label for="k-name">Name*</label><input id="k-name" name="name" required autocomplete="name"></div>
        <div class="field"><label for="k-tel">Telefonnummer</label><input id="k-tel" name="telefon" type="tel" autocomplete="tel"></div>
        <div class="field full"><label for="k-mail">E-Mail-Adresse*</label><input id="k-mail" name="email" type="email" required autocomplete="email"></div>
        <div class="field full"><label for="k-msg">Ihr Anliegen*</label><textarea id="k-msg" name="nachricht" required placeholder="z. B. Sehtest, Hörtest, Reparatur, Beratung zu Gehörschutz …"></textarea></div>
        <label class="check full"><input type="checkbox" name="datenschutz" required> <span>Es werden personenbezogene Daten übermittelt und für die in der <a href="/datenschutz/">Datenschutzseite</a> beschriebenen Zwecke verwendet. *</span></label>
        <div class="full"><button class="btn btn-primary" type="submit">Anfrage senden{icon('arrow')}</button></div>
      </form>
    </div>
  </div>
</section>'''
    return page("/kontakt/", "Optik Gaertner in Innsbruck - Kontakt & Anfahrt",
                "Haben Sie Fragen? Rufen Sie uns an - das Team von Optik Gaertner in Innsbruck wird Sie gerne beraten.",
                body, og="Hwbk6TzX", crumbs=crumbs)


CREDITS = """AdobeStock_104835635.jpeg-Syda Productions - stock.adobe.com AdobeStock_114882840.jpeg-javitrapero.com - stock.adobe.com AdobeStock_127682737.jpeg-Liudmila Dutko - stock.adobe.com AdobeStock_165806367.jpeg-Manok - stock.adobe.com AdobeStock_170990733.jpeg-Memed ÖZASLAN - stock.adobe.com AdobeStock_175281327.jpeg-Africa Studio - stock.adobe.com AdobeStock_207156633.jpeg-ivanko80 - stock.adobe.com AdobeStock_231397852.jpeg-Nomad_Soul - stock.adobe.com AdobeStock_246922173.jpeg-Cookie Studio - stock.adobe.com AdobeStock_27941424.jpeg-StefanieBaum - stock.adobe.com AdobeStock_284838853.jpeg-olly - stock.adobe.com AdobeStock_293006762.jpeg-BillionPhotos.com - stock.adobe.com AdobeStock_317123038.jpeg-Morocko - stock.adobe.com AdobeStock_326993165.jpeg-weyo - stock.adobe.com AdobeStock_334076925.jpeg-Strelciuc - stock.adobe.com AdobeStock_349634413.jpeg-Pixel-Shot - stock.adobe.com AdobeStock_375104598.jpeg-BlackMediaHouse - stock.adobe.com AdobeStock_408980630.jpeg-Svitlana - stock.adobe.com AdobeStock_462844409.jpeg-Azulblue - stock.adobe.com AdobeStock_522998695.jpeg-Dusko - stock.adobe.com AdobeStock_548914614.jpeg-S Fanti/peopleimages.com - stock.adobe.com AdobeStock_575654984.jpeg-Prostock-studio - stock.adobe.com AdobeStock_622353061.jpeg-Theron/peopleimages.com - stock.adobe.com AdobeStock_632467555.jpeg-Trik - stock.adobe.com AdobeStock_893480170.jpeg-Trik - stock.adobe.com
AdobeStock_89435346.jpeg-Premium Collection - stock.adobe.com
AdobeStock_279299167.jpeg-SHOTPRIME STUDIO - stock.adobe.com
AdobeStock_415740740.jpeg-diquesvet - stock.adobe.com
gfx_yasir 993386540
Dorde 1021484232
Dilshad 1030200787
reddish 1089335746
RealPeopleStudio 780987931
Rido 399499905
InsideCreativeHouse 304537986
miss irine 1131787695
Dina Photo Stories 1002771395
Vadim 305945198
Jürgen Fälchle 601739429
Ezio Gutzemberg 700010932, 700009245
TigerDude 919370553
JoxyAimages 987638762
LIGHTFIELD STUDIOS 738358126, 738364254
peterschreiber.media #237374285
Mountains Hunter #289449457
Valeri Luzina #233318661"""


def impressum():
    crumbs = [("Home", "/"), ("Impressum", "/impressum/")]
    kv = [("Vollständiger Firmenname", "Gaertner GmbH"),
          ("Ort der Gewerbeberechtigung", "Leopoldstraße 16, 6020 Innsbruck, Österreich"),
          ("UID-Nummer", "ATU77352516"), ("Rechtsform", "GmbH"),
          ("Geschäftsführung/Juristische Person", "Sophie Grimm-Gaertner, Joseph Gaertner"),
          ("Firmenbuchnummer", "FN565210t"), ("Firmenbuchgericht", "Landesgericht Innsbruck"),
          ("Unternehmensgegenstand", "Augenoptiker"), ("Kammer/Berufsverband-Zugehörigkeit(en)", "WK Tirol"),
          ("Aufsichtsbehörde", "Magistrat der Stadt Innsbruck"),
          ("Gewerbeordnung", 'Anwendbare gewerbe- oder berufsrechtliche Vorschriften: Gewerbeordnung 1994, abrufbar unter <a href="https://www.ris.bka.gv.at" target="_blank" rel="noopener">www.ris.bka.gv.at</a>')]
    kvh = "".join(f"<dt>{escape(k)}</dt><dd>{v if '<a' in v else escape(v)}</dd>" for k, v in kv)
    credits = "<br>".join(escape(x) for x in CREDITS.split("\n"))
    body = page_hero("Rechtliches", "Impressum", "", crumbs=crumbs, plain=True) + f'''
<section class="section" style="padding-top:20px">
  <div class="container legal">
    <h2 style="margin-top:0">Optik Gaertner</h2>
    <p>Leopoldstraße 16<br>6020 Innsbruck<br>Telefon: <a href="tel:{TEL_OPTIK}">{PHONE_OPTIK}</a><br>E-Mail: <a href="mailto:optik@gaertner-innsbruck.at">optik@gaertner-innsbruck.at</a></p>
    <dl class="kv" style="margin-top:32px">{kvh}</dl>

    <h2>Fotos Copyright</h2>
    <p class="credits">{credits}</p>

    <h2>Haftungsausschluss</h2>
    <h3>Inhalt des Onlineangebotes</h3>
    <p>Der Autor übernimmt keinerlei Gewähr für die Aktualität, Korrektheit, Vollständigkeit oder Qualität der bereitgestellten Informationen. Haftungsansprüche gegen den Autor, welche sich auf Schäden materieller oder ideeller Art beziehen, die durch die Nutzung oder Nichtnutzung der dargebotenen Informationen bzw. durch die Nutzung fehlerhafter und unvollständiger Informationen verursacht wurden, sind grundsätzlich ausgeschlossen, sofern seitens des Autors kein nachweislich vorsätzliches oder grob fahrlässiges Verschulden vorliegt. Alle Angebote sind freibleibend und unverbindlich. Der Autor behält es sich ausdrücklich vor, Teile der Seiten oder das gesamte Angebot ohne gesonderte Ankündigung zu verändern, zu ergänzen, zu löschen oder die Veröffentlichung zeitweise oder endgültig einzustellen.</p>
    <h3>Verweise und Links</h3>
    <p>Bei direkten oder indirekten Verweisen auf fremde Internetseiten (Links), die außerhalb des Verantwortungsbereiches des Autors liegen, würde eine Haftungsverpflichtung ausschließlich in dem Fall in Kraft treten, in dem der Autor von den Inhalten Kenntnis hat und es ihm technisch möglich und zumutbar wäre, die Nutzung im Falle rechtswidriger Inhalte zu verhindern. Der Autor erklärt hiermit ausdrücklich, dass zum Zeitpunkt der Linksetzung keine illegalen Inhalte auf den zu verlinkenden Seiten erkennbar waren. Auf die aktuelle und zukünftige Gestaltung, die Inhalte oder die Urheberschaft der gelinkten/verknüpften Seiten hat der Autor keinerlei Einfluss. Deshalb distanziert er sich hiermit ausdrücklich von allen Inhalten aller gelinkten/verknüpften Seiten, die nach der Linksetzung verändert wurden. Diese Feststellung gilt für alle innerhalb des eigenen Internetangebotes gesetzten Links und Verweise sowie für Fremdeinträge in vom Autor eingerichtete Gästebücher, Diskussionsforen und Mailinglisten. Für illegale, fehlerhafte oder unvollständige Inhalte und insbesondere für Schäden, die aus der Nutzung oder Nichtnutzung solcherart dargebotener Informationen entstehen, haftet allein der Anbieter der Seite, auf welche verwiesen wurde, nicht derjenige, der über Links auf die jeweilige Veröffentlichung lediglich verweist.</p>
    <h3>Urheber- und Kennzeichenrecht</h3>
    <p>Der Autor ist bestrebt, in allen Publikationen die Urheberrechte der verwendeten Grafiken, Tondokumente, Videosequenzen und Texte zu beachten, von ihm selbst erstellte Grafiken, Tondokumente, Videosequenzen und Texte zu nutzen oder auf lizenzfreie Grafiken, Tondokumente, Videosequenzen und Texte zurückzugreifen. Alle innerhalb des Internetangebotes genannten und ggf. durch Dritte geschützten Marken- und Warenzeichen unterliegen uneingeschränkt den Bestimmungen des jeweils gültigen Kennzeichenrechts und den Besitzrechten der jeweiligen eingetragenen Eigentümer. Allein aufgrund der bloßen Nennung ist nicht der Schluss zu ziehen, dass Markenzeichen nicht durch Rechte Dritter geschützt sind! Das Copyright für veröffentlichte, vom Autor selbst erstellte Objekte bleibt allein beim Autor der Seiten. Eine Vervielfältigung oder Verwendung solcher Grafiken, Tondokumente, Videosequenzen und Texte in anderen elektronischen oder gedruckten Publikationen ist ohne ausdrückliche Zustimmung des Autors nicht gestattet.</p>
    <h3>Datenschutz</h3>
    <p>Sofern innerhalb des Internetangebotes die Möglichkeit zur Eingabe persönlicher oder geschäftlicher Daten (E-Mail-Adressen, Namen, Anschriften) besteht, so erfolgt die Preisgabe dieser Daten seitens des Nutzers auf ausdrücklich freiwilliger Basis. Die Inanspruchnahme und Bezahlung aller angebotenen Dienste ist - soweit technisch möglich und zumutbar - auch ohne Angabe solcher Daten bzw. unter Angabe anonymisierter Daten oder eines Pseudonyms gestattet. Die Nutzung der im Rahmen des Impressums oder vergleichbarer Angaben veröffentlichten Kontaktdaten wie Postanschriften, Telefon- und Faxnummern sowie E-Mail-Adressen durch Dritte zur Übersendung von nicht ausdrücklich angeforderten Informationen ist nicht gestattet. Rechtliche Schritte gegen die Versender von so genannten Spam-Mails bei Verstößen gegen dieses Verbot sind ausdrücklich vorbehalten. Details finden Sie in unserer <a href="/datenschutz/">Datenschutzerklärung</a>.</p>
    <h3>Rechtswirksamkeit dieses Haftungsausschlusses</h3>
    <p>Dieser Haftungsausschluss ist als Teil des Internetangebotes zu betrachten, von dem aus auf diese Seite verwiesen wurde. Sofern Teile oder einzelne Formulierungen dieses Textes der geltenden Rechtslage nicht, nicht mehr oder nicht vollständig entsprechen sollten, bleiben die übrigen Teile des Dokumentes in ihrem Inhalt und ihrer Gültigkeit davon unberührt.</p>
    <h3>Online-Streitbeilegung</h3>
    <p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit, die Sie unter <a href="https://ec.europa.eu/odr/" target="_blank" rel="noopener">ec.europa.eu/odr</a> finden.</p>
    <h3>Cookies</h3>
    <p>Bei Cookies handelt es sich um Dateien, die auf der lokalen Festplatte Ihres Computers angelegt werden. Sie ermöglichen ein besseres Nutzererlebnis, indem sie Daten zu den von Ihnen aufgerufenen Websites abspeichern. So ermöglichen Cookies etwa, die Ladezeit einer mehrmals besuchten Website deutlich zu kürzen, oder Ihnen das erneute Eingeben von Daten zu erleichtern. Sie haben die Möglichkeit, das Speichern von Cookies auf Ihrem Rechner zu verhindern. Dazu wählen Sie in Ihren Browser-Einstellungen die Option „Keine Cookies akzeptieren“. Sie können in Ihren Browser-Einstellungen auch definieren, dass Sie die Speicherung der Daten jedes Mal explizit bestätigen müssen. Des Weiteren können gespeicherte Cookies jederzeit gelöscht werden. Falls Sie keine Cookies akzeptieren, kann es zu Einschränkungen in der Funktion oder zu verzögerter Ladezeit beim Aufruf dieser Website kommen.</p>
  </div>
</section>'''
    return page("/impressum/", "Impressum - Optik Gaertner in Innsbruck",
                "Hier finden Sie das Impressum von Optik Gaertner in 6020 Innsbruck. Bei Fragen beraten wir Sie gerne - rufen Sie uns an.",
                body, crumbs=crumbs)


def datenschutz():
    crumbs = [("Home", "/"), ("Datenschutz", "/datenschutz/")]
    # ENTWURF – vor Livegang rechtlich prüfen lassen (siehe README.md)
    body = page_hero("Rechtliches", "Datenschutzerklärung", "", crumbs=crumbs, plain=True) + f'''
<section class="section" style="padding-top:20px">
  <div class="container legal">
    <h2 style="margin-top:0">1. Verantwortlicher</h2>
    <p>Gaertner GmbH<br>Leopoldstraße 16, 6020 Innsbruck, Österreich<br>Telefon: <a href="tel:{TEL_OPTIK}">{PHONE_OPTIK}</a><br>E-Mail: <a href="mailto:optik@gaertner-innsbruck.at">optik@gaertner-innsbruck.at</a></p>
    <p>Der Schutz Ihrer personenbezogenen Daten ist uns ein wichtiges Anliegen. Wir verarbeiten Ihre Daten ausschließlich auf Grundlage der gesetzlichen Bestimmungen (DSGVO, DSG, TKG 2021). In dieser Datenschutzerklärung informieren wir Sie über die wichtigsten Aspekte der Datenverarbeitung im Rahmen unserer Website.</p>

    <h2>2. Aufruf der Website und Hosting</h2>
    <p>Beim Aufruf dieser Website werden durch den Hosting-Anbieter technisch notwendige Daten verarbeitet (IP-Adresse, Datum und Uhrzeit des Zugriffs, aufgerufene Seite, Browser- und Betriebssysteminformationen). Diese Daten dienen ausschließlich der sicheren und stabilen Bereitstellung der Website und werden nicht mit anderen Datenquellen zusammengeführt. Rechtsgrundlage ist unser berechtigtes Interesse gemäß Art. 6 Abs. 1 lit. f DSGVO.</p>
    <p>Die Website wird bei Netlify, Inc., 512 2nd Street, Suite 200, San Francisco, CA 94107, USA gehostet. Netlify ist unter dem EU-US Data Privacy Framework zertifiziert; zusätzlich bestehen Standardvertragsklauseln gemäß Art. 46 DSGVO.</p>

    <h2>3. Kontakt- und Bestellformulare</h2>
    <p>Wenn Sie uns über das Anfrageformular oder das Formular zur Nachbestellung von Kontaktlinsen kontaktieren, verarbeiten wir die von Ihnen angegebenen Daten (z. B. Name, Kontaktdaten, Adresse, Geburtsdatum, Ihre Nachricht) zur Bearbeitung Ihrer Anfrage bzw. Bestellung. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Vertragsanbahnung bzw. -erfüllung). Die Formulardaten werden über den Dienst Netlify Forms übermittelt und an uns weitergeleitet. Wir speichern die Daten nur so lange, wie es für die Bearbeitung und aufgrund gesetzlicher Aufbewahrungspflichten erforderlich ist.</p>
    <p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, verarbeiten wir Ihre Angaben zur Bearbeitung Ihres Anliegens auf derselben Rechtsgrundlage.</p>

    <h2>4. Cookies, Analyse und Schriften</h2>
    <p>Diese Website verwendet keine Cookies zu Analyse- oder Marketingzwecken und setzt keine Tracking-Dienste ein. Die verwendeten Schriftarten sind lokal auf unserem Server eingebunden; beim Aufruf der Website wird keine Verbindung zu Servern von Google oder anderen Schriftanbietern hergestellt.</p>

    <h2>5. Externe Links</h2>
    <p>Unsere Website enthält Links zu externen Angeboten, etwa zu Google Maps (Anfahrtsplanung), zum Online-Hörtest (digitalhearingtest.com) oder zu See Sophie (seesophie.at). Erst wenn Sie einen solchen Link anklicken, werden Daten an den jeweiligen Anbieter übertragen. Für die Datenverarbeitung auf diesen Seiten ist der jeweilige Anbieter verantwortlich.</p>

    <h2>6. Ihre Rechte</h2>
    <p>Ihnen stehen grundsätzlich die Rechte auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch zu. Wenn Sie glauben, dass die Verarbeitung Ihrer Daten gegen das Datenschutzrecht verstößt, können Sie sich bei uns oder bei der Aufsichtsbehörde beschweren. In Österreich ist dies die Datenschutzbehörde, Barichgasse 40–42, 1030 Wien, <a href="https://www.dsb.gv.at" target="_blank" rel="noopener">www.dsb.gv.at</a>.</p>

    <h2>7. Kontakt in Datenschutzfragen</h2>
    <p>Bei Fragen zum Datenschutz erreichen Sie uns unter <a href="mailto:optik@gaertner-innsbruck.at">optik@gaertner-innsbruck.at</a> oder telefonisch unter <a href="tel:{TEL_OPTIK}">{PHONE_OPTIK}</a>.</p>
  </div>
</section>'''
    return page("/datenschutz/", "Datenschutz - Optik Gaertner in Innsbruck",
                "Datenschutzerklärung von Optik Gaertner in Innsbruck: welche Daten wir beim Besuch der Website und bei Anfragen verarbeiten und welche Rechte Sie haben.",
                body, crumbs=crumbs)


def danke():
    body = page_hero("Vielen Dank", "Ihre Nachricht ist <em>angekommen</em>.",
                     "<p>Vielen Dank für Ihre Anfrage. Wir melden uns so rasch wie möglich bei Ihnen – in der Regel innerhalb eines Werktags.</p>",
                     plain=True, buttons=[btn("Zur Startseite", "/"), f'<a class="btn btn-ghost" href="tel:{TEL_OPTIK}">{icon("phone")}{PHONE_OPTIK}</a>'])
    return page("/danke/", "Vielen Dank | Optik Gaertner Innsbruck",
                "Vielen Dank für Ihre Nachricht an Optik Gaertner in Innsbruck. Wir melden uns so rasch wie möglich bei Ihnen.",
                body, robots="noindex, follow")


def not_found():
    body = page_hero("Fehler 404", "Diese Seite gibt es <em>nicht</em> (mehr).",
                     "<p>Möglicherweise wurde die Seite verschoben. Über die Navigation oder die Startseite finden Sie rasch zum gewünschten Inhalt.</p>",
                     image="aOHYeayl", alt="Luchs",
                     buttons=[btn("Zur Startseite", "/"), btn("Kontakt", "/kontakt/", "ghost")])
    return page("/404.html", "Seite nicht gefunden | Optik Gaertner Innsbruck",
                "Die gesuchte Seite wurde nicht gefunden. Über die Startseite gelangen Sie zu allen Angeboten von Optik Gaertner in Innsbruck.",
                body, robots="noindex, follow")


def build():
    write("/kontakt/", kontakt())
    write("/impressum/", impressum())
    write("/datenschutz/", datenschutz())
    write("/danke/", danke())
    write("/404.html", not_found())
