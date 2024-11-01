import pygame, simpleGE, random
#zombie brain catcher
class Zombie(simpleGE.Sprite):
    def __int__(self, scene):
        super().__init__(scene)
        self.image("zombie.png")
        self.setsize(50,50)
        self.position = (320,400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
class Brain(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("brain.png")
        self.setSize (25,25)
        self.minSpeed = 3
        self.maxspeed = 8
        self.reset()
        
   def reset (self):
        self.x = random.randint (0, self.screenWidth)
        self.y = 0
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    #def checkbounds(self):
        #if self
class game(simpleGE.Sprite):
    def __int__(self):
        super().__init__()