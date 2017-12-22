import pygame

class Spritesheet():
    """
    Class to handle Spritesheets. Make sure the width is the same for all sprites in the sheet.
    """
    def __init__(self, filename, sprite_width):
        self.spritesheet = pygame.image.load(filename).convert_alpha()
        self.sprite_width = sprite_width
        self.number_sprites = self.spritesheet.get_width() / sprite_width

    def get_image(self, index):
        """
        Returns an image from the spritesheed based on the provided index
        """
        if index >= self.number_sprites:
            raise ValueError('Sprite {} was requested. Not available'.format(index))
        rect = pygame.Rect(self.sprite_width * index,
                           0,
                           self.sprite_width,
                           self.spritesheet.get_height())

        image = pygame.surface.Surface(rect.size)
        image.set_colorkey(pygame.color.Color('black'))
        image.blit(self.spritesheet, (0, 0), rect)

        return image

    def get_images(self):
        """
        Returns a list of individual sprites from the spritesheet image
        """
        return [self.get_image(i) for i in range(0, self.number_sprites - 1)]

