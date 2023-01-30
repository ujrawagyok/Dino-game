import pygame
pygame.init()

kezdo = pygame.image.load('kezdes.png')
bg = pygame.image.load('bgpi.jpg')
bg = pygame.transform.scale(bg, (680, 350 ))
win = pygame.display.set_mode((680, 350))
pygame.display.set_caption('Első játékom')

x = 100
y = 300
m = 5
width = 30
height = 40
ugras = False
um = 10
dead = False

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if not (ugras):
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP] and y > m:
            ugras = True
            
    else:
        if um  >= -10:
            pygame.time.delay(10)
            neg = 1
            if um < 0:
                pygame.time.delay(20)
                neg = -1
            y -=(um **2)* 0.5 * neg
            um -= 1
        else:
            ugras = False
            um = 10

    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()
                        

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.QUIT()


pygame.quit()