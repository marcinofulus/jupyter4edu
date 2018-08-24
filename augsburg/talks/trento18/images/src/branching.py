import sys, os
from pyx import canvas, color, deco, deformer, path, text, trafo, unit

def set_myattrs(n, nhl):
    normalcolor = color.hsb(0.66, 1, 0.6)
    highlight = color.hsb(0, 1, 0.6)
    if n == nhl:
        return [highlight]
    else:
        return [normalcolor]

def file(c, size=1, xoff=0, yoff=0, attrs=[], title=''):
    w = 3
    h = 2.1
    fold = 0.6
    outline = path.path(path.moveto(0, 0),
                        path.lineto(w, 0),
                        path.lineto(w, h-fold),
                        path.lineto(w-fold, h),
                        path.lineto(0, h),
                        path.closepath())
    foldpath = path.path(path.moveto(w-fold, h),
                         path.lineto(w-fold, h-fold),
                         path.lineto(w, h-fold))
    c1 = canvas.canvas()
    c1.stroke(outline, attrs)
    d = deformer.smoothed(0.2)
    c1.stroke(d.deform(foldpath), attrs)
    c1.stroke(path.rect(0.1*w, 0.3*h, 0.6*w, 0.1*h))
    c1.stroke(path.rect(0.1*w, 0.45*h, 0.6*w, 0.1*h))
    c1.stroke(path.rect(0.1*w, 0.6*h, 0.6*w, 0.1*h))
    c1.stroke(path.rect(0.1*w, 0.75*h, 0.6*w, 0.1*h))
    c1.text(0.1, 0.1, r'\sffamily '+title, [trafo.scale(0.7)])
    myattrs = [trafo.translate(xoff, yoff), trafo.scale(size)]
    myattrs.extend(attrs)
    c.insert(c1, myattrs)

text.set(text.LatexRunner)
text.preamble(r'''%\usepackage[sfdefault,scaled=0.85,lining]{FiraSans}
                  \usepackage{arev}
                  \usepackage[utf8]{inputenc}''')
unit.set(wscale=1.3)

name = os.path.splitext(sys.argv[0])[0]+'_{}'
for norder in range(4):
    c = canvas.canvas()
    file(c, yoff=2.5, title='JuliaSet',
         attrs=set_myattrs(norder, 0))
    file(c, xoff=1, yoff=0, title=r'$\sim${}ColorRepresentation',
         attrs=set_myattrs(norder, 1))
    file(c, xoff=1, yoff=-2.5, title=r'$\sim${}Grid',
         attrs=set_myattrs(norder, 2))
    file(c, xoff=1, yoff=-5, title=r'$\sim${}JuliaIteration',
         attrs=set_myattrs(norder, 3))
    c.stroke(path.path(path.moveto(0.3, 2.4),
                       path.lineto(0.3, 0.2),
                       path.lineto(0.9, 0.2)), [deco.earrow])
    c.stroke(path.path(path.moveto(0.3, 0.1),
                       path.lineto(0.3, -2.3),
                       path.lineto(0.9, -2.3)), [deco.earrow])
    c.stroke(path.path(path.moveto(0.3, -2.4),
                       path.lineto(0.3, -4.8),
                       path.lineto(0.9, -4.8)), [deco.earrow])
    c.writePDFfile(name.format(norder+1))
