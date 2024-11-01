import pygame, random, simpleGE

#zombie catcher

class brain(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("brian.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class zombie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("zombie.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
         def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("train.jpg")
        
        self.zombie = zombie(self)
        self.brain = brain(self)
        
        self.sprites = [self.zombie,
                        self.brain]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()