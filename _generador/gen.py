#!/usr/bin/env python3
"""Genera las piezas SVG de la marca VUELCOS. Letras trazadas como paths (sin fuentes)."""
import math, sys, os

NAVY = "#0F172A"
BG = "#F8FAFC"
RED = "#DC2626"
RED_DARK_BG = "#EF4444"

# Letras en una rejilla de 100 de alto (altura de versal). Verticales 22, horizontales 20.
LETTERS = {
    "V": (70, "M0 0H23L35 68L47 0H70L46 100H24Z"),
    "U": (62, "M0 0H22V68Q22 80 31 80Q40 80 40 68V0H62V70Q62 100 31 100Q0 100 0 70Z"),
    "E": (50, "M0 0H50V20H22V39H46V59H22V80H50V100H0Z"),
    "L": (48, "M0 0H22V80H48V100H0Z"),
    "C": (62, "M62 36H40V30Q40 20 31 20Q22 20 22 30V70Q22 80 31 80Q40 80 40 70V64H62V70Q62 100 31 100Q0 100 0 70V30Q0 0 31 0Q62 0 62 30Z"),
    "O": (62, "M31 0Q62 0 62 30V70Q62 100 31 100Q0 100 0 70V30Q0 0 31 0ZM31 20Q40 20 40 30V70Q40 80 31 80Q22 80 22 70V30Q22 20 31 20Z"),
}
WORD = "VUELCO"          # + "S" colgando aparte
GAP = 8
THREAD_W = 3.5           # grosor del hilo en unidades de rejilla
TILT = 12                # inclinación de la S (grados)
S_PATH = ("M52 26C52 16 43 10 31 10C19 10 10 16 10 27C10 38 21 42 31 50"
          "C41 58 52 62 52 73C52 84 43 90 31 90C19 90 10 84 10 74")
S_STROKE = 20
HOLE_LOCAL = (31, 8)     # punto de enganche en coordenadas locales de la S
S_ORIGIN_LOCAL = (31, 50)  # centro local de la S

META = ('<metadata><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/"><rdf:Description>'
        '<dc:creator>Juan Peco</dc:creator></rdf:Description></rdf:RDF></metadata>')


def layout():
    """Devuelve (letras[(ch, x, path)], ancho_texto, x_centro_O)."""
    x = 0
    out = []
    for ch in WORD:
        w, p = LETTERS[ch]
        out.append((ch, x, p))
        x += w + GAP
    width = x - GAP
    o_x = [l[1] for l in out if l[0] == "O"][0]
    return out, width, o_x + LETTERS["O"][0] / 2


def composition(ink, accent, hole_y=150, with_text=True, thread="#64748B", tw=1.7, hole="#FFFFFF"):
    """Grupo en coordenadas de rejilla. Devuelve (svg, bbox(w,h))."""
    letters, width, o_cx = layout()
    th = math.radians(TILT)
    # La S rota TILT grados; calculamos su origen para que el punto de enganche caiga en (o_cx, hole_y)
    dx, dy = HOLE_LOCAL[0] - S_ORIGIN_LOCAL[0], HOLE_LOCAL[1] - S_ORIGIN_LOCAL[1]
    rx = dx * math.cos(th) - dy * math.sin(th)
    ry = dx * math.sin(th) + dy * math.cos(th)
    tx, ty = o_cx - rx, hole_y - ry
    parts = []
    if with_text:
        parts.append(f'<path id="hilo" d="M{o_cx:g} 80V{hole_y:g}" fill="none" stroke="{thread}" stroke-width="{tw}" stroke-linecap="round"/>')
        parts.append(f'<g id="vuelco" fill="{ink}">')
        for ch, x, p in letters:
            rule = ' fill-rule="evenodd"' if ch == "O" else ""
            parts.append(f'<path id="{ch.lower()}" transform="translate({x} 0)"{rule} d="{p}"/>')
        parts.append("</g>")
    else:
        parts.append(f'<path id="hilo" d="M{o_cx:g} 0V{hole_y:g}" fill="none" stroke="{thread}" stroke-width="{tw}"/>')
    parts.append(f'<g id="s" transform="translate({tx:.3f} {ty:.3f}) rotate({TILT}) translate({-S_ORIGIN_LOCAL[0]} {-S_ORIGIN_LOCAL[1]})">'
                 f'<path d="{S_PATH}" fill="none" stroke="{accent}" stroke-width="{S_STROKE}"/></g>')
    parts.append(f'<circle id="agujero" cx="{o_cx:g}" cy="{hole_y:g}" r="3.8" fill="{hole}"/>')
    return "\n".join(parts), (width, hole_y + 100), (o_cx, tx, ty)


def svg_open(w, h, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{label}">\n{META}\n')


def logo(path, bg=True):
    comp, (cw, ch), _o = composition(NAVY, RED)
    s = 1.8
    W, H = 1200, 600
    ox = (W - cw * s) / 2
    oy = (H - 250 * s) / 2
    body = svg_open(W, H, "VUELCOS")
    if bg:
        body += f'<rect width="{W}" height="{H}" fill="{BG}"/>\n'
    body += f'<g transform="translate({ox:.2f} {oy:.2f}) scale({s})">\n{comp}\n</g>\n</svg>\n'
    open(path, "w", encoding="utf-8").write(body)


def avatar(path, dark=False):
    N = 1024
    ink = BG if dark else NAVY
    acc = RED_DARK_BG if dark else RED
    bg = NAVY if dark else BG
    s = 5.0
    # solo hilo + S: hilo desde el borde superior hasta el ojal
    hole_y = 62  # en unidades; la S queda centrada verticalmente en el lienzo
    comp, _, (o_cx, tx, ty) = composition(ink, acc, hole_y=hole_y, with_text=False, thread=('#CBD5E1' if dark else '#64748B'), tw=1.1)
    # S ocupa ~ y[hole_y-5 .. hole_y+95] aprox.; centramos el bloque S en el lienzo (centro en y=530)
    total_h = (hole_y + 95)
    # Alinear: x del ojal en el centro del lienzo; hilo parte de y=0 del lienzo
    ox = N / 2 - tx * s   # el cuerpo de la S queda centrado; el hilo cae vertical en su punto de enganche
    oy = 530 - ty * s
    # el hilo debe llegar al borde superior: lo alargamos hacia arriba
    top = -oy / s
    comp = comp.replace(f'M{o_cx:g} 0V', f'M{o_cx:g} {top - 5:.2f}V')
    body = svg_open(N, N, "VUELCOS")
    body += f'<rect width="{N}" height="{N}" fill="{bg}"/>\n'
    body += f'<g transform="translate({ox:.2f} {oy:.2f}) scale({s})">\n{comp}\n</g>\n</svg>\n'
    open(path, "w", encoding="utf-8").write(body)


def banner(path):
    comp, (cw, ch), _o = composition(NAVY, RED, tw=2.1)
    W, H = 2048, 1152
    s = 1.2
    ox = (W - cw * s) / 2
    oy = (H - 250 * s) / 2
    body = svg_open(W, H, "VUELCOS")
    body += f'<rect width="{W}" height="{H}" fill="{BG}"/>\n'
    body += f'<g transform="translate({ox:.2f} {oy:.2f}) scale({s})">\n{comp}\n</g>\n</svg>\n'
    open(path, "w", encoding="utf-8").write(body)


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    logo(f"{out}/vuelcos-logo-horizontal.svg", bg=True)
    logo(f"{out}/vuelcos-logo-horizontal-transparente.svg", bg=False)
    avatar(f"{out}/vuelcos-avatar.svg", dark=False)
    avatar(f"{out}/vuelcos-avatar-oscuro.svg", dark=True)
    banner(f"{out}/vuelcos-banner-youtube.svg")
    print("ok")
