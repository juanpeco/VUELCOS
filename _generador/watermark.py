import math, sys
sys.path.insert(0, '/home/claude/build')
import gen
SC = 0.95
N = 150
th = math.radians(gen.TILT)
dx, dy = gen.HOLE_LOCAL[0]-gen.S_ORIGIN_LOCAL[0], gen.HOLE_LOCAL[1]-gen.S_ORIGIN_LOCAL[1]
rx = SC*(dx*math.cos(th)-dy*math.sin(th)); ry = SC*(dx*math.sin(th)+dy*math.cos(th))
cx, cy = 75, 82
hx, hy = cx+rx, cy+ry
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {N} {N}" width="{N}" height="{N}" role="img" aria-label="VUELCOS">
{gen.META}
<path id="hilo-halo" d="M{hx:.2f} 0V{hy:.2f}" fill="none" stroke="#FFFFFF" stroke-width="4.5"/>
<path id="hilo" d="M{hx:.2f} 0V{hy:.2f}" fill="none" stroke="#64748B" stroke-width="2.2"/>
<g id="s" transform="translate({cx} {cy}) scale({SC}) rotate({gen.TILT}) translate({-gen.S_ORIGIN_LOCAL[0]} {-gen.S_ORIGIN_LOCAL[1]})">
<path d="{gen.S_PATH}" fill="none" stroke="#FFFFFF" stroke-width="{gen.S_STROKE+5}"/>
<path d="{gen.S_PATH}" fill="none" stroke="{gen.RED}" stroke-width="{gen.S_STROKE}"/>
</g>
<circle id="agujero" cx="{hx:.2f}" cy="{hy:.2f}" r="3.8" fill="#FFFFFF"/>
</svg>
'''
open('/home/claude/deliver/vuelcos-marca-de-agua-youtube.svg','w',encoding='utf-8').write(svg)
