import random
import colorsys

def random_colour():
    #selects a random colour and it's opposite colour

    h = random.random()
    s = 1
    v = 1

    if h < 0.5:
        opposite_h = h+0.5
    else:
        opposite_h = h-0.5

    float_rgb = colorsys.hsv_to_rgb(h,s,v)
    rgb = [int(x*255) for x in float_rgb]
    o_float_rgb = colorsys.hsv_to_rgb(opposite_h,s,v)
    o_rgb = [int(x*255) for x in o_float_rgb]

    return [tuple(rgb),tuple(o_rgb)]