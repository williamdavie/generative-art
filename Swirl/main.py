from PIL import Image, ImageDraw, ImageChops
import random
import numpy as np
from math import *
import colorsys
import os

from functions.generate_points import *
from functions.hsv_to_rgb import *
from functions.random_hsv import *

def generate_art(n):
    print("Generating")
    target_size = 256
    scale_factor = 6
    size = target_size * scale_factor
    colour1_hsv = random_hsv()
    if colour1_hsv[0] > 0.66:
        colour2_h = colour1_hsv[0] - 0.33
        colour3_h = colour1_hsv[0] - 0.66
    
    elif colour1_hsv[0] < 0.33:
        colour2_h = colour1_hsv[0] + 0.33
        colour3_h = colour1_hsv[0] + 0.66

    else:
        colour2_h = colour1_hsv[0] + 0.33
        colour3_h = colour1_hsv[0] - 0.33

    colour1 = hsv_to_rgb(colour1_hsv[0],colour1_hsv[1],colour1_hsv[2])
    colour2 = hsv_to_rgb(colour2_h,colour1_hsv[1],colour1_hsv[2])
    colour3 = hsv_to_rgb(colour3_h,0.5,0.1)

    image = Image.new("RGB", (size,size),(colour3))
    image2 = image

    draw = ImageDraw.Draw(image)


    ran_range = random.randint(2,5)
    colours = [colour1,colour2,colour3]

    for z in range(1,ran_range):

        all_points = []

        random_x = random.randint(size/8,7*size/8)
        random_y = random.randint(size/8,7*size/8) 


        random_angle_range = random.randint(180,2160)

        range1 = np.arange(150,750)
        range2 = np.arange(-250,-150)

        choice = random.randint(1,2)
        if choice == 1:
            random_magnitude = random.choice(range1) * scale_factor/2
        else: 
            random_magnitude = random.choice(range2) * scale_factor/2

        points = generate_points(random_magnitude,random_angle_range)

        colour_choice = random.randint(1,2)
        if colour_choice == 1:
            random_colour = colour1
        if colour_choice == 2:
            random_colour = colour2

        for i in points:
            x = int(i[0] + random_x)
            y = int(i[1] + random_y) 

            if x > 0 and x < size and y > 0 and y < size :
                image.putpixel((x,y),value=(random_colour))
                all_points.append((x,y))


        thickness = 2
        for i in all_points:
            for j in range(0,thickness):
                if i[0] < (size - j) and i[0] > (0 + j) and i[1] < (size - j) and i[1] > (0 + j):
                    image.putpixel((i[0]+j,i[1]+j),value=(random_colour))
                    image.putpixel((i[0]-j,i[1]-j),value=(random_colour))
                    image.putpixel((i[0]+j,i[1]-j),value=(random_colour))
                    image.putpixel((i[0]-j,i[1]+j),value=(random_colour))
                    image.putpixel((i[0]+j,i[1]),value=(random_colour))
                    image.putpixel((i[0]-j,i[1]),value=(random_colour))
                    image.putpixel((i[0],i[1]+j),value=(random_colour))
                    image.putpixel((i[0],i[1]-j),value=(random_colour))

    image.resize((target_size,target_size),resample=Image.ANTIALIAS)

    image.save(f"{os.path.abspath(os.getcwd())}/Swirl/Images/image{n}.png")



for i in range(0,10):
    generate_art(i)