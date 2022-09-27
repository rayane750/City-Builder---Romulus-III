
import pygame as pg
import random
from game.model.case import Case
from game.model.settings import TILE_SIZE



class World:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.grass_tiles = pg.Surface((grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha() #
        self.tiles = self.load_images()
        self.world = self.create_world()

    def create_world(self):

        world = []

        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

                render_pos = world_tile.get_render_pos()
                self.grass_tiles.blit(self.tiles["block"], (render_pos[0] + self.grass_tiles.get_width()/2, render_pos[1])) #
                self.grass_tiles.blit(self.tiles["block"], (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))

        return world

    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        r = random.randint(1, 1000)

        if r <= 50 and r > 5:
            tile = "tree1"
        elif r <= 100 and r >= 50:
            tile = "tree2"
        elif r <= 150 and r >= 100:
            tile = "tree3"
        #elif r <= 1:
        #    tile = "farm"
        else:
            tile = ""

        out = Case([grid_x,grid_y],rect,iso_poly,[minx,miny],tile)

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):

        block = pg.image.load("C3_sprites/C3/Land1a_00002.png")
        tree1 = pg.image.load("C3_sprites/C3/Land1a_00045.png")
        tree2 = pg.image.load("C3_sprites/C3/Land1a_00054.png")
        tree3 = pg.image.load("C3_sprites/C3/Land1a_00059.png")
        farm = pg.image.load("C3_sprites/C3/Security_00053.png")

        return {"block": block, "tree1": tree1, "tree2": tree2, "tree3": tree3, "farm": farm}

    def get_case(self,i,j):
        return self.world[i][j]
