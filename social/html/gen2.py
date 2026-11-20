import os, json, shutil
ROOT='/home/user/gaertner-website'; OUT=ROOT+'/social/html'
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT)
A='file://'+ROOT+'/dist/assets'
def I(f): return f'{A}/img/{f}'
CSS=f'''@font-face{{font-family:"Manrope";src:url("{A}/fonts/manrope-latin-wght-normal.woff2");font-weight:200 800}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:#080a09;background-image:radial-gradient(70% 40% at 0% 0%,rgba(0,140,60,.22),transparent 70%);color:#eef2ec;font-family:Manrope,sans-serif;-webkit-font-smoothing:antialiased}}
.p{{position:absolute;inset:0;padding:64px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;font-size:20px;letter-spacing:.12em;text-transform:uppercase;color:#c3db9a;font-weight:600}}
.top img{{height:26px}}
.frame{{border-radius:24px;overflow:hidden;background:#111512;border:1px solid rgba(255,255,255,.08)}}
.frame img{{width:100%;height:100%;object-fit:cover;display:block}}
.t{{font-weight:600;letter-spacing:-.035em;line-height:1.08}}
.g{{color:#00bd52}}
.s{{font-size:28px;line-height:1.45;color:#a6b0a9}}
.n{{font-size:30px;font-weight:600;color:#00bd52;display:inline-block;margin-bottom:14px;letter-spacing:.04em}}
.foot{{display:flex;justify-content:space-between;font-size:20px;color:#717c75}}
'''
LOGO=I('logowhitesmall.webp')
def doc(b): return f'<!doctype html><html lang="de-AT"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="p">{b}</div></body></html>'
def cover(img,pos,title,tag):
    return doc(f'''<div class="top"><img src="{LOGO}"><span>{tag}</span></div>
<div class="frame" style="flex:1;margin:40px 0 44px"><img src="{I(img)}" style="object-position:{pos}"></div>
<p class="t" style="font-size:54px">{title}</p>''')
def info(i,n,tag,title,sub='',img=None,pos='center'):
    im=f'<div class="frame" style="height:520px;margin-bottom:56px"><img src="{I(img)}" style="object-position:{pos}"></div>' if img else ''
    sb=f'<p class="s" style="margin-top:24px">{sub}</p>' if sub else ''
    return doc(f'''<div class="top"><img src="{LOGO}"><span>{tag}</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{im}<p class="t" style="font-size:52px">{title}</p>{sb}</div>
<div class="foot"><span>gaertner-innsbruck.at</span><span>{i}/{n}</span></div>''')

POSTS=[]
def post(key,slides): POSTS.append((key,slides))

post('01-ihre-sinne',[cover('headernew-661-556.webp','66% 40%','Ihre Sinne in <span class="g">Bestform.</span>','Für Auge und Ohr'),
 info(2,3,'Für Auge und Ohr','Präzision für Augen &amp; Ohren.','Optiker und Hörakustiker in Innsbruck.'),
 info(3,3,'Für Auge und Ohr','Seit mehr als <span class="g">45 Jahren</span>.','Familienbetrieb · Meisterbetrieb · Eigenes Labor')])
post('02-familienbetrieb',[cover('teamneu.webp','center 30%','Familienbetrieb seit <span class="g">45+ Jahren</span>.','Über uns'),
 info(2,3,'Über uns','Johannes Grimm, Sophie Grimm-Gaertner, Joseph Gaertner.','Optik und Hörakustik aus einer Hand.'),
 info(3,3,'Über uns','Keine Nummer, sondern ein <span class="g">Mensch</span>.','Ihre Seh- und Hörlösung richtet sich nach Ihren Bedürfnissen.')])
post('03-schnellreparatur',[cover('rs-re-nature-charger-rie61-8042.webp','center 55%','Hörgerät-Reparatur in <span class="g">10 Minuten</span>.','Hörakustik'),
 info(2,3,'Hörakustik','Für Geräte <span class="g">aller Hersteller</span>.','Als freier Akustiker sind wir an keine Marke gebunden.'),
 info(3,3,'Hörakustik','Direkte Abrechnung mit Ihrer <span class="g">Krankenkasse</span>.','Gaertner Auditiv · Heiliggeiststraße 1a')])
post('04-gehoerschutz',[cover('dsc-0588.webp','center','Gehörschutz – <span class="g">made in Tirol</span>.','Eigenes Labor'),
 info(2,3,'Eigenes Labor','Von Hand gefertigt und <span class="g">geprüft</span>.','In unserem hauseigenen Labor.',img='dscf6616.webp',pos='center 40%'),
 info(3,3,'Eigenes Labor','Jagd · Arbeit · Schlaf · Schwimmen · <span class="g">In-Ear-Monitoring</span>','Maßgefertigt für jede Anforderung.')])
post('05-hoertest',[cover('adobestock-622353061.webp','center 30%','Ihr persönlicher <span class="g">Hörtest</span>.','Hörtest'),
 info(2,4,'Hörtest','Hörverlust kommt <span class="g">schleichend</span>.','Oft merkt man es erst, wenn Gespräche anstrengend werden.'),
 info(3,4,'Hörtest','Früh erkennen heißt <span class="g">besser verstehen</span>.','Und Entlastung für Gehirn und Konzentration.'),
 info(4,4,'Hörtest','Termin vereinbaren.','<span class="g">+43 512 93 53 95</span>')])
post('06-sonnenbrille',[cover('adobestock.webp','61% 50%','Gute <span class="g">Sonnenbrillen</span> erkennen.','Optik'),
 info(2,4,'Optik','<span class="n">01</span><br>CE-Zeichen'),
 info(3,4,'Optik','<span class="n">02</span><br>Bügelaufschrift EN 1836:1997'),
 info(4,4,'Optik','<span class="n">03</span><br>100 % UV-Schutz','Wir testen Ihre Sonnenbrille gerne im Geschäft.')])
post('07-kinderbrillen',[cover('adobestock-prxlywub.webp','center 35%','<span class="g">Kinderbrillen</span>, die gefallen.','Kinderbrillen'),
 info(2,3,'Kinderbrillen','Guter Sitz. Leichte Fassung. <span class="g">Bruchsichere</span> Gläser.'),
 info(3,3,'Kinderbrillen','Ihr Kind sucht <span class="g">selbst</span> aus.','Von schlicht über bunt bis zum Lieblingscomic.')])
post('08-hoergeraete-pflege',[cover('reinigung-183.webp','center','<span class="g">Hörgeräte-Pflege</span> in vier Schritten.','Pflege-Tipps'),
 info(2,5,'Pflege-Tipps','<span class="n">01</span><br>Über Nacht in die Trockenbox.'),
 info(3,5,'Pflege-Tipps','<span class="n">02</span><br>Niemals Wasser oder Spülmittel.'),
 info(4,5,'Pflege-Tipps','<span class="n">03</span><br>Vor dem Duschen abnehmen.'),
 info(5,5,'Pflege-Tipps','<span class="n">04</span><br>Alle drei Monate zur Profi-Reinigung.')])
locs=[('kontakt-gaertner.webp','Gaertner Optik','Leopoldstraße 16'),('die-fotografen003-792-414.webp','Gaertner Auditiv','Heiliggeiststraße 1a'),('kontakt-gaertner-auditiv-2-940-402-365.webp','Auditiv 2 – Labor','Heiliggeiststraße 4'),('kontakt-see-sophie.webp','See Sophie','Heiliggeiststraße 1b')]
post('09-standorte',[cover('kontakt-gaertner.webp','center','Vier Adressen in <span class="g">Innsbruck</span>.','Standorte')]+
 [info(i+2,5,'Standorte',n,a,img=f) for i,(f,n,a) in enumerate(locs)])

meta=[]
for key,sl in POSTS:
    for i,h in enumerate(sl):
        fn=f'{key}_{i+1}'; open(f'{OUT}/{fn}.html','w').write(h); meta.append(fn)
json.dump(meta,open(OUT+'/list.json','w')); print(len(meta))
