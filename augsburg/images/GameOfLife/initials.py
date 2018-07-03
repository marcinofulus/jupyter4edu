import os
import sys
from pyx import canvas, color, path, text, trafo, unit

def draw_config(name):
    c = canvas.canvas()
    config = configs[name]
    ysize = len(config)
    xsize = len(config[0])
    for nx in range(xsize):
        for ny in range(ysize):
            if config[ny][nx]:
                c.fill(path.rect(nx, ysize-ny, 1, -1))
    strokecolor = color.grey(0.6)
    c.stroke(path.rect(0, 0, xsize, ysize), [strokecolor])
    for nx in range(1, xsize):
        c.stroke(path.line(nx, 0, nx, ysize), [strokecolor])
    for ny in range(1, ysize):
        c.stroke(path.line(0, ny, xsize, ny), [strokecolor])
    return c

configs = {'blinker': [[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]],
           'toad': [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]],
           'glider': [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]],
           'beacon': [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 0, 0, 0],
                      [0, 1, 1, 0, 0, 0],
                      [0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0]],
           'pulsar': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
           'pentadecathlon': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
          }

text.set(text.LatexRunner)
unit.set(xscale=4, wscale=2)
c = canvas.canvas()
xpos = 0
for k in ('blinker', 'beacon', 'toad', 'glider',
          'pentadecathlon', 'pulsar'):
    c.insert(draw_config(k), [trafo.translate(xpos, 0)])
    wd = len(configs[k][0])
    c.text(xpos+0.5*wd,
           -0.5, r'\sffamily {}'.format(k),
           [text.halign.center, text.valign.top])
    xpos = xpos+wd+1
filename = os.path.splitext(sys.argv[0])[0]+'.png'
c.writeGSfile(filename, resolution=200)
