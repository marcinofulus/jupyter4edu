from pyx import canvas, color, deco, deformer, path, style, text, trafo, unit

text.set(text.LatexRunner)
text.preamble(r'''\usepackage[scaled=0.85,lining]{FiraMono}
                  \usepackage[utf8]{inputenc}
                  \usepackage{marvosym}''')
unit.set(xscale=1.2)

c = canvas.canvas()
dx = 0.3
h = 4
w = 6.5
p = path.rect(-dx, -dx, w+2*dx, h+2*dx)
p = deformer.smoothed(0.5).deform(p)
c.fill(p, [color.grey(0.5), trafo.translate(0.05, -0.05)])
c.fill(p, [color.grey(0.9)])

c.stroke(path.line(0, 0.4*h, w, 0.4*h), [deco.earrow])
c.stroke(path.line(0, 0, 0, h), [deco.earrow])
with open('parrondo.dat') as file:
    dataset = file.readlines()

data = [tuple(map(int, line.strip('\n').split())) for line in dataset]
scale = lambda x: ((x+1000)/2500)*h
datascaled = [tuple(map(scale, x)) for x in data]
p1 = path.path(path.moveto(0, 0.4*h))
p2 = path.path(path.moveto(0, 0.4*h))
p3 = path.path(path.moveto(0, 0.4*h))
for n, (a, b, aabb) in enumerate(datascaled):
    p1.append(path.lineto(w*n/1000, a))
    p2.append(path.lineto(w*n/1000, b))
    p3.append(path.lineto(w*n/1000, aabb))
c.stroke(p1, [color.rgb(1, 0, 0)])
c.stroke(p2, [color.rgb(0, 1, 0)])
c.stroke(p3, [color.rgb(0, 0, 1)])

c1 = canvas.canvas()
c1.fill(path.circle(0, 0, 0.08*w), [color.hsb(0.1, 1, 0.6)])
c1.text(0, 0, r'\Large\textit{\bfseries 1}',
        [text.halign.center, text.valign.middle, color.hsb(0.1, 1, 1)])
c1.fill(path.circle(0.18*w, 0, 0.08*w), [color.hsb(0.1, 1, 0.6)])
c1.text(0.18*w, 0, r'\Large\Smiley',
        [text.halign.center, text.valign.middle, color.hsb(0.1, 1, 1)])
c.insert(c1, [trafo.translate(0.1*w, 0.8*h)])
c.writeGSfile(device="png16m", resolution=300)
