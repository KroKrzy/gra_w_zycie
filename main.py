from komorka import Komorka

n = int(input("Podaj szerokosc planszy: "))
m = int(input("Podaj wysokosc planszy: "))

plansza = [[Komorka(i,j) for j in range(m+2)] for i in range(n+2)]

il = int(input("Podaj ilosc zywych komorek: "))

for i in range(il):
    x = int(input("Podaj 1. wspolrzedna komorki: "))
    y = int(input("Podaj 2. wspolrzedna komorki: "))
    plansza[x][y].zyje = True

while (True):
    #Tu wyswietl stan
    
    for i in range (1,n+1):
        for j in range (1,m+1):
            plansza[i][j].liczsasiadow()
    
    for i in range (1,n+1):
        for j in range (1,m+1):
            plansza[i][j].czy_zyje()
