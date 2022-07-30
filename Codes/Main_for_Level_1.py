import pygame, sys
from Settings_for_Level_1  import *
from Level_for_Level_1 import Level
from GameData_for_Level_1 import level_1

#pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_1,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        screen.fill('black')
        level .run()

        pygame.display.update()
        clock.tick(60)