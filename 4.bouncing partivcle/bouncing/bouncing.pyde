#doing the same thing using the concept of OOP
from particle import Particle

particle = None
def setup():
    size(400, 400)
    #lets create a vector wth x and y
    pos = PVector(random(width), random(height))
    vel = PVector(2, 3)
    
    #using the particle
    global particle
    particle = Particle(pos, vel)
    
    
def draw():
    background(0, 200)
    global particle
    particle.show()
    particle.move()
    particle.bounce()