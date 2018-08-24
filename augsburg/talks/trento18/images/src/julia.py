from pyx import canvas, color, deformer, graph, path, trafo
import numpy as np

def julia_iteration(x, y, c, schwelle, maxit):
    """Führe die Julia-Iterationsvorschrift aus, bis der
       Betrag des Ergebnisses den Wert von schwelle
       überschreitet. Es werden maximal maxit Iterationen
       ausgeführt.

       Die Iterationsvorschrift lautet z→z²+c, wobei
       z=x+iy.

       Es wird die Zahl der benötigten Iterationen bis zum
       Erreichend der Schwelle zurückgegeben. Wird diese
       nicht erreicht, so wird maxit zurückgegeben.

    """
    z = complex(x, y)
    for n in range(maxit):
        z = z**2+julia_c
        if abs(z) >= schwelle:
            break
    return n+1

xmin = -0.3
xmax = -0.1
ymin = 0.4
ymax = 0.6
seitenlaenge = 1000
julia_c = -0.8+0.156j
schwelle = 50000
maxit = 600

julia_daten = []

for y in np.linspace(ymin, ymax, seitenlaenge):
    for x in np.linspace(xmin, xmax, seitenlaenge):
        iterationen = julia_iteration(x, y, julia_c,
                                      schwelle, maxit)
        julia_daten.append((x, y, iterationen/maxit))

c = canvas.canvas()
dx = 0.3
h = 4
w = 6.5
p = path.rect(-dx, -dx, w+2*dx, h+2*dx)
p = deformer.smoothed(0.5).deform(p)
c.fill(p, [color.grey(0.5), trafo.translate(0.05, -0.05)])

c1 = canvas.canvas([canvas.clip(p)])
g = graph.graphxy(height=8, width=8,
                  x=graph.axis.linear(min=xmin, max=xmax),
                  y=graph.axis.linear(min=ymin, max=ymax))
g.plot(graph.data.points(julia_daten, x=1, y=2, color=3, title="iterations"),
       [graph.style.density(gradient=color.rgbgradient.Rainbow)])
c1.insert(g, [trafo.translate(-0.1*w, -0.5*h)])

c.insert(c1)
c.writePDFfile()
