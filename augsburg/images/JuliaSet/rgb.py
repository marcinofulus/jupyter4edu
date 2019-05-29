import os
import sys
import numpy as np
from pyx import canvas, color, deco, graph, path, trafo

c = canvas.canvas()

coordinates = np.linspace(-0.5, 0.5, 200)
pt1 = [0, 0, 0]
pt2 = [0, 0, 0]
pt3 = [0, 0, 0]
pt4 = [0, 0, 0]
for x0, y0, side, projector in ((0, 0, 0.5, graph.graphxyz.central(5, 30, 30)),
                                (2.5, -0.1, -0.5, graph.graphxyz.central(5, 210, -30))):
    for direction in range(3):
        for coord11, coord12 in zip(coordinates[:-1], coordinates[1:]): 
            for coord21, coord22 in zip(coordinates[:-1], coordinates[1:]): 
                pt1[direction] = side
                pt1[(direction+1) % 3] = coord11
                pt1[(direction+2) % 3] = coord21
                pt2[direction] = side
                pt2[(direction+1) % 3] = coord12
                pt2[(direction+2) % 3] = coord21
                pt3[direction] = side
                pt3[(direction+1) % 3] = coord12
                pt3[(direction+2) % 3] = coord22
                pt4[direction] = side
                pt4[(direction+1) % 3] = coord11
                pt4[(direction+2) % 3] = coord22
                p = path.path(path.moveto(*projector.point(*pt1)),
                              path.lineto(*projector.point(*pt2)),
                              path.lineto(*projector.point(*pt3)),
                              path.lineto(*projector.point(*pt4)),
                              path.closepath())
                rgbcolor = [0, 0, 0]
                rgbcolor[direction] = side+0.5
                rgbcolor[(direction+1) % 3] = (coord11+coord12+1)/2
                rgbcolor[(direction+2) % 3] = (coord21+coord22+1)/2
                c.fill(p, [color.rgb(*rgbcolor), trafo.translate(x0, y0)])

filename = os.path.splitext(sys.argv[0])[0]+'.png'
c.writeGSfile(filename, resolution=200)
