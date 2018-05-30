import os
import sys
from pyx import canvas, color, deco, path, text

def put_label(x, y, nr):
    r = 0.3
    label = r'\textsf{{\bfseries {}}}'.format(nr)
    if abs(x) == abs(y):
        c.fill(path.circle(x, y, r), [color.rgb.black])
        c.text(x, y, label, [text.halign.center, text.valign.middle,
                               color.rgb.white])
    else:
        c.stroke(path.circle(x, y, r), [deco.filled([color.rgb.white])])
        c.text(x, y, label, [text.halign.center, text.valign.middle])

text.set(text.LatexRunner)
c = canvas.canvas()

x0 = 0
y0 = 0
nr = 0
for n in range(1, 7):
    if n % 2:
        x1 = x0+n
        y1 = y0
        c.stroke(path.line(x0, y0, x1, y1))
        for nt in range(n):
            nr = nr+1
            put_label(x0+nt, y0, nr)
        x0 = x1
        y1 = y0-n
        c.stroke(path.line(x0, y0, x1, y1))
        for nt in range(n):
            nr = nr+1
            put_label(x0, y0-nt, nr)
        y0 = y1
    else:
        x1 = x0-n
        y1 = y0
        c.stroke(path.line(x0, y0, x1, y1))
        for nt in range(n):
            nr = nr+1
            put_label(x0-nt, y0, nr)
        x0 = x1
        y1 = y0+n
        c.stroke(path.line(x0, y0, x1, y1))
        for nt in range(n):
            nr = nr+1
            put_label(x0, y0+nt, nr)
        y0 = y1
x1 = x0+n
c.stroke(path.line(x0, y0, x1, y1))
for nt in range(n+1):
    nr = nr+1
    put_label(x0+nt, y0, nr)

filename = os.path.splitext(sys.argv[0])[0]+'.png'
c.writeGSfile(filename, resolution=100)
