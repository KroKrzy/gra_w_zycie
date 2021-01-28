import pygame
import sys



class Plansza:
    def __init__(self, n, m):
        pygame.init()
        self.zapis = True
        self.wysokosc_Okna = m
        self.szerokosc_Okna = n
        self.rozmiar_Kratki = 15
        self.screen = pygame.display.set_mode((self.szerokosc_Okna, self.wysokosc_Okna))
        self.temp = [0,0]
    def mouse_position(self):
        mousePos = pygame.mouse.get_pos()
        x = mousePos[0]
        y = mousePos[1]
        x = x // self.rozmiar_Kratki
        x = x * self.rozmiar_Kratki
        y = y // self.rozmiar_Kratki
        y = y * self.rozmiar_Kratki
        mousePos = (x, y)
        return mousePos

    def drawRect(self,poz):
        r = pygame.Rect((poz[0], poz[1]), (self.rozmiar_Kratki, self.rozmiar_Kratki))
        pygame.draw.rect(self.screen, (255, 255, 255), r)
        pygame.display.flip()
    def drawGrid(self):
        for x in range(self.wysokosc_Okna):
            for y in range(self.szerokosc_Okna):
                rect = pygame.Rect(x * self.rozmiar_Kratki, y * self.rozmiar_Kratki,
                                   self.rozmiar_Kratki, self.rozmiar_Kratki)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)
        pygame.display.flip()
        pygame.image.save(self.screen, 'temp.jpeg')
        
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.temp=self.mouse_position()
                print(self.temp)
                self.drawRect(self.temp)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.zapis = False


    def work(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
      
