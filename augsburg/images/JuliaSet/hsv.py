import os
import sys
from fractions import Fraction
from math import cos, degrees, pi, sin
import numpy as np
from pyx import canvas, color, path, text

def fracstr(num, denom):
    f = Fraction(num, denom)
    if f.numerator == 0:
        return '0'
    else:
        return r'\small$\nicefrac{{{}}}{{{}}}$'.format(f.numerator, f.denominator)

radius = np.linspace(0, 1, 200)
angle = np.linspace(0, 2*pi, 200)

text.set(text.LatexRunner)
text.preamble(r'\usepackage{nicefrac}')
c = canvas.canvas()
for x0, y0, v in ((0, 0, 1), (3.2, 0, 0.7)):
    for nphi in range(6):
        phi = 2*pi*nphi/6
        c.stroke(path.line(x0+0.95*cos(phi), y0+0.95*sin(phi),
                           x0+1.08*cos(phi), y0+1.08*sin(phi)))
        c.text(x0+1.3*cos(phi), y0+1.3*sin(phi), fracstr(nphi, 6),
               [text.halign.center, text.valign.middle])
    for r1, r2 in zip(radius[:-1], radius[1:]):
        for phi1, phi2 in zip(angle[:-1], angle[1:]):
            p = path.path(path.moveto(x0+r1*cos(phi1), y0+r1*sin(phi1)),
                          path.lineto(x0+r2*cos(phi1), y0+r2*sin(phi1)),
                          path.arc(x0, y0, r2, degrees(phi1), degrees(phi2)),
                          path.lineto(x0+r1*cos(phi2), y0+r1*sin(phi2)),
                          path.arcn(x0, y0, r1, degrees(phi2), degrees(phi1)),
                          path.closepath()
                         )
            c.fill(p, [color.hsb(0.5*(phi1+phi2)/(2*pi), 0.5*(r1+r2), v)])
            c.text(x0, y0-1.7, '$v = {}$'.format(v), [text.halign.center,
                                                      text.valign.top])
filename = os.path.splitext(sys.argv[0])[0]+'.png'
c.writeGSfile(filename, resolution=200)
