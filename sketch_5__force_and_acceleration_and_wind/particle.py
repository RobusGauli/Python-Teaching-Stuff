class Particle:
    
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        
    def show(self):
        ellipse(self.pos.x, self.pos.y, 40, 40)
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc.mult(0)
        self.vel.limit(15)
        
    def applyForce(self, vector):
        self.acc.add(vector)
        
    def bounce(self):
        if self.pos.x > width or self.pos.x < 0:
            self.vel.x = self.vel.x * -1
        if self.pos.y > height or self.pos.y < 0:
            self.vel.y = self.vel.y * -1
        
    