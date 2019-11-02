import pygame
from paddle import Paddle

def pongWindow():
    pygame.init()

    #Set game colours
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    #Define window size
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")

def paddles():
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200

    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 670
    paddleB.rect.y = 200

def mainGame():
    carryOn = True

    clock = pygame.time.Clock()

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    pygame.display.flip()

    clock.tick(60)

    pygame.quit()


if __name__ =="__main__":
    pongWindow()