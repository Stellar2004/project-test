import pygame
from Tiles_for_Level_1 import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    def __init(self,size,x,y):
        super().__init__(size,x,y,'../CS Game Project/Graphics/Treasure Hunters/The Crusty Crew/Sprites/Fierce Tooth/02-Run/Run 01.png')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3,5)

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image,True,False)

    def reverse(self):
        self.speed *= -1


    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()

