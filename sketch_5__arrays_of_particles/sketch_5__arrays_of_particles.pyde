from particle import Particle

particles = []

def setup():
    global par
    size(600, 600)
    for i in range(15):
        particles.append(Particle())
        
def draw():
    background(0)
    for particle in particles:
        particle.show()
        particle.update()
        particle.bounce()
        
        particle.applyForce(PVector(0, 0.2))
        if mousePressed:
            particle.applyForce(PVector(0.3, 0))
        
        

    #create a gravity

    

    