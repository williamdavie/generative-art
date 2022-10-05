
def point_to_rec(x,y,width,height):
    top_x = x - width/2
    top_y = y - height/2

    bottom_x = x + width/2
    bottom_y = y + height/2 

    return top_x,top_y,bottom_x,bottom_y