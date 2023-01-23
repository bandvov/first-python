from vpython import *
import numpy as np

toRad = 2*np.pi/360
toDeg = 1/toRad


def get_vector_coordinates(pitch, yaw, length):
    x = length * cos(pitch) * cos(yaw)
    y = length * sin(pitch)
    z = length * sin(yaw) * cos(pitch)
    return x, y, z


def get_vector_length(x, y, z):
    return sqrt(x*x + y*y + z*z)
