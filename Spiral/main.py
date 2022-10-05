from PIL import Image,ImageDraw


import os
import random
import numpy as np
from math import *
import colorsys
from functions.mathematical_function import *
from functions.opposite_corner import *
from functions.random_colour import *



def generate_spiral(n):

    print("generating")
    target_size = 256
    scale_factor = 4
    size = target_size * scale_factor
    bg_colour = (255,255,255)
    image = Image.new("RGB",(size,size),bg_colour)

    #adding colour...

    colour = random_colour()

    rec_colour = colour[0]
    line_colour = colour[1]


    #drawing the rectangle...

    #finding a range where we can place the rectangle:

    rec_range = np.arange(-int(size/4),int(size/4))
    not_range = np.arange(-int(size/8),int(size/8)) #where we don't want the rectangle to be

    #need to remove not_range from rec_range first

    for i in rec_range:
        if i in not_range:
            np.delete(rec_range,i)

    #then we find the first corner 

    rec_x = random.choice(rec_range)
    rec_y = random.choice(rec_range)

    #finding the second corner using a function:

    draw = ImageDraw.Draw(image)

    #actually drawing the rectangle
    
    draw.rectangle(xy=(rec_x+size/2,
                        rec_y+size/2,
                        rectangle_corner(rec_x,rec_y,size)),
                        fill=(rec_colour))


    #drawing the spiral:

    #setting up another function...

    #variables for this function:

    b = random.choice(np.arange(0,1,0.01))
    c = random.choice(np.arange(0,1,0.01))

    points = []

    #adding thickness in some direction vertical or horizontal:

    x_or_y = random.randint(0,1)

    #plotting over an angle range of 0 - 10pi

    for i in np.arange(0,10*pi,0.0001*pi):

        (x,y) = spiral_function(size/2.2,b,c,i,size)
        points.append((x,y))

        image.putpixel((int(x),int(y)),value=(line_colour))

        for j in range(1,5):
            if x_or_y == 0:
                image.putpixel((int(x) + j,int(y)),value=(line_colour))

            else:
                image.putpixel((int(x),int(y) + j),value=(line_colour))


    image.resize((target_size,target_size),resample=Image.ANTIALIAS)

    image.save(f"{os.path.abspath(os.getcwd())}/Spiral/Images/image{n}.png")


for i in range(0,20):
    generate_spiral(i)
