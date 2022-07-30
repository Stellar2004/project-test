import pygame
from Support_for_Level_1 import import_csv_layout, import_cut_graphics
from Settings_for_Level_1 import tile_size
from Tiles_for_Level_1 import Tile, StaticTile

class Level:
    def __init__(self,level_data,surface):
        # General Setup
        self.display_surface = surface
        self.world_shift = 0
        
        # terrain setup 
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('../CS Game Project/Graphics/Treasure Hunters/Palm Tree Island/Sprites/Terrain/Terrain (32x32).png')
                        print(val)
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                        sprite_group.add(sprite)



        return sprite_group
 
    def run(self):
        # run the entire game / level
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift) 
    