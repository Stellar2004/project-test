from Tiles_for_Level_1 import AnimatedTile
from Settings_for_Level_1 import vertical_tile_number, tile_size, screen_width
import pygame
from Tiles_for_Level_1 import AnimatedTile, StaticTile
from Support_for_Level_1 import import_folder
from random import choice, randint

class Sky:
    def __init__(self,horizon):
        self.top = pygame.image.load('../Graphics/sky/sky_top.png').convert()
        self.bottom = pygame.image.load('../Graphics/sky/sky_bottom.png').convert()
        self.middle = pygame.image.load('../Graphics/sky/sky_middle.png').convert()
        self.horizon = horizon

        #stretch
        self.top = pygame.transform.scale(self.top,(screen_width,tile_size))
        self.bottom = pygame.transform.scale(self.bottom,(screen_width,tile_size))
        self.middle = pygame.transform.scale(self.middle,(screen_width,tile_size))

    def draw(self,surface):
        for row in range(vertical_tile_number):
            y = row * tile_size
            if row < self.horizon:
                surface.blit(self.top,(0,y))
            elif row == self.horizon:
                surface.blit(self.middle,(0,y))
            else:
                 surface.blit(self.bottom,(0,y))


class Water:
    def __init__(self,top,level_width):
        water_start = -screen_width
        water_tile_width = 192
        tile_x_amount = int((level_width + screen_width) / water_tile_width)
        self.water_sprites = pygame.sprite.Group()

        for tile in range(tile_x_amount):
            x = tile * water_tile_width + water_start
            y = top
            sprite = AnimatedTile(192,x,y,'../Graphics/water')
            self.water_sprites.add(sprite)

    def draw(self,surface,shift):
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)

class Clouds:
    def __init__(self,horizon,level_width,cloud_number):
        cloud_surf_list = import_folder('../Graphics/clouds')
        min_x = -screen_width
        max_x = level_width + screen_width
        min_y = 0
        max_y = horizon
        self.cloud_sprites = pygame.sprite.Group()

        for cloud in range(cloud_number):
            cloud = choice(cloud_surf_list)
            x = randint(min_x,max_x)
            y = randint(min_y,max_x)
            sprite = StaticTile(0,x,y,cloud)
            self.cloud_sprite.add(sprite)

    def draw(self,surface,shift):
        self.cliud_sprites.update(shift)
        self.cloud_sprites.draw(surface)

                
            
