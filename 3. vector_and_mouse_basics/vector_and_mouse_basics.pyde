# a simple illustration of vector and how vector needs t make sense
mouse_vec = None

def setup():
    global mouse_vec
    
    size(600, 600)
    mouse_vec = PVector(0, 0)
def draw():
    global mouse_vec
    background(255)
    mouse_vec.x = mouseX
    mouse_vec.y = mouseY
    # mouse_vec.normalize()
    # mouse_vec.mult(80)
    

    
    fill(255)
    line(0, 0, mouse_vec.x, mouse_vec.y)
    fill(0)
    rect(0, 0, mouse_vec.mag(), 34)  
    print(mouse_vec.heading())  