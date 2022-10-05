from math import *

def spiral_function(a,b,c,angle,size):
    #this will be a mathematical function that uses polar co-ordinates and returns our desired pattern

    x = a*(sin(b*angle)**2)*(cos(c*angle)**2)*cos(angle)
    y = a*(sin(b*angle)**2)*(cos(c*angle)**2)*sin(angle)

    return (round(x) + size/2,round(y) + size/2)