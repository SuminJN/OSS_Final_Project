import pygame
import random

pygame.init()  #Pygame Initialization

BLACK = (0, 0, 0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
size = [400, 600]
screen = pygame.display.set_mode(size)

def runGame():
    bomb_image = pygame.image.load('bomb.png')
    bomb_image = pygame.transform.scale(bomb_image, (50, 50))

    character_image = pygame.image.load('character.png')
    character_image = pygame.transform.scale(character_image, (50, 50))

runGame()
pygame.quit()
