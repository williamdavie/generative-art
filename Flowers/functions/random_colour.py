import random
import colorsys

def random_colour(s):
    h = random.random()
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h,s,v)
    rgb = [int(x*255) for x in float_rgb]
    
    return tuple(rgb)