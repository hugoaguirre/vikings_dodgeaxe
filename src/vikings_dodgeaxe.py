import sys
import pygame
from spritesheet import Spritesheet
from arena import Arena

def run_game():
    #Init game
    pygame.init()
    screen = pygame.display.set_mode((420, 210))

    arena = Arena()
    clock = pygame.time.Clock()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        #arena.update() iterates over the arena spritesheet changing arena sprite over time
        arena.update()
        screen.blit(arena.image, (0, 0))
        pygame.display.flip()
        clock.tick(60)

run_game()
