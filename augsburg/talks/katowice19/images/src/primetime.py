from math import cos, radians, sin, sqrt
from pyx import canvas, color, deformer, path, style, text, trafo, unit

def prime_list(maximum):
    if maximum < 2:
        raise ValueError('maximum should be at least 2')
    candidates = [False, False]+[True]*(maximum-1)
    maxcandidate = int(sqrt(maximum)+0.5)
    candidate = candidates.index(True)
    while candidate <= maxcandidate:
        for multiple in range(candidate**2, maximum+1, candidate):
            candidates[multiple] = False
        offset = candidate+1
        candidate = candidates[offset:].index(True)+offset
    primelist = [nr for nr, isprime in enumerate(candidates) if isprime]
    return primelist

def is_time(n):
    hours, minutes = divmod(n, 100)
    return 0 <= hours <= 23 and 0 <= minutes <= 59

def formattime(t):
    s = '{:04}'.format(t)
    return r'\scriptsize\texttt{{{}:{}}}'.format(s[0:2], s[2:])

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

c2 = canvas.canvas([canvas.clip(p)])
primetimes = [p for p in prime_list(2359) if is_time(p)]
s = text.text(0, 0, formattime(primetimes[0]))
textwidth, textheight = s.width, s.height
nx = int(w/unit.tocm(textwidth))
xoff = 0.5*(w-1.2*textwidth*nx+0.2*textwidth)
for n, p in enumerate(primetimes):
    s = formattime(p)
    x = xoff+(n % nx)*1.2*textwidth
    y = 1.03*h-(n//nx)*textheight*1.4
    c2.text(x, y, s, [color.hsb(0.67, 0.4, 0.8)])
c.insert(c2)

r1 = 0.95*h/2
r2 = 0.8*h/2
for n in range(12):
    x = sin(radians(n*30))
    y = cos(radians(n*30))
    c.stroke(path.line(w/2+r1*x, h/2+r1*y, w/2+r2*x, h/2+r2*y),
             [style.linewidth.THICk])
x = sin(radians(70))
y = cos(radians(70))
c.stroke(path.line(w/2-0.1*x, h/2-0.1*y, w/2+r1*x, h/2+r1*y),
         [style.linewidth.THICk, color.rgb(0.7, 0, 0)])
x = sin(radians(320))
y = cos(radians(320))
c.stroke(path.line(w/2-0.1*x, h/2-0.1*y, w/2+0.6*r1*x, h/2+0.6*r1*y),
         [style.linewidth.THICk, color.rgb(0.7, 0, 0)])
c.writeGSfile(device="png16m", resolution=300)
