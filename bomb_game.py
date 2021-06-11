import pygame  
import random

pygame.init()  # pygame initialization


# global variable
BLACK = (0,0,0)
size = [700, 800] # Set the height and width of the screen
screen = pygame.display.set_mode(size)
game_font = pygame.font.Font(None, 150)
background_image = pygame.image.load('background.png')

done = False
clock = pygame.time.Clock()

# runGame Function
def runGame():

    # Set bombs
    bomb_image = pygame.image.load('bomb.png')
    bomb_image = pygame.transform.scale(bomb_image, (60, 60))
    bombs = []

    for i in range(7):
        rect = pygame.Rect(bomb_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        bombs.append({'rect': rect, 'dy': dy})

    # Set character
    character_image = pygame.image.load('character.png')
    character_image = pygame.transform.scale(character_image, (100, 100))
    character = pygame.Rect(character_image.get_rect())

    character.left = size[0] // 2 - character.width // 2
    character.top = size[1] - character.height - 180
    character_dx = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)
        screen.blit(background_image, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_dx = -7
                elif event.key == pygame.K_RIGHT:
                    character_dx = 7
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    character_dx = 0
                elif event.key == pygame.K_RIGHT:
                    character_dx = 0

        for bomb in bombs:
            bomb['rect'].top += bomb['dy']
            if bomb['rect'].top > size[1]:
                bombs.remove(bomb)
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                bombs.append({'rect': rect, 'dy': dy})

        character.left = character.left + character_dx

        if character.left < 0:
            character.left = 0
        elif character.left > size[0] - character.width:
            character.left = size[0] - character.width

        screen.blit(character_image, character)

        # Check for bomb-character collisions
        for bomb in bombs:
            if bomb['rect'].colliderect(character): 
                done = True
            screen.blit(bomb_image, bomb['rect'])

        pygame.display.update()


runGame()

# Game Over
msg = game_font.render("Game Over", True, (255, 100, 100))
msg_rect = msg.get_rect(center=(int(size[0] / 2), int(size[1] / 3)))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()