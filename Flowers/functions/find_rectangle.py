
import random

def find_rectangle(size):
    top_y = size/2 - random.randint(size/4,size/2)
    bottom_y = size - top_y

    top_x = size/2
    bottom_x = random.randint(0,size)

    if bottom_x < size/2:
        return bottom_x,top_y,top_x,bottom_y
    else:
        return top_x,top_y,bottom_x,bottom_y