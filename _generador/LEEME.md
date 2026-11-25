# Generador de la web VUELCOS

Copia de seguridad del código que genera la web (no se publica: está excluido en `.assetsignore`).

- `build.sh` ejecuta `seo.py` y después `site.py` (siempre en ese orden).
- Variables de entorno: `VUELCOS_DOMAIN`, `VUELCOS_EMAIL`, `VUELCOS_NOMBRE`, `VUELCOS_NIF`, `VUELCOS_DIR`, `VUELCOS_REG`, `VUELCOS_CORREO_PROV`, `VUELCOS_WF_KEY` (clave pública de Web3Forms).
- Los textos están en `content.py`, `content2.py` y `content3.py`. El registro de fuentes está en `VERIFICAR-TEXTOS.md`.
- Las rutas de salida están escritas para el entorno original (`/home/claude/sitio`); hay que ajustarlas si se ejecuta en otro sitio.
- No incluye las fotos originales: solo las ya procesadas, que están en `assets/img/`.
