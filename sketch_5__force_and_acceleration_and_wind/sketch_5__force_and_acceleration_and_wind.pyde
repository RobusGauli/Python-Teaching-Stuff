from particle import Particle

par = None

def setup():
    global par
    size(600, 600)
    par = Particle()
        
def draw():
    background(0)
    par.show()
    par.update()
    par.bounce()
    
    #create a gravity
    gravity = PVector(0, 0.2)
    par.applyForce(gravity)
    
    if mousePressed:
        wind = PVector(0.4, 0)
        par.applyForce(wind)
    
    
    