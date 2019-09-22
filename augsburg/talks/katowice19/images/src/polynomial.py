from math import cos, radians, sin, sqrt
from pyx import canvas, color, deformer, path, style, text, trafo, unit

text.set(text.LatexRunner)
text.preamble(r'''\usepackage[scaled=0.85,lining]{FiraMono}
                  \usepackage[utf8]{inputenc}''')
unit.set(xscale=1.2)

c = canvas.canvas()
dx = 0.3
h = 4
w = 6.5
p = path.rect(-dx, -dx, w+2*dx, h+2*dx)
p = deformer.smoothed(0.5).deform(p)
c.fill(p, [color.grey(0.5), trafo.translate(0.05, -0.05)])
c.fill(p, [color.grey(0.9)])

c1 = canvas.canvas([canvas.clip(p)])
c2 = canvas.canvas()
textcolor = color.hsb(0.6, 0.3, 1)
t = """\Huge
$2x^4+10x^3$

p1 = \{4: 2, 3: 10\}

$5x^2-x+32$

p2 = \{2: 5, 1: -1, 0: 32\}

multiply(p1, p2)
"""
c2.text(0, 0, t, [text.parbox(2*w), textcolor])
c1.insert(c2, [trafo.rotate(20).translated(-0.2*w, 0.9*h)])
c.insert(c1)

t = r'\Large $(2x^4+10x^3)(5x^2-x+32)$'
c.text(w/2, h/2, t, [text.halign.center, text.valign.middle,
                     color.hsb(0.05, 0.9, 0.6)])
c.writeGSfile(device="png16m", resolution=300)
