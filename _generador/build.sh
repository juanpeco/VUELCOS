#!/bin/sh
# Uso: VUELCOS_DOMAIN=https://midominio.es VUELCOS_EMAIL=hola@midominio.es VUELCOS_NIF=... VUELCOS_DIR="..." ./build.sh
cd /home/claude/build && python3 seo.py && python3 site.py
