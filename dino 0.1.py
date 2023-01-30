import pygame
pygame.init()

win = pygame.display.set_mode((680, 350))
pygame.display.set_caption('Első játékom')

x = 100
y = 50
m = 5
width = 20
height = 15

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

        if pygame.key.get_pressed()[pygame.K_a] and x > m:
            x -= m

        if pygame.key.get_pressed()[pygame.K_d] and x < 680 - m - width:
            x += m

        if pygame.key.get_pressed()[pygame.K_w] and y > m:
            y -= m

        if pygame.key.get_pressed()[pygame.K_s] and y < 350 - height - m :
            y += m

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (0,255,0), (x, y, width, height))
        pygame.display.update()
            

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()


pygame.quit()

# Alapvető mozdulatok
