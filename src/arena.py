import pygame
import time
from os.path import join as path_join
from spritesheet import Spritesheet

class Arena():

    ANIMATION_FRAMES = 4
    IMAGE_FILENAME = path_join('resources', 'map_spritesheet.png')
    MAP_WIDTH = 420
    MAP_HEIGHT = 210

    def __init__(self):
        ss = Spritesheet(Arena.IMAGE_FILENAME, Arena.MAP_WIDTH)
        self.start_frame = time.time()
        self.fps = 12
        self.index = 0
        self.images = ss.get_images()
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, Arena.MAP_WIDTH, Arena.MAP_HEIGHT)

    def update(self):
        # Map animation should be independant from the rest of the sprites.
        self.index = int((time.time() - self.start_frame) * self.fps % Arena.ANIMATION_FRAMES)
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
