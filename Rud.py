import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
import random
import time
from pygame.locals import *
#import pygame_menu



######################
pygame.init()
#pygame.display.set_mode

FPS=30
fpsClock = pygame.time.Clock()
win = pygame.display.set_mode((30, 50))
pin = pygame.display.set_mode((200, 200))

#координаты (ширина/высота)
W=45
H=545
Wr=430
Hr=50
Wgr=45
Hgr=370
Wpr=570
Hpr=50
W1=170
H1=545
W2=170
H2=545
background_position = [0, 0]
dis=pygame.display.set_mode((1134,850))
sc = pygame.display.set_mode((W, H))
window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

# размер окна!!!!!!
screen = pygame.display.set_mode([730, 750]) 
#фон
clock = pygame.time.Clock()
timer = 10  
dt = 5
#задний фон
background_image = pygame.image.load('shemanew.png')
#иконка светофора
gameIcon = pygame.image.load('TLred.png')
pygame.display.set_icon(gameIcon)
pygame.display.update()
#название приложение
pygame.display.set_caption('World Skills X')
#машинка 
surf = pygame.image.load('BCright.png')
rect = surf.get_rect(bottomright=(W, H))
sc.blit(surf, rect)
#красная машинка 
surfred = pygame.image.load('Cbottom.png')
rectred = surfred.get_rect(bottomright=(Wr, Hr))
sc.blit(surfred, rectred)
#грузовая машинка 
surfgruz = pygame.image.load('Truck.png')
rectgruz = surfgruz.get_rect(bottomright=(Wgr, Hgr))
sc.blit(surfgruz, rectgruz)
#с прицепом машинка 
surfpr =pygame.transform.rotate(pygame.image.load('Trailer.png'), 180)
rectpr = surfpr.get_rect(bottomright=(Wpr, Hpr))
sc.blit(surfpr, rectpr)
#red
#pygame.transform.rotate(image, degree)
tlred = pygame.image.load('TLred.png')
rect1 = tlred.get_rect(bottomright=(W1, H1))
sc.blit(tlred, rect1)
#green
#tlgreen = pygame.image.load('TLgreen1.png')
#rect2 = tlgreen.get_rect(bottomright=(W2, H2))
#sc.blit(tlgreen, rect2)
#кнопки, цвета

button = Button(win, 470, 245, 50, 50, inactiveColour=(200, 50, 0),  hoverColour=(150, 0, 0), pressedColour=(100, 0, 0),  radius=20, onClick=lambda: sc.blit(tlred, rect1) )
button1 = Button(pin, 470, 5, 50, 50,  inactiveColour=(0, 200, 0),  hoverColour=(0, 150, 0), pressedColour=(0, 100, 20), margin=20,  radius=20, onClick=lambda: sc.blit(tlred, rect1) ) 

pygame.display.update()
game_over=False



while not game_over:

   for event in pygame.event.get():
    if event.type==pygame.QUIT:
      game_over=True# выводит на экран все действия игры
    
   screen.blit(background_image, background_position) 
   pygame_widgets.update(event) 
   sc.blit(surf, rect)
   sc.blit(surfred, rectred)
   sc.blit(surfgruz, rectgruz)
   sc.blit(surfpr, rectpr)
   pygame.display.update()
    

    
pygame.quit()






