from pyx import canvas, color, deco, deformer, graph, path, style, trafo

def ellipse(r, scaley, fillcolor):
    ce = canvas.canvas()
    ce.fill(path.circle(0, 0, r), [trafo.scale(1, scaley), fillcolor])
    return ce

c = canvas.canvas()
dx = 0.3
h = 4
w = 6.5
p = path.rect(-dx, -dx, w+2*dx, h+2*dx)
p = deformer.smoothed(0.5).deform(p)
c.fill(p, [color.grey(0.5), trafo.translate(0.05, -0.05)])

c1 = canvas.canvas([canvas.clip(p)])
c1.fill(p, [color.grey(0.9)])

r = 1
brown1 = color.rgb(148/255, 77/255, 48/255)
brown2 = color.rgb(193/255, 91/255, 49/255)
red1 = color.rgb(200/255, 0, 0)
red2 = color.rgb(220/255, 0.5, 0.5)
flame = color.rgb(248/255, 212/255, 27/255)
c2 = canvas.canvas()
c2.insert(ellipse(r, 0.5, brown1))
c2.fill(path.rect(-r, 0, 2*r, 0.5*r), [brown1])
c2.insert(ellipse(r, 0.5, brown2), [trafo.translate(0, 0.5*r)])
c2.insert(ellipse(0.2*r, 0.5, red1), [trafo.translate(0, 0.5*r)])
c2.fill(path.rect(-0.2*r, 0.5*r, 0.4*r, r), [red1])
c2.insert(ellipse(0.2*r, 0.5, red2), [trafo.translate(0, 1.5*r)])
c2.stroke(path.line(0, 1.5*r, 0, 1.5*r+0.2), [style.linewidth.Thick])
c2a = canvas.canvas()
c2a.fill(path.path(path.moveto(0, 0),
                   path.curveto(-0.1, -0.2, -0.3, -0.6, 0, -0.6),
                   path.curveto(0.3, -0.6, 0, -0.3, 0, 0),
                   path.closepath()), [flame])
c2.insert(c2a, [trafo.translate(0, 1.65*r+0.6)])

c.insert(c1)
c.insert(c2, [trafo.translate(1.75, 1.3)])
c.insert(c2, [trafo.translate(4.7, 1.3)])
c.writeGSfile(device="png16m", resolution=300)
