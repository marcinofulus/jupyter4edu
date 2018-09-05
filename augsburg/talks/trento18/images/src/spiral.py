from pyx import canvas, color, deformer, path, text, trafo, unit

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

c1 = canvas.canvas()
boxwd = 0.7
for n in range(-5, 6):
    x = (n-0.5)*boxwd
    c1.stroke(path.line(x, -0.5*h-dx, x, 0.5*h+dx))
for n in range(-5, 6):
    y = (n-0.5)*boxwd
    c1.stroke(path.line(-0.5*w-dx, y, 0.5*w+dx, y))

highlight = color.rgb(0.7, 0, 0)
template = r'\texttt{{\bfseries{}}}'
pos = [0, 0]
number = 1
c1.text(*pos, template.format(number),
        [text.halign.center, text.valign.middle, highlight])
for nshell in range(1, 6):
    pos[0] = pos[0]+1
    pos[1] = pos[1]+1
    for dir in ((0, -1), (-1, 0), (0, 1), (1, 0)):
        for _ in range(2*nshell):
            number = number+1
            pos = list(x+y for x, y in zip(pos, dir))
            x, y = boxwd*pos[0], boxwd*pos[1]
            myattrs = [text.halign.center, text.valign.middle]
            if abs(pos[0]) == abs(pos[1]):
                myattrs.append(highlight)
            c1.text(x, y, template.format(number), myattrs)

c2 = canvas.canvas([canvas.clip(p)])
c2.insert(c1, [trafo.translate(0.5*w, 0.5*h)])
c.insert(c2)
c.writePDFfile()
