from komorka import Komorka
from plansza import Plansza


n = int(input("Podaj szerokosc planszy: "))
m = int(input("Podaj wysokosc planszy: "))
zapis = True
field = Plansza(n, m)

plansza = [[Komorka(i,j) for j in range(m+2)] for i in range(n+2)]

while (zapis):
    field.input()



while (True):

    for i in range (1,n+1):
        for j in range (1,m+1):
            plansza[i][j].liczsasiadow()

    for i in range (1,n+1):
        for j in range (1,m+1):
            plansza[i][j].czy_zyje()
