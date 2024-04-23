import vedo
from vedo import Box, show
from vedo import Cube, show
from time import time
import time

from vedo import *
import numpy as np
from vtk import vtkBooleanOperationPolyDataFilter
from vtk import vtkMassProperties

c1 = Cube()
c2 = Cube()
c2.pos(0.6,0.4,0.3)
c2.rotate_x(30)
c1.triangulate().subdivide(4, method=1).wireframe().alpha(0.1)
c2.triangulate().subdivide(4, method=1).wireframe().alpha(0.1)
cc = c1.boolean("intersect", c2).c("red5")
show(c1, c2, cc, f"Volume = {cc.volume()}", axes=1)
