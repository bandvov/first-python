from vpython import *
import numpy as np
import math
scene.background = color.white
scene.width = 1500
scene.height = 760
scene.forward = vector(-1, -1, -1)
rate(30)
arrowLength = 1000
shaftwidth = 1
xarrow = arrow(shaftwidth=shaftwidth, color=color.red)
yarrow = arrow(shaftwidth=shaftwidth, color=color.green)
zarrow = arrow(shaftwidth=shaftwidth, color=color.blue)
xarrow.axis = vector(1, 0, 0)
xarrow.length = arrowLength
yarrow.axis = vector(0, 1, 0)
yarrow.length = arrowLength
zarrow.axis = vector(0, 0, 1)
zarrow.length = arrowLength


toRad = 2*np.pi/360
toDeg = 1/toRad

radius = 1000

pitch = 30*toRad
yaw = 30*toRad
x = radius * cos(pitch) * cos(yaw)
z = radius * sin(yaw) * cos(pitch)
y = radius * sin(pitch)

axis = vector(x, y, z)
print(axis)
cylinder(axis=axis, radius=1, length=radius, color=color.red)

pitch1 = 30*toRad
yaw1 = 52*toRad
radius1 = 1100
x1 = radius1 * cos(pitch1) * cos(yaw1)
y1 = radius1 * sin(pitch1)
z1 = radius1 * sin(yaw1) * cos(pitch1)

axis1 = vector(x1, y1, z1)
print(axis1)
cylinder(axis=axis1, radius=1, length=radius1, color=color.blue)


x2 = (x1-x)
y2 = (y1-y)
z2 = (z1-z)

cylinder(pos=vector(x, y, z), axis=vector(x2, y2, z2),
         radius=1, length=100, color=color.red)

cylinder(pos=vector(x1, y1, z1), axis=vector(x2, y2, z2),
         radius=1, length=100, color=color.black)
coefficient = 1
x3 = x1+(x2*coefficient)
y3 = y1+(y2*coefficient)
z3 = z1+(z2*coefficient)

axis3 = vector(x3, y3, z3)
magnitude = sqrt(x3*x3 + y3*y3 + z3*z3)

cylinder(axis=axis3, radius=1, length=magnitude, color=color.cyan)

pitch3 = math.asin(y3/magnitude)

print(pitch3)
yaw3 = math.atan2(z3, x3)

# print('here',  pitch3*toDeg)
# print('here',  yaw3*toDeg)
print(x3)
print(y3)
print(z3)
print(pitch*toDeg)
print(yaw*toDeg)

x4 = magnitude * cos(pitch3) * cos(yaw3)
y4 = magnitude * sin(pitch3)
z4 = magnitude * sin(yaw3) * cos(pitch3)

axis4 = vector(x4, y4, z4)
cylinder(axis=axis4, radius=4, length=magnitude, color=color.orange)