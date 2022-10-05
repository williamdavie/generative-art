import random

def random_hsv():
    h = random.random()
    s = random.randint(7,10) / 10
    v = 1
    
    return h,s,v