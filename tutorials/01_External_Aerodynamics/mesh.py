import drnum
import numpy

M = drnum.ExternalAeroMesh()

M.x1[0] = -60.0
M.x1[1] = -10.0
M.x1[2] = -10.0

M.x2[0] =   0.0
M.x2[1] =  10.0
M.x2[2] =  10.0

M.x1_far[0] = -80.0
M.x1_far[1] = -80.0
M.x1_far[2] = -80.0

M.x2_far[0] =   0.0
M.x2_far[1] =  80.0
M.x2_far[2] =  80.0

M.super_cell_size = 5.0
M.cell_size       = 0.1

M.quarterGeometry()
M.createExternalAeroMesh()
M.save('patches/standard.grid')
M.printInfo()
