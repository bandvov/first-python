from vpython import *


def set_scene():
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
