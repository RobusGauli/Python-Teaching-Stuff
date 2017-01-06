#bouncing ball
x_pos = None
y_pos = None

x_vel = None
y_vel = None
def setup():
    size(400, 400)
    global x_pos, y_pos, x_vel, y_vel
    x_pos = width/2
    y_pos = height/2
    
    x_vel = 3
    y_vel = 2
    
def draw():
    global x_pos, y_pos, x_vel, y_vel
    background(0)
    #drawin the ellipse
    ellipse(x_pos, y_pos, 45, 45)
    
    #applying a velocity
    x_pos = x_pos + x_vel
    y_pos = y_pos + y_vel
    
    if x_pos > width or x_pos < 0:
        x_vel = x_vel * -1
        
    if y_pos > height or y_pos < 0:
        y_vel = y_vel * -1
        
    
    