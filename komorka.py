


class Komorka:
    def __init__(self,x,y):
        self.zyje= False
        self.ilesasiadow = 0
        self.x = x #wspolrzedna x komorki na planszy
        self.y = y #wspolrzedna y komorki na planszy
    def czy_zyje(self):
        """Metoda sprawdza czy komorka zyje na podstawie ilosci sasiadow"""
        if (self.zyje and self.ilesasiadow == 2) or self.ilesasiadow == 3:
            self.zyje = True
        else:
            self.zyje = False
        return self
    def liczsasiadow(self):
        """Metoda sprawdza ilosc sasiadow"""
        global plansza
        suma = 0
        if plansza[self.x-1][self.y-1].zyje:
            suma += 1
        if plansza[self.x-1][self.y].zyje:
            suma += 1
        if plansza[self.x-1][self.y+1].zyje:
            suma += 1
        if plansza[self.x][self.y-1].zyje:
            suma += 1
        if plansza[self.x][self.y+1].zyje:
            suma += 1
        if plansza[self.x+1][self.y-1].zyje:
            suma += 1
        if plansza[self.x+1][self.y].zyje:
            suma += 1
        if plansza[self.x+1][self.y+1].zyje:
            suma += 1
        
        self.ilesasiadow = suma
        
        return self

m = int(input("Podaj szerokosc planszy: "))
n = int(input("Podaj wysokosc planszy: "))

l=int(n*15)
k=int(m*15)

plansza = [[Komorka(i,j) for j in range(m+2)] for i in range(n+2)]

