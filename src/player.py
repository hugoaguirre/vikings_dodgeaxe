import pygame
from os.path import join as path_join

from spritesheet import Spritesheet

class Player():
    IMAGE_FILENAME = path_join('resources', 'player_spritesheet.png')
    PLAYER_WIDTH = 16
    PLAYER_HEIGHT = 16
    SPEED = 3

    def __init__(self):
        ss = Spritesheet(Player.IMAGE_FILENAME, Player.PLAYER_WIDTH)
        self.index = 0
        self.images = ss.get_images()
        self.image = self.images[self.index]
        self.pos_x = 100
        self.pos_y = 100
        self.rect = pygame.Rect(0, 0, Player.PLAYER_WIDTH, Player.PLAYER_HEIGHT)

    def move(self, pressed_keys):
        old_pos_x = self.pos_x
        old_pos_y = self.pos_y

        if pressed_keys[pygame.K_w]:
            self.pos_y -= Player.SPEED
        elif pressed_keys[pygame.K_a]:
            self.pos_x -= Player.SPEED
        elif pressed_keys[pygame.K_s]:
            self.pos_y += Player.SPEED
        elif pressed_keys[pygame.K_d]:
            self.pos_x += Player.SPEED
        else:
            pass

        if self.pos_x < 0:
            self.pos_x = 0
        elif self.pos_x > 420 - self.image.get_width():
            self.pos_x = 420 - self.image.get_width()

        if self.pos_y < 0:
            self.pos_y = 0
        elif self.pos_y > 210 - self.image.get_height():
            self.pos_y = 210 - self.image.get_height()

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1

