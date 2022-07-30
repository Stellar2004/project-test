from csv import reader
from Settings_for_Level_1 import tile_size
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map,delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map 
            
def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_number_x = int(surface.get_size()[0] / tile_size)
    tile_number_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_number_y):
        for col in range(tile_number_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size))
            new_surf.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size))
            cut_tiles.append(new_surf)
        
        
        return cut_tiles