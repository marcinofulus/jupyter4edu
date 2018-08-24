from pyx import canvas, color, deformer, path, text, trafo, unit

text.set(text.LatexRunner)
text.preamble(r'''\usepackage[scaled=0.85,lining]{FiraMono}
                  \usepackage[utf8]{inputenc}''')
pistring = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852'
char_per_line = 25
pistring = ' '.join([pistring[n*char_per_line:(n+1)*char_per_line]
                     for n in range(10)])
unit.set(xscale=1.45)

c = canvas.canvas()
dx = 0.3
h = 4
w = 6.5
p = path.rect(-dx, -dx, w+2*dx, h+2*dx)
p = deformer.smoothed(0.5).deform(p)
c.fill(p, [color.grey(0.5), trafo.translate(0.05, -0.05)])
c.fill(p, [color.grey(0.9)])
c.text(0, 0, r'\noindent\texttt{{{}}}'.format(pistring),
       [text.valign.bottom, text.parbox(5)])
c.text(0.5*w, 0.5*h, r'\Huge $\pi$', [text.halign.center, text.valign.middle,
                                      color.hsb(0.66, 0.8, 1), color.transparency(0.2),
                                      trafo.scale(5.8)])

c.writePDFfile()
