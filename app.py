from vpython import *
import numpy as np
scene.background = color.white
scene.width = 1500
scene.height = 760
scene.forward = vector(-1, -1, -1)
rate(30)
arrowLength = 100
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

h = 100

pitch = 30*toRad
yaw = 30*toRad
x = h * cos(yaw)
y = h * sin(yaw)
z = y * sin(pitch)
axis = vector(x, y, z)
print(axis)
cylinder(axis=axis, radius=1, length=100, color=color.red)
cylinder(axis=vector(x, y, 0),
         radius=1, length=100, color=color.red)
cylinder(pos=vector(x, y, 0), axis=vector(0, 0, 1),
         radius=1, length=z, color=color.red)

# pitch1 = 45*toRad
# yaw1 = 45*toRad
# x1 = h * cos(yaw1)
# y1 = h * sin(yaw1)
# z1 = y1 * sin(pitch1)
# axis1 = vector(x1, y1, z1)
# print(axis1)
# cylinder(axis=axis1, radius=1, length=100, color=color.black)

pitch2 = 60*toRad
yaw2 = 60*toRad
x2 = h * cos(yaw2)
y2 = h * sin(yaw2)
z2 = y2 * sin(pitch2)
axis2 = vector(x2, y2, z2)
print(axis2)
cylinder(axis=axis2, radius=1, length=120, color=color.green)
cylinder(axis=vector(x2, y2, 0), radius=1, length=100, color=color.green)
cylinder(pos=vector(x2, y2, 0), axis=vector(0, 0, 1),
         radius=1, length=z2, color=color.green)

pitch3 = 80*toRad
yaw3 = 80*toRad
x3 = h * cos(yaw3)
y3 = h * sin(yaw3)
z3 = y3 * sin(pitch3)
axis3 = vector(x3, y3, z3)
print(axis3)
cylinder(axis=axis3, radius=1, length=160, color=color.magenta)
print(h*x)
cylinder(axis=vector(x3, y3, 0), radius=1, length=120, color=color.magenta)
cylinder(pos=vector(x3, 120, 0), axis=vector(0, 0, 1),
         radius=1, length=120, color=color.magenta)


cylinder(pos=vector(x, y, z), radius=1, length=120,
         axis=vector(-x, y2, 120*sin(pitch2)), color=color.blue)
