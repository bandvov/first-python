from vpython import *
import numpy as np
import math
from scene import *

set_scene()

toRad = 2*np.pi/360
toDeg = 1/toRad

radius = 1000

pitch = 30*toRad
yaw = 30*toRad

x = radius * cos(pitch) * cos(yaw)
z = radius * sin(yaw) * cos(pitch)
y = radius * sin(pitch)

axis = vector(x, y, z)

cylinder(axis=axis, radius=1, length=radius, color=color.red)

pitch1 = 30*toRad
yaw1 = 40.*toRad
radius1 = 900

x1 = radius1 * cos(pitch1) * cos(yaw1)
y1 = radius1 * sin(pitch1)
z1 = radius1 * sin(yaw1) * cos(pitch1)

axis1 = vector(x1, y1, z1)

cylinder(axis=axis1, radius=1, length=radius1, color=color.blue)

x2 = x1-x
y2 = y1-y
z2 = z1-z

magnitude_short = sqrt(x2*x2 + y2*y2 + z2*z2)

cylinder(pos=vector(x, y, z), axis=vector(x2, y2, z2),
         radius=1, length=magnitude_short, color=color.red)

cylinder(pos=vector(x1, y1, z1), axis=vector(x2, y2, z2),
         radius=1, length=60, color=color.black)

speed = 60
time_in_seconds = 1
coefficient = (1 / (magnitude_short / speed)) * time_in_seconds

x3 = x1+(x2*coefficient)
y3 = y1+(y2*coefficient)
z3 = z1+(z2*coefficient)

magnitude = sqrt(x3*x3 + y3*y3 + z3*z3)
axis3 = vector(x3, y3, z3)

cylinder(axis=axis3, radius=1, length=magnitude, color=color.cyan)
sphere(pos=vector(x3, y3, z3), radius=4)

pitch3 = math.asin(y3/magnitude)
yaw3 = math.atan2(z3, x3)
print(magnitude_short, 'short')
print(x3)
print(y3)
print(z3)
print(pitch3*toDeg)
print(yaw3*toDeg)

x4 = magnitude * cos(pitch3) * cos(yaw3)
y4 = magnitude * sin(pitch3)
z4 = magnitude * sin(yaw3) * cos(pitch3)

axis4 = vector(x4, y4, z4)
cylinder(axis=axis4, radius=4, opacity=0.2,
         length=magnitude, color=color.orange)
