"""

A plotting tool for 3D particle in a box.

Pranay Venkatesh

"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, hbar
from mpl_toolkits.mplot3d import Axes3D
import sys

class coord:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def psi_squared (l, nx, ny, nz, c):
    prob = (np.sin(nx * math.pi * c.x / l)**2) * (np.sin(ny * math.pi * c.y / l)**2) * (np.sin(nz * math.pi * c.z / l)**2)
    return prob


coords = []
probs = []

args = sys.argv

l = int(args[1])
nx = int(args[2])
ny = int(args[3])
nz = int(args[4])

x = np.linspace(0, l, 100)
y = np.linspace(0, l, 100)
z = np.linspace(0, l, 100)


for i1 in x:
    for i2 in y:
        for i3 in z:
            coords.append(coord(i1,i2,i3))
            probs.append(psi_squared(l, nx, ny, nz, coord(i1,i2,i3)))


probs = probs/np.sum(probs)

rand_coords = np.random.choice(coords, size = 100, replace = True, p = probs)

x_coords = []
y_coords = []
z_coords = []

for c in rand_coords:
    x_coords.append(c.x)
    y_coords.append(c.y)
    z_coords.append(c.z)

fig = plt.figure(figsize = (10,10))

ax = fig.add_subplot(111, projection = "3d")

ax.scatter(x_coords, y_coords, z_coords)
ax.set_title("Particle in a 3D Box")

plt.show()
