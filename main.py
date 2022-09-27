
import pygame as pg
from game.controller.game import Game
from game.controller.camera import Camera


def main():

    running = True
    playing = True

    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((900, 700))
    clock = pg.time.Clock()

    # implement menus

    # implement game
    game = Game(screen, clock)
    # setup 
    camera_group = Camera
    
    while running:
        
        # start menu goes here

        while playing:
            # game loop here
            game.run()
            playing = False
        running = False

if __name__ == "__main__":
    main()
