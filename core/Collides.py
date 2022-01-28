import math
class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 
        
    def update_point(self,pos):
        self.x, self.y = pos
        
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def distance(self, p):
        return math.sqrt(abs(p.x - self.x)**2 + abs(p.y - self.y)**2)
    
class Rect:
    def __init__(self, p, w = 0, h = 0):
        self.p = p
        self.w = w
        self.h = h
        
    def collide(self, r):
        # calculamos los valores de los lados
        left = self.p.x
        right = self.p.y + self.w
        top = self.p.y + self.h
        bottom = self.p.y
        r_left = r.p.x
        r_right = r.p.x + r.w
        r_top = r.p.y + r.h
        r_bottom = r.p.y
        return right >= r_left and left <= r_right and top >= r_bottom and bottom <= r_top
    
class Circ:
    def __init__(self, p, r):
        self.p = p
        self.r = r
        
    def update(self,pos,r):
        self.p.update_point(pos)
        self.r = r
        
    def collide(self, c):
        return self.r + c.r > self.p.distance(c.p)
    
    