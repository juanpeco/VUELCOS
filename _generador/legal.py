# Borradores legales de VUELCOS. Se generan con los datos de la persona titular (variables de entorno).
# Todo lo que no se conoce queda como [PENDIENTE: ...] y la página muestra un aviso de borrador.
import os
CFG={
 'nombre':os.environ.get('VUELCOS_NOMBRE','Juan Antonio Peco Celdrán'),
 'nif':os.environ.get('VUELCOS_NIF','[PENDIENTE: NIF]'),
 'dir':os.environ.get('VUELCOS_DIR','[PENDIENTE: domicilio profesional]'),
 'email':os.environ.get('VUELCOS_EMAIL','[PENDIENTE: correo de contacto]'),
 'reg':os.environ.get('VUELCOS_REG','[PENDIENTE: datos de alta o inscripción, si procede]'),
 'correo_prov':os.environ.get('VUELCOS_CORREO_PROV','[PENDIENTE: proveedor de correo]'),
}
def pendientes(): return sorted({v for v in CFG.values() if 'PENDIENTE' in v})
def banner():
    p=pendientes()
    if not p: return ''
    return '<p class="callout" style="border-left:4px solid #d9232d;padding:12px 16px;background:#fff4f4"><strong>Borrador pendiente de revisión.</strong> Faltan datos del titular y la revisión de un gestor o abogado antes de publicar.</p>'
def pages():
    c=CFG
    aviso=f'''<h2>1. Titular del sitio web</h2>
<p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de los datos del titular:</p>
<ul><li>Titular: {c['nombre']}</li><li>NIF: {c['nif']}</li><li>Domicilio: {c['dir']}</li><li>Correo electrónico: {c['email']}</li><li>Datos de alta o inscripción: {c['reg']}</li></ul>
<h2>2. Actividad</h2>
<p>VUELCOS ofrece el diseño y la creación de páginas web para negocios, elaboradas con apoyo de herramientas de inteligencia artificial y revisadas por una persona. Los servicios, sus condiciones y sus precios orientativos se describen en este sitio; el presupuesto final se acuerda por escrito con cada cliente.</p>
<h2>3. Condiciones de uso</h2>
<p>El acceso y la navegación por este sitio son libres y gratuitos. Quien lo use se compromete a hacerlo conforme a la ley, la buena fe y el orden público, y a no dañar ni sobrecargar el sitio o sus servicios.</p>
<h2>4. Ejemplos por sector y nicho</h2>
<p>Las páginas de sectores y nichos, así como las tarjetas de ejemplos de la portada, describen planteamientos orientativos de cómo se estructuraría una web para ese tipo de negocio. No son trabajos reales realizados para clientes, y los esquemas e ilustraciones que los acompañan son representaciones orientativas.</p>
<h2>5. Propiedad intelectual</h2>
<p>Los textos, el diseño, las ilustraciones y la marca VUELCOS son de su titular, salvo las fotografías, que se utilizan conforme a las licencias de sus bancos de imágenes. Queda prohibida su reproducción o distribución sin autorización, salvo en los casos permitidos por la ley.</p>
<h2>6. Responsabilidad</h2>
<p>El titular procura que la información sea correcta y actual, pero no garantiza que esté libre de errores ni se responsabiliza de los daños derivados de un uso indebido del sitio. Los contenidos informativos sobre sectores (por ejemplo, sanitario, jurídico o turístico) no sustituyen el asesoramiento profesional ni la normativa aplicable a cada negocio.</p>
<h2>7. Enlaces</h2>
<p>Este sitio puede enlazar a páginas de terceros. El titular no controla sus contenidos ni responde de ellos.</p>
<h2>8. Legislación aplicable</h2>
<p>Este aviso se rige por la legislación española. Para cualquier controversia serán competentes los juzgados y tribunales que correspondan conforme a la normativa aplicable, incluida la de protección de consumidores y usuarios.</p>'''
    priv=f'''<h2>1. Responsable del tratamiento</h2>
<ul><li>Responsable: {c['nombre']}</li><li>NIF: {c['nif']}</li><li>Domicilio: {c['dir']}</li><li>Correo electrónico: {c['email']}</li></ul>
<h2>2. Qué datos tratamos y cómo llegan</h2>
<p>Los datos llegan cuando rellenas el formulario de la portada y pulsas el botón de enviar, o cuando nos escribes por correo. Tratamos solo lo que nos hagas llegar: nombre, correo o teléfono, tipo de negocio y lo que cuentes de tu proyecto. Al enviar el formulario, tu navegador transmite esos datos al servicio de formularios Web3Forms, que nos los entrega por correo electrónico. No usamos esos datos para otra cosa.</p>
<h2>3. Finalidad y base jurídica</h2>
<p>Usamos esos datos para responder a tu consulta y, si lo solicitas, preparar un presupuesto. La base es la aplicación de medidas precontractuales a petición tuya (artículo 6.1.b del Reglamento (UE) 2016/679, RGPD). Si llegas a contratar, los trataremos para ejecutar el contrato y cumplir las obligaciones legales (fiscales y contables).</p>
<h2>4. Conservación</h2>
<p>Conservamos los datos mientras dure la relación y, después, durante los plazos exigidos por la ley. Si no llega a haber relación, los conservamos solo el tiempo necesario para atender tu consulta. [PENDIENTE: confirmar plazos con el gestor]</p>
<h2>5. Destinatarios</h2>
<p>No cedemos tus datos a terceros salvo obligación legal. Pueden acceder a ellos los proveedores que nos prestan servicios necesarios, como el servicio de formularios (Web3Forms), el de correo electrónico ({c['correo_prov']}) y el de alojamiento del sitio (Cloudflare). Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo; en ese caso se exigirán las garantías previstas en el RGPD. [PENDIENTE: confirmar con la documentación de cada proveedor dónde se tratan los datos, cuánto tiempo conserva Web3Forms los envíos y las garantías aplicables]</p>
<h2>6. Tus derechos</h2>
<p>Puedes ejercer los derechos de acceso, rectificación, supresión, oposición, limitación del tratamiento y portabilidad escribiendo a {c['email']}. Si consideras que no hemos tratado tus datos correctamente, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (www.aepd.es).</p>
<h2>7. Datos técnicos del servidor</h2>
<p>Como en cualquier sitio web, el servicio de alojamiento puede registrar datos técnicos de la conexión (por ejemplo, la dirección IP) para el funcionamiento y la seguridad del servicio. [PENDIENTE: confirmar qué registra el alojamiento elegido]</p>'''
    cook='''<h2>Qué usamos</h2>
<p>Este sitio no usa cookies propias ni de terceros, ni guarda información en tu dispositivo mediante almacenamiento local. Tampoco carga analítica, publicidad ni contenidos de otros sitios: las tipografías se sirven desde el propio sitio.</p>
<h2>Qué pasa si esto cambia</h2>
<p>Si en el futuro se añade analítica u otro servicio que use cookies o tecnologías similares, esta política se actualizará y se pedirá tu consentimiento cuando la ley lo exija (artículo 22.2 de la LSSI-CE).</p>
<h2>Cómo controlarlas en tu navegador</h2>
<p>Aunque no usamos cookies, puedes configurar tu navegador para bloquearlas o borrarlas en cualquier sitio. [PENDIENTE: tras publicar, comprobar en las cabeceras de respuesta que el alojamiento no establece cookies]</p>'''
    return [
     ('/aviso-legal/','Aviso legal — VUELCOS','Titular, condiciones de uso y responsabilidad del sitio web de VUELCOS.','Aviso legal',aviso),
     ('/privacidad/','Política de privacidad — VUELCOS','Cómo trata VUELCOS los datos que nos haces llegar al escribirnos, sus finalidades y tus derechos.','Política de privacidad',priv),
     ('/cookies/','Política de cookies — VUELCOS','Qué cookies y almacenamiento usa el sitio web de VUELCOS.','Política de cookies',cook)]
