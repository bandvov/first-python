from vpython import *
from scene import set_scene
from util import *
import math


set_scene()

radius = 1000
pitch_in_deg = 30
yaw_in_deg = 30

pitch = pitch_in_deg*toRad
yaw = yaw_in_deg*toRad


radius1 = 1000
pitch_in_deg1 = 30
yaw_in_deg1 = 40

pitch1 = pitch_in_deg1*toRad
yaw1 = yaw_in_deg1*toRad

x, y, z = get_vector_coordinates(pitch=pitch, yaw=yaw, length=radius)

axis = vector(x, y, z)

cylinder(axis=axis, radius=1, length=radius, color=color.red)


x1, y1, z1 = get_vector_coordinates(pitch=pitch1, yaw=yaw1, length=radius1)


axis1 = vector(x1, y1, z1)

cylinder(axis=axis1, radius=1, length=radius1, color=color.blue)

x2 = x1-x
y2 = y1-y
z2 = z1-z

short_vector_length = get_vector_length(x2, y2, z2)

axis2 = vector(x2, y2, z2)

cylinder(pos=vector(x, y, z), axis=axis2,
         radius=1, length=short_vector_length, color=color.red)

cylinder(pos=vector(x1, y1, z1), axis=axis2,
         radius=1, length=60, color=color.black)

speed = 60
time_in_seconds = 1
coefficient = (1 / (short_vector_length / speed)) * time_in_seconds

x3 = x1+(x2*coefficient)
y3 = y1+(y2*coefficient)
z3 = z1+(z2*coefficient)

length3 = get_vector_length(x3, y3, z3)

pitch3 = math.asin(y3/length3)
yaw3 = math.atan2(z3, x3)

axis3 = vector(x3, y3, z3)

cylinder(axis=axis3, radius=1, length=length3, color=color.cyan)
sphere(pos=vector(x3, y3, z3), radius=4)

x4, y4, z4 = get_vector_coordinates(pitch=pitch3, yaw=yaw3, length=length3)

axis4 = vector(x4, y4, z4)
cylinder(axis=axis4, radius=4, opacity=0.2,
         length=length3, color=color.orange)

while True:
    rate(1)
