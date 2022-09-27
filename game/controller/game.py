import pygame as pg

from game.view.utils import draw_text
from game.model.world import World
from game.model.settings import TILE_SIZE
from game.controller.camera import Camera
from game.controller.keyboard import keyboard

class Game:

    def __init__(self, screen, clock):
        self.keyboard = keyboard(self)
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.state = 2
        self.playing = True

        # world
        self.world = World(65, 65, self.width, self.height)

        # camera
        self.camera = Camera(self.width, self.height)



    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.draw()
            self.keyboard.notify()
            self.update()

    def set_playing(self,bool):
        self.playing = bool

    def update(self):
        self.camera.update()

    def get_state(self):
        return self.state

    def set_state(self,state):
        self.state = state

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.world.grass_tiles, (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):

                # sq = self.world.world[x][y]["cart_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                # pg.draw.rect(self.screen, (0, 0, 255), rect, 1)

                render_pos =  self.world.world[x][y].get_render_pos()
                #self.screen.blit(self.world.tiles["block"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))

                tile = self.world.world[x][y].get_tile()
                if tile != "":
                    self.screen.blit(self.world.tiles[tile],
                                    (render_pos[0] + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x,
                                     render_pos[1] - (self.world.tiles[tile].get_height() - TILE_SIZE) + self.camera.scroll.y))

                # p = self.world.world[x][y]["iso_poly"]
                # p = [(x + self.width/2, y + self.height/4) for x, y in p]
                # pg.draw.polygon(self.screen, (255, 0, 0), p, 1)

        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )

        pg.display.flip()
