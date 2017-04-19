#!/usr/bin/python

import drnum

mesh = drnum.ExternalAeroMesh()
mesh.super_cell_scaling = 2.

x = [-1.2, -0.6, 0.6, 1.2]
y = [-1.2, -0.6, 0.6, 1.2]
z = [-1.2, -0.6, 0.6, 1.2]

mesh.x1 = (x[0],  y[0],  z[0])
mesh.x2 = (x[-1], y[-1], z[-1])

mesh.x1_far = (-4.4, -4.4, -4.4)
mesh.x2_far = ( 4.4,  4.4,  4.4)

mesh.createRectGrid(x, y, z)
mesh.setResFromFile("box1.stl", 0.03, inside=True)

mesh.create()
mesh.save("patches/standard.grid")
mesh.printInfo()
