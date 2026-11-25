import sys, glob, re, unicodedata
from PIL import Image
BAD = [(0x200B,0x200F),(0x2028,0x202E),(0x2060,0x206F),(0xFEFF,0xFEFF),(0xE0000,0xE007F),(0xFE00,0xFE0F),(0x2000,0x200A),(0x202F,0x202F),(0x205F,0x205F),(0x3000,0x3000),(0x00AD,0x00AD),(0x00A0,0x00A0)]
def bad(c): return any(a<=ord(c)<=b for a,b in BAD)
for f in sorted(glob.glob(sys.argv[1]+'/*.svg')):
    t = open(f,encoding='utf-8').read()
    hits = [(i,hex(ord(c))) for i,c in enumerate(t) if bad(c)]
    nonascii = [c for c in t if ord(c)>127]
    meta = re.findall(r'<dc:(\w+)>([^<]*)</dc:\w+>', t)
    print(f"{f.split('/')[-1]}: unicode_problematico={len(hits)} no_ascii={len(nonascii)} metadatos={meta} <text>={'<text' in t} <title>={'<title' in t}")
for f in sorted(glob.glob(sys.argv[1]+'/*.png')):
    im = Image.open(f)
    print(f"{f.split('/')[-1]}: {im.size} info={ {k:(v if k!='icc_profile' else 'ICC') for k,v in im.info.items()} } exif={bool(im.getexif())}")
