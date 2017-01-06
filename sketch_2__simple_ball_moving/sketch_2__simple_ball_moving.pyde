#a simple program that shows the velocity and how velocity works
#velocity is simply a vector that represents the rate of change in position
pos_x = None
pos_y = None
def setup():
    global pos_x, pos_y
    size(600, 600)
    pos_x = width/2
    pos_y = height/2
    
def draw():
    global pos_x, pos_y
    background(0)
    ellipse(pos_x, pos_y, 45, 45)
    
    
    ##increment the pos_x by 3
    pos_x = pos_x + 3
    #pos_y = pos_y + 1
    
    if pos_x > width - 45/2:
        pos_x = 0
    elif pos_y < 0:
        pos_x = width
    
    