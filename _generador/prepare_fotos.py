# Uso: python3 prepare_fotos.py CARPETA_ORIGEN   (archivos nombrados <clave>.jpg|png|webp, p.ej. dentistas.jpg)
import sys,os,glob
from PIL import Image,ImageOps
src=sys.argv[1]; dst='/home/claude/sitio/assets/img'; os.makedirs(dst,exist_ok=True)
for f in sorted(glob.glob(src+'/*')):
    k=os.path.splitext(os.path.basename(f))[0]
    im=ImageOps.exif_transpose(Image.open(f)).convert('RGB')
    im=ImageOps.fit(im,(1200,900),Image.LANCZOS)
    im.save(f'{dst}/{k}.jpg',quality=82,optimize=True,progressive=True)  # sin EXIF/XMP
    print('ok',k,os.path.getsize(f'{dst}/{k}.jpg')//1024,'KB')
