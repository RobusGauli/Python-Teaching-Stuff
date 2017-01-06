class Particle:
    
    def __init__(self, pos, vel, acc=None):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        
    def show(self):
        ellipse(self.pos.x, self.pos.y, 60, 60)
        
    def move(self):
        self.pos.x = self.pos.x + self.vel.x
        self.pos.y = self.pos.y + self.vel.y
    
    def bounce(self):
        if self.pos.x > width or self.pos.x < 0:
            self.vel.x = self.vel.x * -1
            
        if self.pos.y > height or self.pos.y < 0:
            self.vel.y = self.vel.y * -1
            