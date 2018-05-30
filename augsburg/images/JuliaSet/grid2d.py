import os
import sys
from pyx import canvas, color, deco, path, text

nxpts = 4
nypts = 3
arrowstyle = [deco.earrow.small, color.rgb(0.8, 0, 0)]
c = canvas.canvas()
for ny in range(nypts):
    for nx in range(nxpts):
        c.fill(path.circle(nx, ny, 0.05))
        c.text(nx, ny-0.1, r'\tiny $({},{})$'.format(nx, ny),
               [text.halign.center, text.valign.top])
        if nx < nxpts-1:
            c.stroke(path.line(nx+0.1, ny, nx+0.9, ny), arrowstyle)
        elif ny < nypts-1:
            c.stroke(path.line(nx-0.1, ny+0.1, 0.1, ny+0.9), arrowstyle)
filename = os.path.splitext(sys.argv[0])[0]+'.png'
c.writeGSfile(filename, resolution=200)
