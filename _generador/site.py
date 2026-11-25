import os
# -*- coding: utf-8 -*-
import sys, os, re, json, html as H
sys.path.insert(0,'/home/claude/build')
from content import SERVICES, SECTORS
from content2 import NICHES
from content3 import WHY
PHOTO_ALT={}
try:
    from fotos_alt import PHOTO_ALT
except ImportError: pass
import scenes
OUT='/home/claude/sitio'; D=os.environ.get('VUELCOS_DOMAIN','https://TU-DOMINIO.es').rstrip('/'); LAST='2026-11-24'
E=lambda s:H.escape(s,quote=True)
ACC={'landing':'#B91C1C','web-de-negocio':'#1D4ED8','tienda-online':'#047857','reservas-y-citas':'#6D28D9','textos-y-seo':'#B45309','mantenimiento':'#475569',
 'abogados':'#1E3A8A','clinicas':'#0E7490','hosteleria':'#B45309','inmobiliarias':'#4D7C0F','reformas':'#C2410C','estetica':'#A21CAF',
 'arquitectos':'#334155','dentistas':'#0E7490','fisioterapia':'#0F766E','psicologos':'#4338CA','fontaneros':'#1D4ED8','cerrajeros':'#78350F','gimnasios':'#BE123C','casas-rurales':'#3F6212'}


home=open(f'{OUT}/index.html',encoding='utf-8').read()
m=re.search(r'<style>(.*?)</style>',home,re.S)
css=m.group(1)
EXTRA='''.ex-img.photo{position:relative}.ex-img.photo>img{width:100%;height:auto;display:block;aspect-ratio:4/3;object-fit:cover}
.ex-img.photo .badge{position:absolute;left:12px;bottom:12px;width:28%;border-radius:8px;overflow:hidden;background:#fff;box-shadow:0 6px 14px rgba(15,23,42,.25)}
.sector.ex{display:flex;flex-direction:column}.ex-img{display:block;margin:-26px -26px 16px;overflow:hidden}.ex-img svg{width:100%;height:auto;display:block}
.ex-tag{font:600 12px/1 var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--slate);margin-bottom:8px}.sector.ex .more{margin-top:auto;padding-top:10px}
.scene.photo{position:relative}.scene.photo>img{width:100%;height:auto;display:block;border-radius:14px;box-shadow:0 18px 30px rgba(15,23,42,.14);aspect-ratio:4/3;object-fit:cover}
.scene.photo .badge{position:absolute;left:-14px;bottom:-14px;width:34%;border-radius:12px;overflow:hidden;box-shadow:0 8px 18px rgba(15,23,42,.25);background:#fff}.scene.photo .badge svg{box-shadow:none;border-radius:0}
.scene{margin:0}.scene svg{width:100%;height:auto;display:block;border-radius:14px;box-shadow:0 18px 30px rgba(15,23,42,.14)}
.split{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:40px;align-items:start}
.split .mock{position:sticky;top:20px}.split .checks{grid-template-columns:1fr}
@media(max-width:900px){.split{grid-template-columns:1fr}.split .mock{position:static}}

.phero-grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:40px;align-items:center}
.phero-grid h1{max-width:16ch}
.mock{margin:0}.mock svg{width:100%;height:auto;display:block;filter:drop-shadow(0 18px 30px rgba(15,23,42,.18))}
.mock figcaption{font-size:13px;color:var(--slate);margin-top:10px}
body[style*="--acc"] .phero{background:linear-gradient(90deg,color-mix(in srgb,var(--acc) 9%,#fff),#fff 70%);border-top:6px solid var(--acc)}
body[style*="--acc"] .phero .eyebrow,body[style*="--acc"] .sec-head .eyebrow{color:var(--acc)}
body[style*="--acc"] .box{border-left-color:var(--acc)}
body[style*="--acc"] .rel a:hover{border-color:var(--acc)}
.steps{list-style:none;margin:0;padding:0;display:grid;gap:0;counter-reset:s}
.steps li{counter-increment:s;display:grid;grid-template-columns:72px 1fr;gap:6px 20px;padding:22px 0;border-top:2px solid var(--line)}
.steps li::before{content:counter(s);grid-row:1/3;font:800 52px/1 var(--display);color:var(--acc,var(--red))}
.steps h3{margin:0}.steps p{margin:0;color:var(--slate)}
.checks{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:14px 36px}
.checks li{position:relative;padding-left:34px;display:grid;gap:4px}
.checks li::before{content:"";position:absolute;left:0;top:3px;width:20px;height:20px;border-radius:50%;background:var(--acc,var(--red))}
.checks li::after{content:"";position:absolute;left:7px;top:7px;width:5px;height:9px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg)}
.checks b{font-size:18px}.checks span{color:var(--slate);font-size:16px}
.journey{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:3px solid var(--acc,var(--red))}
.journey article{padding:22px 24px 8px 0}.journey article+article{padding-left:24px;border-left:1px solid var(--line)}
.journey .n{font:800 40px/1 var(--display);color:var(--acc,var(--red));display:block;margin-bottom:10px}
.journey h3{margin:0 0 8px}.journey p{margin:0;color:var(--slate)}
body[style*="--acc"] .band .eyebrow{color:color-mix(in srgb,var(--acc) 35%,#fff)}
.band .journey{border-top-color:color-mix(in srgb,var(--acc) 55%,#fff)}
.band .journey .n{color:color-mix(in srgb,var(--acc) 40%,#fff)}
.band .journey h3{color:#fff}.band .journey p{color:#CBD5E1}.band .journey article+article{border-left-color:#334155}
.acc details{border-left:4px solid var(--acc,var(--red))}
@media(max-width:820px){.phero-grid{grid-template-columns:1fr}.checks{grid-template-columns:1fr}.journey{grid-template-columns:1fr}.journey article+article{padding-left:0;border-left:0;border-top:1px solid var(--line)}}

/* Páginas interiores */
a.sector{display:block;text-decoration:none;color:inherit}
a.sector:hover{background:var(--panel)}
a.sector span.more{display:inline-block;margin-top:10px;font-weight:700;font-size:14px;color:var(--red)}
.crumbs{padding:18px 0 0;font-size:14px;color:var(--slate)}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.crumbs li+li::before{content:"/";margin-right:6px;color:#94A3B8}
.crumbs a{text-decoration:none}.crumbs a:hover{text-decoration:underline}
.phero{padding:40px 0 56px}
.phero h1{font-size:clamp(38px,6.4vw,80px);max-width:18ch}
.phero .lead{margin:22px 0 28px}
section.tight{padding:56px 0}
.card h3 a{text-decoration:none}.card h3 a:hover{text-decoration:underline}
.lists{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.box{border-left:3px solid var(--red);background:var(--panel);padding:20px 22px;border-radius:0 4px 4px 0}
.box h3{margin-bottom:10px}
.box ul{margin:0;padding-left:18px;display:grid;gap:8px;color:var(--slate);font-size:16px}
.callout{border:2px solid var(--ink);border-radius:4px;padding:22px 24px;background:var(--panel)}
.callout .price b{color:var(--ink)}
.callout .price{border-top:0;color:var(--slate);padding-top:0}
.rel{display:flex;flex-wrap:wrap;gap:10px}
.rel a{display:inline-block;padding:10px 16px;border:2px solid var(--line);border-radius:3px;text-decoration:none;font-weight:600;font-size:15px;background:var(--panel)}
.rel a:hover{border-color:var(--ink)}
section:not(.band) .price{border-top-color:var(--line);color:var(--slate)}
section:not(.band) .price b{color:var(--ink)}
@media (max-width:900px){.lists{grid-template-columns:1fr}}
'''
os.makedirs(f'{OUT}/assets',exist_ok=True)
open(f'{OUT}/assets/style.css','w',encoding='utf-8').write(css.strip()+'\n'+EXTRA)
defs=re.search(r'<svg width="0" height="0".*?</svg>',home,re.S).group(0)

# ---------- home: usar CSS externo, sectores enlazados, pie con hubs ----------
home=home.replace(m.group(0),'<link rel="stylesheet" href="/assets/style.css">')
def _thumb(key):
    src=f'{OUT}/assets/img/{key}.jpg'
    if not os.path.exists(src): return None
    from PIL import Image
    os.makedirs(f'{OUT}/assets/img/t',exist_ok=True)
    Image.open(src).resize((600,450),Image.LANCZOS).save(f'{OUT}/assets/img/t/{key}.jpg',quality=78,optimize=True,progressive=True)
    return f'/assets/img/t/{key}.jpg'
def _ex(path,key,name,lead,tag):
    t=_thumb(key)
    if t: img=f'<span class="ex-img photo"><img src="{t}" width="600" height="450" loading="lazy" alt="{E(PHOTO_ALT.get(key,name))}"><span class="badge">{scenes.S(key,ACC[key])}</span></span>'
    else: img=f'<span class="ex-img">{scenes.S(key,ACC[key])}</span>'
    return f'<a class="sector ex" href="{path}">{img}<span class="ex-tag">{tag}</span><h3>{E(name)}</h3><p>{E(lead.split(".")[0])}.</p><span class="more">Ver el ejemplo →</span></a>\n      '
sec_cards=''.join(_ex(f'/sectores/{k}/',k,v["name"],v["lead"],'Sector') for k,v in SECTORS.items())+''.join(_ex(f'/nichos/{k}/',k,v["name"],v["lead"],'Nicho') for k,v in NICHES.items())
home=home.replace('<span class="eyebrow">Sectores</span>\n      <h2>Negocios para los que funciona bien</h2>','<span class="eyebrow">Ejemplos por sector y nicho</span>\n      <h2>Así se plantea la web de cada negocio</h2>\n      <p class="lead" style="margin-top:12px">Cada ejemplo muestra cómo se organizaría la web de ese tipo de negocio, qué piezas lleva y qué cuidar. Son planteamientos de ejemplo, no trabajos de clientes reales.</p>')
home=re.sub(r'(<div class="sectors">\s*).*?(\s*</div>\s*</div>\s*</section>)',lambda mm:mm.group(1)+sec_cards.rstrip()+mm.group(2),home,count=1,flags=re.S)
svc_links=''.join(f'<li><a href="/servicios/{k}/">{E(v["short"])}</a></li>' for k,v in SERVICES.items())
home=re.sub(r'<div><h4>Servicios</h4><ul>.*?</ul></div>',f'<div><h4>Servicios</h4><ul>{svc_links}</ul></div>',home,count=1,flags=re.S)
sec_links=''.join(f'<li><a href="/sectores/{k}/">{E(v["name"].split(",")[0])}</a></li>' for k,v in SECTORS.items())
home=re.sub(r'<div><h4>Compañía</h4><ul>.*?</ul></div>',f'<div><h4>Sectores</h4><ul>{sec_links}</ul></div>',home,count=1,flags=re.S)
home=home.replace('<a href="#proceso">Proceso</a>','<a href="/que-hacemos/">Qué hacemos</a>').replace('<a href="#servicios">Servicios</a>','<a href="/servicios/">Servicios</a>').replace('<a href="#sectores">Sectores</a>','<a href="/sectores/">Sectores</a>')
home=home.replace('<div><h4>Contacto</h4><ul><li><a href="#contacto">Pide tu web</a></li></ul></div>','<div><h4>Contacto</h4><ul><li><a href="/que-hacemos/">Qué hacemos y qué no</a></li><li><a href="#contacto">Pide tu web</a></li></ul></div>')
open(f'{OUT}/index.html','w',encoding='utf-8').write(home)

# ---------- plantilla ----------
def head(title,desc,path,ld):
    assert len(title)<=60,(len(title),title); assert len(desc)<=160,(len(desc),desc)
    url=f'{D}{path}'
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="author" content="Juan Peco">
<meta name="description" content="{E(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#0F172A">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/icon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="VUELCOS">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{D}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="VUELCOS, webs hechas con IA para tu negocio">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{D}/og-image.png">
<script type="application/ld+json">
{json.dumps(ld,ensure_ascii=False,indent=1)}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Schibsted+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{defs}
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="/" aria-label="VUELCOS, inicio"><svg viewBox="0 0 400 252" role="img" aria-hidden="true"><use href="#logo"/></svg></a>
    <nav class="nav" aria-label="Principal">
      <a href="/servicios/">Servicios</a>
      <a href="/sectores/">Sectores</a>
      <a href="/que-hacemos/">Qué hacemos</a>
      <a class="btn btn-primary" href="/#contacto">Pide tu web</a>
    </nav>
  </div>
</header>
<main id="contenido">
'''
def foot():
    return f'''</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="brand" href="/" aria-label="VUELCOS, inicio"><svg viewBox="0 0 400 252" role="img" aria-hidden="true" style="height:64px"><use href="#logo"/></svg></a>
        <p style="margin-top:14px;max-width:34ch;font-size:15px">Webs hechas con inteligencia artificial para negocios que quieren estar en línea sin complicarse.</p>
      </div>
      <div><h4>Servicios</h4><ul>{svc_links}</ul></div>
      <div><h4>Sectores</h4><ul>{sec_links}</ul></div>
      <div><h4>Contacto</h4><ul><li><a href="/que-hacemos/">Qué hacemos y qué no</a></li><li><a href="/#contacto">Pide tu web</a></li></ul></div>
    </div>
    <p class="legal">© 2026 VUELCOS. Aviso legal, política de privacidad y cookies: pendientes de publicar antes de salir en línea.</p>
  </div>
</footer>
</body>
</html>
'''
def crumbs(items):
    lis=''.join((f'<li><a href="{u}">{E(n)}</a></li>' if u else f'<li aria-current="page">{E(n)}</li>') for n,u in items)
    return f'<nav class="crumbs" aria-label="Migas de pan"><div class="wrap"><ol>{lis}</ol></div></nav>'
def bc_ld(items,path):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":D+(u or path)} for i,(n,u) in enumerate(items)]}
def cta(label="Pide tu web"):
    return f'<div class="cta-row"><a class="btn btn-primary" href="/#contacto">{label}</a><a class="btn btn-ghost" href="/servicios/">Ver servicios y precios</a></div>'
def faq(items):
    return '<div class="faq">'+''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q,a in items)+'</div>'
def cards(items):
    return '<div class="grid g2">'+''.join(f'<article class="card"><h3>{E(t)}</h3><p>{E(p)}</p></article>' for t,p in items)+'</div>'
def ul(items): return '<ul>'+''.join(f'<li>{E(i)}</li>' for i in items)+'</ul>'
def price_html(v):
    a,b,c=v['price']; 
    return f'<div class="price">{a}<b>{E(b)}</b>{E(c)}</div>' if a else f'<div class="price ask"><b>{E(b)}</b></div>'
def write(path,html):
    d=f'{OUT}{path}'; os.makedirs(d,exist_ok=True); open(f'{d}index.html','w',encoding='utf-8').write(html)


# ---------- variedad visual por página ----------
def _cut(t,n=22):
    t=t.strip()
    return t if len(t)<=n else t[:n-1].rsplit(' ',1)[0]+'…'
def mock(key,name,labels,slug):
    c=ACC[key]; L=[_cut(x) for x in labels[:4]]+['']*4
    lay=sum(map(ord,key))%4
    top=f'<rect x="1" y="1" width="458" height="378" rx="10" fill="#fff" stroke="#CBD5E1" stroke-width="2"/><rect x="1" y="1" width="458" height="30" rx="10" fill="#E2E8F0"/><rect x="1" y="20" width="458" height="11" fill="#E2E8F0"/><circle cx="18" cy="16" r="4" fill="#94A3B8"/><circle cx="32" cy="16" r="4" fill="#94A3B8"/><circle cx="46" cy="16" r="4" fill="#94A3B8"/><rect x="66" y="8" width="250" height="16" rx="8" fill="#fff"/><text x="78" y="20" font-size="10" fill="#475569">tu-dominio.es/{E(slug)}</text><rect x="20" y="44" width="70" height="14" rx="3" fill="{c}"/>'
    nav=''.join(f'<rect x="{250+i*62}" y="48" width="48" height="6" rx="3" fill="#CBD5E1"/>' for i in range(3))
    def tile(x,y,w,h,t,dark=False):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{"#F1F5F9" if not dark else c}" stroke="#CBD5E1"/><rect x="{x+12}" y="{y+12}" width="22" height="22" rx="5" fill="{c if not dark else "#fff"}" opacity=".9"/><text x="{x+12}" y="{y+h-14}" font-size="12.5" font-weight="700" fill="{"#0F172A" if not dark else "#fff"}">{E(t)}</text>'
    hero=lambda x,y,w,h:f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c}"/><text x="{x+18}" y="{y+34}" font-size="15" font-weight="800" fill="#fff">{E(_cut(name,24))}</text><rect x="{x+18}" y="{y+46}" width="{w-90}" height="6" rx="3" fill="#fff" opacity=".7"/><rect x="{x+18}" y="{y+58}" width="{w-130}" height="6" rx="3" fill="#fff" opacity=".5"/><rect x="{x+18}" y="{y+h-36}" width="92" height="24" rx="4" fill="#fff"/><text x="{x+30}" y="{y+h-20}" font-size="11" font-weight="700" fill="{c}">Contactar</text>'
    if lay==0:
        b=hero(20,74,420,116)+tile(20,198,204,80,L[0])+tile(236,198,204,80,L[1])+tile(20,290,204,76,L[2])+tile(236,290,204,76,L[3])
    elif lay==1:
        b=''.join(tile(20,74+i*72,140,62,L[i]) for i in range(4))+hero(172,74,268,288)
    elif lay==2:
        b=hero(20,74,420,100)+''.join(tile(20+i*142,184,134,92,L[i]) for i in range(3))+f'<rect x="20" y="290" width="420" height="72" rx="6" fill="#0F172A"/><text x="36" y="322" font-size="13" font-weight="700" fill="#fff">{E(_cut(L[3],34))}</text><rect x="36" y="334" width="160" height="6" rx="3" fill="#fff" opacity=".5"/>'
    else:
        b=tile(20,74,204,130,L[0],True)+hero(236,74,204,130)+tile(20,216,204,70,L[1])+tile(236,216,204,70,L[2])+f'<rect x="20" y="298" width="420" height="64" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/><text x="36" y="326" font-size="12.5" font-weight="700" fill="#0F172A">{E(L[3])}</text><rect x="36" y="338" width="200" height="6" rx="3" fill="#CBD5E1"/>'
    return f'<figure class="mock"><svg viewBox="0 0 460 380" role="img" aria-label="Esquema orientativo de cómo se organizaría esta web">{top}{nav}{b}</svg><figcaption>Esquema orientativo con las piezas de esta página. No es un trabajo real.</figcaption></figure>'
def phero(key,eyebrow,h1,lead,labels,slug,name):
    img=f'{OUT}/assets/img/{key}.jpg'
    if os.path.exists(img):
        fig=f'<figure class="scene photo"><img src="/assets/img/{key}.jpg" width="1200" height="900" alt="{E(PHOTO_ALT.get(key,name))}" fetchpriority="high"><span class="badge">{scenes.S(key,ACC[key])}</span></figure>'
    else:
        fig=f'<figure class="scene">{scenes.S(key,ACC[key])}</figure>'
    return f'<section class="phero"><div class="wrap phero-grid"><div><span class="eyebrow">{E(eyebrow)}</span><h1>{E(h1)}</h1><p class="lead">{E(lead)}</p>{cta()}</div>{fig}</div></section>'
def split(inner,key,labels,slug,name):
    return f'<div class="split"><div>{inner}</div>{mock(key,name,labels,slug)}</div>'
def numbered(items):
    return '<ol class="steps">'+''.join(f'<li><h3>{E(t)}</h3><p>{E(p)}</p></li>' for t,p in items)+'</ol>'
def checks(items):
    return '<ul class="checks">'+''.join(f'<li><b>{E(t)}</b><span>{E(p)}</span></li>' for t,p in items)+'</ul>'
def accord(items):
    return '<div class="faq acc">'+''.join(f'<details{" open" if i==0 else ""}><summary>{E(t)}</summary><p>{E(p)}</p></details>' for i,(t,p) in enumerate(items))+'</div>'
def journey(items):
    return '<div class="journey">'+''.join(f'<article><span class="n">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(p)}</p></article>' for i,(t,p) in enumerate(items))+'</div>'
def themed(h,key):
    return h.replace('<body>',f'<body style="--acc:{ACC[key]}">',1)

urls=['/']
def niche_rel(sk):
    ns=[(n,v) for n,v in NICHES.items() if v['parent']==sk]
    if not ns: return ''
    return '<section class="tight"><div class="wrap"><h3 style="margin-bottom:12px">Nichos de este sector</h3><div class="rel">'+''.join(f'<a href="/nichos/{n}/">{E(v["name"])}</a>' for n,v in ns)+'</div></div></section>'

def svc_card(k,page=None):
    v=SERVICES[k]; t=WHY.get((page,k)) or v["lead"].split(".")[0]+"."; return f'<article class="card"><h3><a href="/servicios/{k}/">{E(v["name"])}</a></h3><p>{E(t)}</p>{price_html(v)}</article>'

# ---------- servicios ----------
for k,v in SERVICES.items():
    path=f'/servicios/{k}/'; urls.append(path)
    items=[("Inicio","/"),("Servicios","/servicios/"),(v['name'],None)]
    svc={"@type":"Service","name":v['name'],"description":v['desc'],"provider":{"@type":"Organization","name":"VUELCOS","url":D+"/"},"areaServed":"ES","url":D+path}
    if v['pn']: svc["offers"]={"@type":"Offer","priceSpecification":{"@type":"PriceSpecification","minPrice":v['pn'],"priceCurrency":"EUR","valueAddedTaxIncluded":False}}
    ld={"@context":"https://schema.org","@graph":[svc,bc_ld(items,path)]}
    rel_sec=[s for s,sv in SECTORS.items() if k in sv['services']]
    rel=''.join(f'<a href="/sectores/{s}/">{E(SECTORS[s]["name"])}</a>' for s in rel_sec)
    others=''.join(f'<a href="/servicios/{o}/">{E(SERVICES[o]["short"])}</a>' for o in SERVICES if o!=k)
    h=head(v['title'],v['desc'],path,ld)+crumbs(items)+f'''
{phero(k,'Servicio',v['h1'],v['lead'],[t for t,_ in v['incl']],'servicios/'+k+'/',v['name'])}
<section class="tight band"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Para quién es</span><h2>Encaja si…</h2></div>
  <div class="grid g3">{''.join(f'<article class="card"><p>{E(x)}</p></article>' for x in v['who'])}</div>
</div></section>
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Qué incluye</span><h2>Lo que recibes</h2></div>
  {split(numbered(v['incl']),k,[t for t,_ in v['incl']],'servicios/'+k+'/',v['name'])}
</div></section>
<section class="tight"><div class="wrap"><div class="lists">
  <div class="box"><h3>Lo que no incluye</h3>{ul(v['notin'])}</div>
  <div class="box"><h3>Qué necesito de ti</h3>{ul(v['need'])}</div>
</div></div></section>
<section class="tight"><div class="wrap">
  <div class="callout"><h3>{E(v['name'])}</h3>{price_html(v)}<p class="muted" style="margin-top:12px">Alcance, plazo y precio, por escrito antes de empezar. Dominio y alojamiento se presupuestan aparte. El IVA se indica en la propuesta según tu país y si contratas como empresa o como particular.</p><div style="margin-top:16px">{cta("Pide tu presupuesto")}</div></div>
</div></section>
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Preguntas</span><h2>Antes de decidir</h2></div>
  {faq(v['faq'])}
</div></section>
<section class="tight"><div class="wrap">
  {('<h3 style="margin-bottom:12px">Sectores donde más encaja</h3><div class="rel" style="margin-bottom:28px">'+rel+'</div>') if rel else ''}
  <h3 style="margin-bottom:12px">Otros servicios</h3><div class="rel">{others}</div>
</div></section>
'''+foot()
    write(path,themed(h,k))

# ---------- sectores ----------
for k,v in SECTORS.items():
    path=f'/sectores/{k}/'; urls.append(path)
    items=[("Inicio","/"),("Sectores","/sectores/"),(v['name'],None)]
    ld={"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":D+path+"#page","url":D+path,"name":v['title'],"description":v['desc'],"inLanguage":"es","isPartOf":{"@type":"WebSite","name":"VUELCOS","url":D+"/"}},bc_ld(items,path)]}
    svcs=''.join(svc_card(s,k) for s in v['services'])
    others=''.join(f'<a href="/sectores/{o}/">{E(SECTORS[o]["name"])}</a>' for o in SECTORS if o!=k)
    h=head(v['title'],v['desc'],path,ld)+crumbs(items)+f'''
{phero(k,v['name'],v['h1'],v['lead'],[t for t,_ in v['must']],'sectores/'+k+'/',v['name'])}
<section class="tight band"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Quién llega a tu web</span><h2>Qué busca tu cliente</h2></div>
  {journey(v['visitors'])}
</div></section>
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Qué tiene que tener</span><h2>La web, pieza a pieza</h2></div>
  {split(checks(v['must']),k,[t for t,_ in v['must']],'sectores/'+k+'/',v['name'])}
</div></section>
<section class="tight"><div class="wrap"><div class="lists">
  <div class="box"><h3>Con qué cuidado se hace</h3>{ul(v['care'])}</div>
  <div class="box"><h3>Qué necesito de ti</h3>{ul(v['need'])}</div>
</div></div></section>
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Servicios que encajan</span><h2>Por dónde empezar</h2></div>
  <div class="grid g3">{svcs}</div>
  <p class="pricenote" style="color:var(--slate)">Precios «desde» sin IVA; el punto de partida, no el precio final. Alcance y precio por escrito antes de empezar.</p>
</div></section>
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Preguntas</span><h2>Antes de decidir</h2></div>
  {faq(v['faq'])}
</div></section>
{niche_rel(k)}<section class="tight"><div class="wrap"><h3 style="margin-bottom:12px">Otros sectores</h3><div class="rel">{others}</div></div></section>
'''+foot()
    write(path,themed(h,k))

# ---------- hubs ----------
def hub(path,name,title,desc,h1,lead,cardsx):
    items=[("Inicio","/"),(name,None)]; urls.append(path)
    ld={"@context":"https://schema.org","@graph":[{"@type":"CollectionPage","url":D+path,"name":title,"description":desc,"inLanguage":"es"},bc_ld(items,path)]}
    h=head(title,desc,path,ld)+crumbs(items)+f'''
<section class="phero"><div class="wrap"><span class="eyebrow">{E(name)}</span><h1>{E(h1)}</h1><p class="lead">{E(lead)}</p></div></section>
<section class="tight"><div class="wrap">{cardsx}</div></section>
<section class="tight band"><div class="wrap"><div class="sec-head"><h2>¿No ves tu caso?</h2><p>Cuéntalo en el formulario. Si no encaja, te lo digo antes de que gastes nada.</p></div>{cta()}</div></section>
'''+foot()
    write(path,h)
hub('/servicios/','Servicios',"Servicios y precios de diseño web con IA | VUELCOS","Landing desde 300 €, web de negocio desde 800 €, tienda online desde 1.200 €, reservas, textos y SEO, y mantenimiento. Precios sin IVA.","Qué hacemos y cuánto cuesta","Seis servicios con alcance y precio por escrito antes de empezar. Los «desde» no incluyen IVA.",'<div class="grid g3">'+''.join(svc_card(k) for k in SERVICES)+'</div>')
hub('/sectores/','Sectores',"Webs para abogados, clínicas, hostelería y más | VUELCOS","Webs pensadas para abogados, clínicas, restaurantes y hoteles, inmobiliarias, reformas y oficios, y centros de estética. Desde 800 € sin IVA.","Webs pensadas para tu sector","Cada sector tiene dudas, normas y búsquedas distintas. Estas son las páginas que hemos trabajado primero.",'<div class="sectors">'+''.join(f'<a class="sector" href="/sectores/{k}/"><h3>{E(v["name"])}</h3><p>{E(v["lead"].split(".")[0])}.</p><span class="more">Ver cómo lo hacemos →</span></a>' for k,v in SECTORS.items())+'</div><h2 style="margin:56px 0 24px;font-size:clamp(30px,4.4vw,48px)">Nichos con página propia</h2><div class="sectors">'+''.join(f'<a class="sector" href="/nichos/{k}/"><h3>{E(v["name"])}</h3><p>{E(v["lead"].split(".")[0])}.</p><span class="more">Ver cómo lo hacemos →</span></a>' for k,v in NICHES.items())+'</div>')


# ---------- qué hacemos ----------
def honest():
    path='/que-hacemos/'; urls.append(path)
    items=[("Inicio","/"),("Qué hacemos y qué no",None)]
    t="Qué hacemos y qué no hacemos | VUELCOS"; d="Sin letra pequeña: qué entregamos (webs en HTML, textos, logos sencillos), qué no (WordPress, apps, garantías de posición) y cómo usamos la IA."
    ld={"@context":"https://schema.org","@graph":[{"@type":"WebPage","url":D+path,"name":t,"description":d,"inLanguage":"es"},bc_ld(items,path)]}
    si=["Webs en HTML estático: las escribimos, las probamos en local y te las entregamos listas para publicar.","Maquetamos los textos que tú nos pasas. Son tu responsabilidad; si prefieres que los redactemos nosotros, se presupuesta aparte.","Logos sencillos en vectorial (SVG y PNG), con favicon e imagen para redes, si los necesitas. Se cobran aparte si se piden por separado o no figuran en el precio de tu propuesta. No es identidad corporativa completa.","SEO técnico: títulos, descripciones, datos estructurados, mapa del sitio y velocidad.","Guía para publicar la web de forma gratuita o barata y para registrar tu dominio.","Alcance, plazo y precio por escrito antes de empezar."]
    no=["No hacemos WordPress ni otros gestores de contenido. Si lo necesitas, no es esto.","No programamos aplicaciones, ni backends a medida, ni integraciones con tu software de gestión sin valorarlas antes y decírtelo.","No garantizamos posiciones ni plazos en Google. Nadie puede hacerlo con honestidad.","No hacemos fotografía ni vídeo. Usamos tus fotos; si no tienes, te lo decimos antes de poner imágenes genéricas.","No gestionamos redes sociales ni campañas de anuncios.","No damos asesoramiento jurídico, fiscal ni sanitario: los textos legales y la publicidad regulada los revisas tú con tu gestor o tu colegio profesional.","No compramos enlaces ni inventamos reseñas."]
    ia=["La IA es la herramienta con la que trabajamos: nos ahorra tiempo en la producción.","No inventamos datos, cifras ni casos: si algo no se puede comprobar, no se escribe.","Los logos e imágenes se hacen con formas vectoriales propias; no copiamos marcas ni personajes de otros."]
    terc=["Dominio y alojamiento: los contratas tú, a tu nombre. Su coste es aparte.","Reservas, pagos y cuotas de las herramientas que se integren: los cobra cada proveedor.","Tipografías: se cargan desde Google Fonts."]
    h=head(t,d,path,ld)+crumbs(items)+f'''
<section class="phero"><div class="wrap"><span class="eyebrow">Sin letra pequeña</span><h1>Qué hacemos y qué no</h1><p class="lead">Si algo no lo podemos entregar, no lo ofrecemos. Esta página es el compromiso de que lo que ves en la web es lo que recibes.</p>{cta()}</div></section>
<section class="tight"><div class="wrap"><div class="lists"><div class="box"><h3>Lo que sí hacemos</h3>{ul(si)}</div><div class="box"><h3>Lo que no hacemos</h3>{ul(no)}</div></div></div></section>
<section class="tight"><div class="wrap"><div class="lists"><div class="box"><h3>Cómo usamos la IA</h3>{ul(ia)}</div><div class="box"><h3>Lo que depende de terceros</h3>{ul(terc)}</div></div></div></section>
<section class="tight band"><div class="wrap"><div class="sec-head"><h2>¿Dudas sobre si encaja?</h2><p>Cuéntanos tu caso. Si no es para nosotros, te lo decimos antes de que gastes nada.</p></div>{cta()}</div></section>
'''+foot()
    write(path,h)
honest()


# ---------- nichos ----------
for k,v in NICHES.items():
    path=f'/nichos/{k}/'; urls.append(path)
    items=[("Inicio","/"),("Sectores","/sectores/")]
    if v['parent']: items.append((SECTORS[v['parent']]['name'],f'/sectores/{v["parent"]}/'))
    items.append((v['name'],None))
    ld={"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":D+path+"#page","url":D+path,"name":v['title'],"description":v['desc'],"inLanguage":"es","isPartOf":{"@type":"WebSite","name":"VUELCOS","url":D+"/"}},bc_ld(items,path)]}
    svcs=''.join(svc_card(x,k) for x in v['services'])
    sibs=[(n,w) for n,w in NICHES.items() if n!=k and w['parent']==v['parent'] and v['parent']]
    rel=''.join(f'<a href="/nichos/{n}/">{E(w["name"])}</a>' for n,w in sibs)
    if v['parent']: rel+=f'<a href="/sectores/{v["parent"]}/">Sector: {E(SECTORS[v["parent"]]["name"])}</a>'
    else: rel+='<a href="/sectores/">Todos los sectores</a>'
    h=head(v['title'],v['desc'],path,ld)+crumbs(items)+f'''
{phero(k,v['name'],v['h1'],v['lead'],[t for t,_ in v['must']],'nichos/'+k+'/',v['name'])}
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Qué tiene que tener</span><h2>La web, pieza a pieza</h2></div>
  {split(accord(v['must']),k,[t for t,_ in v['must']],'nichos/'+k+'/',v['name'])}
</div></section>
<section class="tight band"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Quién llega a tu web</span><h2>Qué busca tu cliente</h2></div>
  {journey(v['visitors'])}
</div></section>
<section class="tight"><div class="wrap"><div class="lists">
  <div class="box"><h3>Con qué cuidado se hace</h3>{ul(v['care'])}</div>
  <div class="box"><h3>Qué necesito de ti</h3>{ul(v['need'])}</div>
</div></div></section>
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Servicios que encajan</span><h2>Por dónde empezar</h2></div>
  <div class="grid g3">{svcs}</div>
  <p class="pricenote" style="color:var(--slate)">Precios «desde» sin IVA; el punto de partida, no el precio final. Los textos los aportas tú; redactarlos o hacer un logo se presupuesta aparte.</p>
</div></section>
<section class="tight"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Preguntas</span><h2>Antes de decidir</h2></div>
  {faq(v['faq'])}
</div></section>
<section class="tight"><div class="wrap"><h3 style="margin-bottom:12px">Relacionado</h3><div class="rel">{rel}</div></div></section>
'''+foot()
    write(path,themed(h,k))

# ---------- sitemap ----------
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url>\n    <loc>{D}{u}</loc>\n    <lastmod>{LAST}</lastmod>\n  </url>\n' for u in urls)+'</urlset>\n'
open(f'{OUT}/sitemap.xml','w',encoding='utf-8').write(sm)
print(len(urls),'urls')

# ---------- posproceso: fuentes propias, legales, 404, contacto ----------
import re,shutil,glob,legal
os.makedirs(f'{OUT}/assets/fonts',exist_ok=True)
for f in glob.glob('/home/claude/build/fonts/*.woff2'): shutil.copy(f,f'{OUT}/assets/fonts/')
FF=''.join(f"@font-face{{font-family:'{fam}';font-weight:{w};font-display:swap;src:url(/assets/fonts/{fn}-latin-{w}-normal.woff2) format('woff2')}}" for fam,fn,ws in (('Big Shoulders Display','big-shoulders-display',(700,800,900)),('Schibsted Grotesk','schibsted-grotesk',(400,500,600,700))) for w in ws)
css=open(f'{OUT}/assets/style.css',encoding='utf-8').read()
FIX='.band .step p{color:#cbd5e1}footer .fh{margin:0 0 12px;font:700 13px/1 var(--body);letter-spacing:.12em;text-transform:uppercase;color:var(--paper)}'
if '/assets/fonts/' not in css: open(f'{OUT}/assets/style.css','w',encoding='utf-8').write(FF+'\n'+css+'\n'+FIX)

# páginas legales y 404
LEG=legal.pages(); lp=[]
for path,title,desc,h1,body in LEG:
    items=[('Inicio','/'),(h1,None)]
    ld={"@context":"https://schema.org","@graph":[{"@type":"WebPage","url":D+path,"name":title,"inLanguage":"es"}]}
    h=head(title,desc,path,ld).replace('index,follow,max-image-preview:large','noindex,follow')
    h+=f'<section class="tight"><div class="wrap" style="max-width:760px">{crumbs(items)}<h1>{h1}</h1>{legal.banner()}{body}</div></section>'+foot()
    write(path,h)
h=head('Página no encontrada — VUELCOS','La página que buscas no existe o ha cambiado de dirección. Vuelve al inicio de VUELCOS.','/404.html',{"@context":"https://schema.org","@type":"WebPage","name":"Página no encontrada"}).replace('index,follow,max-image-preview:large','noindex,follow')
h+='<section class="tight"><div class="wrap" style="max-width:760px"><h1>Esta página no existe</h1><p>Puede que la dirección esté mal escrita o que la página haya cambiado de sitio.</p><p><a class="btn btn-primary" href="/">Volver al inicio</a> <a class="btn" href="/servicios/">Ver servicios</a></p></div></section>'+foot()
open(f'{OUT}/404.html','w',encoding='utf-8').write(h)

LEGAL_LINE='<p class="legal">© 2026 VUELCOS. <a href="/aviso-legal/">Aviso legal</a> · <a href="/privacidad/">Política de privacidad</a> · <a href="/cookies/">Política de cookies</a></p>'
WF_KEY=os.environ.get('VUELCOS_WF_KEY','')
email=legal.CFG['email']; email='' if 'PENDIENTE' in email else email
for f in glob.glob(f'{OUT}/**/*.html',recursive=True):
    x=open(f,encoding='utf-8').read(); o=x
    x=re.sub(r'<link rel="preconnect" href="https://fonts\.g[^>]*>\s*','',x)
    x=re.sub(r'<link href="https://fonts\.googleapis\.com[^>]*>\s*','',x)
    x=re.sub(r'<p class="legal">.*?</p>',LEGAL_LINE,x,flags=re.S)
    x=x.replace('var CONTACT_EMAIL = "";','var CONTACT_EMAIL = "%s";'%email)
    if 'id="dato"' in x and WF_KEY:
        x=x.replace('<p class="err" id="err3" role="alert"></p>','<div class="field" style="display:flex;gap:10px;align-items:flex-start"><input type="checkbox" id="consent" style="margin-top:5px;width:auto"><label for="consent" style="font-size:14px">He leído la <a href="/privacidad/">política de privacidad</a> y acepto que se usen mis datos para responder a mi consulta.</label></div>\n        <input type="checkbox" name="botcheck" id="botcheck" style="display:none" tabindex="-1" autocomplete="off">\n        <p class="err" id="err3" role="alert"></p>')
        x=x.replace('var CONTACT_EMAIL = "%s";'%email,'var CONTACT_EMAIL = "%s";\n  var WF_KEY = "%s";'%(email,WF_KEY))
        x=x.replace('    summary.textContent = txt;\n','''    if (!document.getElementById("consent").checked) { setErr(3, "Marca la casilla de la política de privacidad para poder enviar el mensaje."); return; }
    if (document.getElementById("botcheck").checked) return;
    var payload = {access_key: WF_KEY, subject: "Nuevo contacto desde la web VUELCOS", from_name: "Web VUELCOS", name: val("nombre"), message: txt, botcheck: ""};
    if (/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(val("dato"))) payload.email = val("dato");
    next.disabled = true; next.textContent = "Enviando…";
    var done = function(ok){
      next.disabled = false;
      summary.textContent = txt;
      note.textContent = ok
        ? "Mensaje enviado. Te responderemos lo antes posible. Esta es la copia de lo que has enviado."
        : "No se ha podido enviar el mensaje. Copia el texto y escríbenos a " + CONTACT_EMAIL + ".";
      steps.forEach(function(s){ s.hidden = true; });
      document.querySelector(".form-nav").hidden = true;
      document.querySelector(".progress").hidden = true;
      stepno.hidden = true;
      result.hidden = false;
    };
    fetch("https://api.web3forms.com/submit", {method: "POST", headers: {"Content-Type": "application/json", "Accept": "application/json"}, body: JSON.stringify(payload)})
      .then(function(r){ return r.json(); })
      .then(function(d){ done(!!(d && d.success)); })
      .catch(function(){ done(false); });
    return;
    summary.textContent = txt;
''',1)
    i=x.find('<footer')
    if i>=0: x=x[:i]+x[i:].replace('<h4>','<p class="fh">').replace('</h4>','</p>')
    if x!=o: open(f,'w',encoding='utf-8').write(x)
p=legal.pendientes()
print('PENDIENTES en legales:',p if p else 'ninguno','| dominio:',D)
