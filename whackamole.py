import pygame
import random

def main():
    try:

        
      
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        x = random.randint(0,19)
        y = random.randint(0,15)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    clickX, ClickY = event.pos[0] // 32, event.pos[1] // 32
                    if (clickX, ClickY) == (x,y):
                        x = random.randint(0,19)
                        y = random.randint(0,15)

                
            screen.fill("light green")
            screenSize = 32
            for i in range(21):
                pygame.draw.line(screen, 'dark blue', (screenSize, 0), (screenSize,512))
                screenSize += 32

            screenSize = 32
            for i in range(17):
                pygame.draw.line(screen, 'dark blue', (0, screenSize), (640,screenSize))
                screenSize += 32

            # random.randrange(640, 512,32)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32, y * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
