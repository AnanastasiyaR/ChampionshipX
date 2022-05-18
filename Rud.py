import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
import time

pygame.init()
#pygame.display.set_mode

W=55
H=545
W1=170
H1=545
W2=170
H2=545
background_position = [0, 0]
dis=pygame.display.set_mode((1134,850))
sc = pygame.display.set_mode((W, H))
window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
#sc.fill((220, 220, 220))

#кнопки, цвета
win = pygame.display.set_mode((100, 100))
pin = pygame.display.set_mode((200, 200))

# Creates the button with optional parameters
#print('green')
#image= pygame.image.load('VagonBlock.png')
button = Button(win, 150, 5, 50, 50, inactiveColour=(200, 50, 0),  hoverColour=(150, 0, 0), pressedColour=(100, 0, 0),  radius=20, onClick=lambda: sc.blit(tlred, rect1) )

button1 = Button(pin, 150, 5, 50, 50,  inactiveColour=(0, 200, 0),  hoverColour=(150, 0, 0), pressedColour=(0, 100, 20),  radius=20, onClick=lambda: sc.blit(tlgreen, rect2) )
     
# размер окна!!!!!!
screen = pygame.display.set_mode([753, 729]) 
#фон
clock = pygame.time.Clock()
timer = 10  # Decrease this to count down.
dt = 5

background_image = pygame.image.load('shema2.png')
#иконка светофора
gameIcon = pygame.image.load('TLred.png')
pygame.display.set_icon(gameIcon)

pygame.display.update()
pygame.display.set_caption('World Skills X')
#машинка
surf = pygame.image.load('BCright.png')
rect = surf.get_rect(bottomright=(W, H))
sc.blit(surf, rect)
#red
tlred = pygame.image.load('TLred.png')
rect1 = tlred.get_rect(bottomright=(W1, H1))
sc.blit(tlred, rect1)
#green
tlgreen = pygame.image.load('TLgreen1.png')
rect2 = tlred.get_rect(bottomright=(W2, H2))
sc.blit(tlgreen, rect2)
 
pygame.display.update()
game_over=False

while not game_over:
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        game_over=True       # выводит на экран все действия игры
          
    #таймер(?)
    x=0
    screen.blit(background_image, background_position) 
    #win.fill((255, 255, 255))
  
    pygame_widgets.update(event) 
    pygame.display.update()
    sc.blit(surf, rect)
   # while x < 11:
   # pygame.time.delay(1000)
   # if x <= dt:
    #  sc.blit(tlgreen, rect2) 
   #   x=x+1
    #  pygame.display.update()
  #  if x>dt:
   #   sc.blit(tlred, rect1)
   #   x=x+1
  #    pygame.display.update()
   # if x==timer:
   #   sc.blit(tlred, rect1)
   
    #  x=0

    pygame.display.update()
    

    
pygame.quit()






