import sys
import pygame
from spritesheet import Spritesheet
from player import Player
from arena import Arena

def run_game():
    #Init game
    pygame.init()
    screen = pygame.display.set_mode((420, 210))

    arena = Arena()
    player = Player()
    clock = pygame.time.Clock()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Player directions
        pressed_keys = pygame.key.get_pressed()
        player.move(pressed_keys);

        arena.update()
        player.update()
        screen.blit(arena.image, (0, 0))
        # Draw player at calculated position
        screen.blit(player.image, (player.pos_x, player.pos_y))
        pygame.display.update()
        clock.tick(60)

run_game()
