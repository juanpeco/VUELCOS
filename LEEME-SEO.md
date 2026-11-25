# Paquete web VUELCOS: cómo publicarla para que Google la indexe

Contenido: index.html, robots.txt, sitemap.xml, favicon.ico, favicon.svg, icon-192.png, apple-touch-icon.png, og-image.png.

## 1. Pon tu dominio (obligatorio)
En todos los archivos aparece el marcador `https://TU-DOMINIO.es`. Sustitúyelo por tu dominio real con https:
    sed -i 's#https://TU-DOMINIO.es#https://tudominio.com#g' index.html robots.txt sitemap.xml
(O dime el dominio y lo hago yo.)

## 2. Sube todo a la RAÍZ del alojamiento, con HTTPS activo
La web debe abrirse en https://tudominio.com/ y los iconos en https://tudominio.com/favicon.ico, etc.

## 3. Google Search Console
- Añade la propiedad del dominio y verifícala.
- Envía https://tudominio.com/sitemap.xml
- En "Inspección de URL", pega la portada y pulsa "Solicitar indexación".

## 4. Comprueba antes de dar por buena la publicación
- Prueba de resultados enriquecidos de Google (datos estructurados).
- PageSpeed Insights (móvil).
- Que robots.txt abre en /robots.txt y no bloquea nada.

## 5. Pendiente de ti antes de salir
- Correo de destino del formulario (constante CONTACT_EMAIL en index.html).
- Aviso legal, privacidad y cookies.
- Si quieres posicionarte en una ciudad concreta: ficha de Google Business Profile y datos de contacto reales en la web.


## Despliegue gratuito (v2: sitio multipágina)
Estructura: `/`, `/servicios/` (+6), `/sectores/` (+6), `assets/style.css`, `/que-hacemos/`, `/nichos/` (+8), `sitemap.xml` (24 URLs).
1. Crea un repositorio en GitHub y sube el contenido de esta carpeta (en la raíz del repo, no la carpeta contenedora).
2. Cloudflare → Workers & Pages → Pages → Connect to Git → elige el repo. Sin comando de build; directorio de salida: `/`.
3. Dominio: añade el dominio en el proyecto (Custom domains). HTTPS se emite automáticamente.
4. Sustituye el marcador de dominio: `grep -rl TU-DOMINIO.es . | xargs sed -i 's#https://TU-DOMINIO.es#https://tudominio.com#g'`.
5. Search Console: envía `https://tudominio.com/sitemap.xml`.
Nota: GitHub Pages gratuito exige repo público y sus términos no permiten alojar un negocio comercial; por eso se recomienda Cloudflare Pages para servir la web y GitHub solo como repositorio.
Pendiente antes de publicar: CONTACT_EMAIL del formulario, páginas legales, y confirmar compromisos de los textos.

## Decisiones y pendientes (revisión final)
- Reglas aplicadas: logo y redacción de textos se presupuestan aparte; los textos los aporta el cliente; la IA es la herramienta de trabajo; no se ofrece WordPress.
- Pagos: enlaces de pago de Stripe (un enlace por producto); no hay carrito propio. Reservas: Cal.com, cada cliente con su cuenta propia (las condiciones de Cal.com restringen ofrecer el servicio a terceros desde tu cuenta; confírmalo por escrito con ellos).
- Probado: una reserva real en cal.com/vuelcos y su cancelación. NO probado: inserción en una página propia, pago con Stripe, integración con calendario.
- Revisar con gestor/colegio: textos de publicidad sanitaria, registro turístico, protección de datos en reservas, IVA en ventas a otros países.
- Antes de publicar: dominio real (sustituir TU-DOMINIO.es), CONTACT_EMAIL del formulario, aviso legal, privacidad y cookies, precio del logo y de la redacción de textos.


## Datos que faltan (sustituir antes de publicar)
Dominio:  grep -rl TU-DOMINIO.es . | xargs sed -i 's#https://TU-DOMINIO.es#https://tudominio.com#g'
Correo del formulario:  grep -rl 'var CONTACT_EMAIL = ""' . | xargs sed -i 's#var CONTACT_EMAIL = "";#var CONTACT_EMAIL = "hola@tudominio.com";#'
Legales: busca "[PENDIENTE" en aviso-legal, privacidad y cookies y sustituye cada marcador por el dato real. Al quitar el último marcador conviene retirar también el recuadro "Borrador pendiente de revisión" de cada página.
Hay 404.html (Cloudflare Pages la sirve sola). Tipografías incluidas en assets/fonts (no se carga nada de Google).
