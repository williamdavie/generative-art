
import numpy as np
from math import *

def generate_points(a,angle_range):
    points = []
    for i in np.arange(1,angle_range,0.01):
        r = a/i
        x = r*cos(i)
        y = r*sin(i)
        points.append((x,y))

    return points