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
        if plansza[self.x-1][self.y-1]:
            suma += 1
        if plansza[self.x-1][self.y]:
            suma += 1
        if plansza[self.x-1][self.y+1]:
            suma += 1
        if plansza[self.x][self.y-1]:
            suma += 1
        if plansza[self.x][self.y+1]:
            suma += 1
        if plansza[self.x+1][self.y-1]:
            suma += 1
        if plansza[self.x+1][self.y]:
            suma += 1
        if plansza[self.x+1][self.y+1]:
            suma += 1
        
        self.ilesasiadow = suma
        
        return self
