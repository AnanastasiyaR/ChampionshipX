import pygame
pygame.init()
W=800
H=800
background_position = [0, 0]
dis=pygame.display.set_mode((300,300))
sc = pygame.display.set_mode((W, H))
#sc.fill((220, 220, 220))
screen = pygame.display.set_mode([800, 600])
#фон
clock = pygame.time.Clock()
background_image = pygame.image.load('shema2.png')
#иконка светофора
gameIcon = pygame.image.load('TLred.png')
pygame.display.set_icon(gameIcon)

pygame.display.update()
pygame.display.set_caption('World Skills X')
#машинка
surf = pygame.image.load('BCvertical.png')
rect = surf.get_rect(bottomright=(W/2, H/2))
sc.blit(surf, rect)
 
pygame.display.update()
game_over=False

while not game_over:
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        game_over=True       # выводит на экран все действия игры
          #dis.blit(background_image, (0, 0))
          #clock.tick(60)
    screen.blit(background_image, background_position)  
    
    pygame.display.update()
    
pygame.quit()
quit()





