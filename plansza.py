import pygame
import sys



class Plansza:
    def __init__(self):
        pygame.init()
        self.wysokosc_Okna = 720
        self.szerokosc_Okna = 1080
        self.rozmiar_Kratki = 15
        self.screen = pygame.display.set_mode((self.szerokosc_Okna, self.wysokosc_Okna))

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

    def drawRect(self):
        wsp = self.mouse_position()
        r = pygame.Rect((wsp[0], wsp[1]), (self.rozmiar_Kratki, self.rozmiar_Kratki))
        pygame.draw.rect(self.screen, (255, 255, 255), r)

    def drawGrid(self):
        for x in range(self.wysokosc_Okna):
            for y in range(self.szerokosc_Okna):
                rect = pygame.Rect(x * self.rozmiar_Kratki, y * self.rozmiar_Kratki,
                                   self.rozmiar_Kratki, self.rozmiar_Kratki)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.drawRect()


field = Plansza()
field.drawGrid()
pygame.display.flip()
pygame.image.save(field.screen, 'temp.jpeg')
myimage = pygame.image.load("temp.jpeg").convert_alpha()
imagerect = myimage.get_rect()

while True:

    field.input()
    pygame.display.flip()