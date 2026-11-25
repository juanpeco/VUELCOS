import sys, os, re, json, shutil
sys.path.insert(0,'/home/claude/build')
import gen
OUT='/home/claude/sitio'; os.makedirs(OUT,exist_ok=True)
import os
D=os.environ.get('VUELCOS_DOMAIN','https://TU-DOMINIO.es').rstrip('/')
TITLE='Webs con IA para negocios, desde 300 € | VUELCOS'
DESC='Webs hechas con IA para negocios: landing desde 300 €, web de negocio desde 800 € y tienda online desde 1.200 € (sin IVA). Alcance y precio por escrito.'
assert len(TITLE)<=60, len(TITLE); assert len(DESC)<=160, len(DESC)

html=open('/home/claude/web/index.html',encoding='utf-8').read()
html=html.replace('<title>VUELCOS Webs con IA</title>',f'<title>{TITLE}</title>')
html=re.sub(r'<meta name="description"[^>]*>', f'<meta name="description" content="{DESC}">', html, count=1)

ld={"@context":"https://schema.org","@graph":[
 {"@type":"Organization","@id":f"{D}/#org","name":"VUELCOS","url":f"{D}/","logo":f"{D}/icon-192.png"},
 {"@type":"WebSite","@id":f"{D}/#web","url":f"{D}/","name":"VUELCOS","inLanguage":"es","publisher":{"@id":f"{D}/#org"}},
]}
for name,desc,price in [("Landing de una oferta","Una sola página con un único objetivo: que te escriban, reserven o compren.",300),
                        ("Web de negocio","Quién eres, qué haces y cómo contactarte, en tres a seis páginas.",800),
                        ("Tienda online sencilla","Para vender pocos productos con una experiencia de compra clara.",1200)]:
    ld["@graph"].append({"@type":"Service","name":name,"description":desc,"provider":{"@id":f"{D}/#org"},
      "offers":{"@type":"Offer","priceSpecification":{"@type":"PriceSpecification","minPrice":price,"priceCurrency":"EUR","valueAddedTaxIncluded":False}}})
ldjson=json.dumps(ld,ensure_ascii=False,indent=1)

seo=f'''<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{D}/">
<link rel="alternate" hreflang="es" href="{D}/">
<link rel="alternate" hreflang="x-default" href="{D}/">
<meta name="theme-color" content="#0F172A">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/icon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="VUELCOS">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{D}/">
<meta property="og:image" content="{D}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="VUELCOS, webs hechas con IA para tu negocio">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{D}/og-image.png">
<script type="application/ld+json">
{ldjson}
</script>
'''
html=html.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', seo+'<link rel="preconnect" href="https://fonts.googleapis.com">',1)
open(f'{OUT}/index.html','w',encoding='utf-8').write(html)

# robots + sitemap
open(f'{OUT}/robots.txt','w',encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {D}/sitemap.xml\n')
open(f'{OUT}/sitemap.xml','w',encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url>\n    <loc>{D}/</loc>\n    <lastmod>2026-11-24</lastmod>\n  </url>\n</urlset>\n')

# favicon svg
S=gen.S_PATH
fav=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" role="img" aria-label="VUELCOS">
{gen.META}
<rect width="64" height="64" rx="12" fill="#0F172A"/>
<g transform="rotate(12 32 32) translate(16.5 7) scale(.5)"><path d="{S}" fill="none" stroke="#EF4444" stroke-width="22"/></g>
</svg>
'''
open(f'{OUT}/favicon.svg','w',encoding='utf-8').write(fav)

# og-image svg
comp,(cw,ch),_o=gen.composition(gen.NAVY,gen.RED,tw=2.4)
s=1.55
og=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="VUELCOS, webs hechas con IA para tu negocio">
{gen.META}
<rect width="1200" height="630" fill="#F8FAFC"/>
<rect x="0" y="618" width="1200" height="12" fill="#DC2626"/>
<g transform="translate(295 52) scale({s})">
{comp}
</g>
<text x="600" y="520" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-weight="800" font-size="46" fill="#0F172A">Webs hechas con IA para tu negocio</text>
<text x="600" y="574" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-weight="500" font-size="30" fill="#475569">Desde 300 €, IVA no incluido. Alcance y precio por escrito.</text>
</svg>
'''
open('/home/claude/build/og.svg','w',encoding='utf-8').write(og)
print("ok", len(TITLE), len(DESC))
