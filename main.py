import pygame
import sys
from game import Game
pygame.init()
screen = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()
#We need the pictures here:
game = Game('img/character.png')
game.resize_images()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                game.shoot()        
            if event.key == pygame.K_SPACE and game.active == False:
                game.restart()
    if game.active:
        game.show_character(screen)
        game.turn_character() 
