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

# To use setResFromFile, uncomment the next line:
#mesh.setResFromFile("box1.stl", 0.03, inside=True)

# And comment the following lines:
middle_patch = mesh.findPatch(0, 0, 0)
middle_patch.setRes(0.015)
mesh.setGrading1(1.5)
mesh.setMinDim(4)
mesh.update()
#

# Create farfield mesh and merge to existing mesh
mesh.createExternalAeroMesh()

# Write mesh
mesh.save("patches/standard.grid")
mesh.printInfo()
