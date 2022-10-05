import random

def rectangle_corner(x,y,size):
    #takes the co-ords of one corner of a rectangle and returns the opposing corner

    scale_x = random.randint(size/8,size/2)
    scale_y = random.randint(size/8,size/2)

    if x >= 0:
        x_2 = x - scale_x
    else:
        x_2 = x + scale_x

    if y >= 0:
        y_2 = y - scale_y
    else:
        y_2 = y + scale_y

    return(x_2 + size/2,y_2+size/2)