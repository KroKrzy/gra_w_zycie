from komorka import *
from plansza import Plansza
import time
import pygame


zapis = True
field = Plansza(k, l)



field.drawGrid()

while (field.zapis):
    field.input()
    plansza[int(field.temp[0]/15+1)][int(field.temp[1]/15+1)].zyje = True


while (True):
    
    field.work()
    
    for i in range (1,n+1):
        for j in range (1,m+1):
            plansza[i][j].liczsasiadow()
        
    for i in range (1,n+1):
        for j in range (1,m+1):
            plansza[i][j].czy_zyje()
            
    
           
    field.screen.fill((0,0,0))
    myimage = pygame.image.load("temp.jpeg").convert_alpha()
    field.screen.blit(myimage,myimage.get_rect())
    for i in range(1,n+1):
        for j in range(1,m+1):
            if plansza[i][j].zyje:
                field.drawRect([(i-1)*15,(j-1)*15])
    time.sleep(0.5)
