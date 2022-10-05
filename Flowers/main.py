from PIL import Image, ImageDraw 
import random
import numpy as np
from math import *
import colorsys
import os

from functions.find_rectangle import *
from functions.point_to_rectangle import *
from functions.random_colour import *


def generate_flower(n):
    print("Generating")
    target_size = 256
    scale_factor = 4
    size = target_size * scale_factor
    bg_colour = random_colour(0.1)
    stem_colour = (102,200,63)
    image = Image.new("RGB", (size,size),bg_colour)

    draw = ImageDraw.Draw(image)

    #stem arcs
    for i in range(0,5):
        arc_rec = find_rectangle(size)
        start_angle = 0
        end_angle = 90
        if arc_rec[0] < size/2:
            start_angle = random.randint(180,240)
            end_angle = 360
        else:
            start_angle = 180
            end_angle = random.randint(210,270)

        draw.arc(arc_rec,start_angle,end_angle,fill=stem_colour)
    #main stem
    draw.line((size/2,size,size/2,size/2),fill=stem_colour)     

    #green points loop
    green_points = []
    for i in range(0,size):
        for j in range(0,int(size)):
            colour = image.getpixel((i,j))
            if colour == stem_colour:
                green_points.append((i,j))

    for i in green_points:
        if i[1] < size - 1:
            image.putpixel((i[0]+1,i[1]+1),value=stem_colour)
            image.putpixel((i[0]-1,i[1]-1),value=stem_colour)
            image.putpixel((i[0]+1,i[1]-1),value=stem_colour)
            image.putpixel((i[0]-1,i[1]+1),value=stem_colour)
            image.putpixel((i[0]+1,i[1]),value=stem_colour)
            image.putpixel((i[0]-1,i[1]),value=stem_colour)
            image.putpixel((i[0],i[1]+1),value=stem_colour)
            image.putpixel((i[0],i[1]-1),value=stem_colour)

    no_go = []

    for i in range(int(3*size/8),int(5*size/8)):
        for j in range(int(size/4),int(size)):
            no_go.append((i,j))

    np.array(green_points)

    for i in no_go:
        if i in green_points:
            green_points.remove(i)
    

    rang = random.randint(1,6)

    for i in range(rang):
        ran_x,ran_y = random.choice(green_points)
        width = random.randint(int(size/16),int(size/8))
        height = width

        rectangle_points = point_to_rec(ran_x,ran_y,width,height)

        draw.ellipse(rectangle_points,fill=random_colour(0.8))



    image.resize((target_size,target_size),resample=Image.ANTIALIAS)

    image.save(f"{os.path.abspath(os.getcwd())}/Flowers/Images/image{n}.png")


for i in range(0,10):
    generate_flower(i)    