from tkinter.tix import Tree
import pygame
from Support_for_Level_1 import import_csv_layout, import_cut_graphics
from Settings_for_Level_1 import tile_size, screen_height
from Tiles_for_Level_1 import Tile, StaticTile, Coin
from Enemy_for_Level_1 import Enemy
from Decoration_for_Level_1 import Sky, Water, Clouds

class Level:
    def __init__(self,level_data,surface):
        # General Setup
        self.display_surface = surface
        self.world_shift = 0

        #player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        #player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # terrain setup 
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

        #coins
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout, 'coins')

        #bg trees
        bg_palm_layout = import_csv_layout(level_data['bg trees'])
        self.bg_palm_sprites = self.create_tile_group(bg_palm_layout, 'bg trees')

        #enemy
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

        #constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constrant_sprites = self.create_tile_group(constraint_layout, 'constraint')

        #decoration
        self.sky = Sky(8)
        level_width = len(terrain_layout[0]) * tile_size
        self.water = Water(screen_height - 40,level_width)
        self.clouds = Clouds(400,level_width,20)


    def create_tile_group(self,layout,type):


        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('../Graphics/Treasure Hunters/Palm Tree Island/Sprites/Terrain/Terrain (32x32).png')
                        print(val)
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                        sprite_group.add(sprite)
 
                    if type == 'coins':
                        if val == '0': sprite = Coin(tile_size,x,y,'../Graphics/Treasure Hunters/Pirate Treasure/Sprites/Gold Coin/01.png')

                    if type == 'bg trees':
                        sprite = Tree(tile_size,x,y,'../Graphics/Treasure Hunters/Palm Tree Island/Sprites/Back Palm Trees/Back Palm Tree Regular 01.png',64)

                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y)

                    if type == 'constraint':
                        sprite = Tile(tile_size,x,y)

                    sprite_group.add(sprite)
        
        return sprite_group

    def player_setup(self,layout):
         for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                   print('Player goes here')
                if val == '1':
                    hat_surface = pygame.image.load('../Graphics/setup_tiles.png').convert_alpha()
                    sprite = StaticTile(tile_size,x,y,hat_surface)
                    self.goal.add(sprite)
        
    
    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprites.spritescollide(enemy,self.constraint_sprites,False):
                enemy.reverse()
    
    def run(self):
        # run the entire game / level
        
        #sky
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface,self.world_shift)

        #bg palms
        self.bg_palm_sprites.update(self.world_shift)
        self.bg_palm_sprites.draw(self.display_surface)

        #terrain
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)

        #enemy
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface) 
   

        #coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites(self.display_surface)

        #player sprites
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        #water
        self.water.draw(self.display_surface,self.world_shift)

      
       