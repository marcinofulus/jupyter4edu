from pyx import canvas, color, deformer, graph, path, trafo
import numpy as np
from scipy import signal

class Conway:
    """Conway's game of life

    """
    v = np.array([[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])

    def __init__(self, size=100):
        """prepare initial state of game of life

           size: Size of the square lattice on which the population
                 dynamics unfolds. Periodic boundary conditions are
                 used.

        """
        self.size = size
        self.world = np.random.randint(0, 2, (self.size, self.size))

    def update(self, *args):
        """update the population in self.world

        """
        n = signal.convolve2d(self.world, self.v, mode='same', boundary='wrap')
        self.world = self.world & (n == 2)
        self.world = self.world | (n == 3)

c = canvas.canvas()
dx = 0.3
h = 4
w = 6.5
p = path.rect(-dx, -dx, w+2*dx, h+2*dx)
p = deformer.smoothed(0.5).deform(p)
c.fill(p, [color.grey(0.5), trafo.translate(0.05, -0.05)])

c1 = canvas.canvas([canvas.clip(p)])
c1.fill(p, [color.grey(0.9)])

np.random.seed = 42
game = Conway(300)
for _ in range(15):
    game.update()
world = game.world
xoff = -0.5*w-dx
yoff = -0.5*h-dx
delta = 0.1
for nx in range(game.size):
    for ny in range(game.size):
        if world[nx, ny]:
            p = path.rect(xoff+(nx+0.1)*delta, yoff+(ny+0.1)*delta,
                          0.8*delta, 0.8*delta)
            c1.fill(p, [color.hsb(0.25, 1, 0.5)])

c.insert(c1)
c.writePDFfile()
