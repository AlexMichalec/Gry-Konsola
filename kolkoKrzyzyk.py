import time
import litery
import random




def RysujPlansze():
    poz = " " + "--- " * 3
    pio = "|" + "   |" * 3
    print(poz + '\n' + (pio + '\n' + poz + '\n') * 3)

def intro():
    time.sleep(1)
    litery.pisz("kółko i\nkrzyżyk")
    time.sleep(1)
    litery.podpis()
    print("\n")
    time.sleep(1)

def plansza(L):
    print("""
    |_1_|_2_|_3_|
  A |_{A1}_|_{A2}_|_{A3}_|
  B |_{B1}_|_{B2}_|_{B3}_|
  C |_{C1}_|_{C2}_|_{C3}_|
    """.format(**L))


def sprawdz(D,komp=0):
    if(D['A1']==D['A2']==D['A3']=='X' or D['B1']==D['B2']==D['B3']=='X' or D['C1']==D['C2']==D['C3']=='X' or D['A1']==D['B1']==D['C1']=='X' or D['A2']==D['B2']==D['C2']=='X' or D['A3']==D['B3']==D['C3']=='X' or D['A1']==D['B2']==D['C3']=='X' or D['A3']==D['B2']==D['C1']=='X'  ):
        if (komp == 0):
            print("Wygrał Gracz X, Gratulacje :D ")
        else:
            print("Udało Ci się, Gratulacje :D")
        return True
    if (D['A1'] == D['A2'] == D['A3'] == 'O' or D['B1'] == D['B2'] == D['B3'] == 'O' or D['C1'] == D['C2'] == D[
        'C3'] == 'O' or D['A1'] == D['B1'] == D['C1'] == 'O' or D['A2'] == D['B2'] == D['C2'] == 'O' or D['A3'] == D[
        'B3'] == D['C3'] == 'O' or D['A1'] == D['B2'] == D['C3'] == 'O' or D['A3'] == D['B2'] == D['C1'] == 'O'):
        if(komp==0):
            print("Wygrał Gracz O, Gratulacje :D ")
        else:
            print("Tym razem wygrał komputer, może następnym razem Ci się uda ^^")
        return True
    return False

def czyOk (pozycja,kartka):
    while(kartka.get(pozycja,'-4')!=' '):
        if(kartka.get(pozycja,'-4')!='-4'):
            pozycja=input("To pole jest już zajęte, wybierz inne pole:\n").upper()
        else:
            pozycja = input("Podaj poprawne współrzędne:\n").upper()
    return pozycja


def multiplayer():
    kartka=dict(A1=" ",A2=' ',A3=' ',B1=' ',B2=' ',B3=' ',C1=' ',C2=" ", C3=' ')
    plansza(kartka)
    wyb=input("Zaczyna X, podaj gdzie chcesz postawić X (np A3)\n").upper()
    wyb=czyOk(wyb,kartka)
    kartka[wyb]="X"
    plansza(kartka)
    t=1
    #Dodać sprawdzanie czy nie zastępuje xD
    while(True):
        wyb=input("Teraz kolej O, podaj gdzie chesz postawić O (np. A3)\n").upper()
        wyb=czyOk(wyb,kartka)
        kartka[wyb]='O'
        t+=1
        plansza(kartka)
        if (sprawdz(kartka)):
            break
        wyb = input("Teraz kolej X, podaj gdzie chesz postawić X (np. A3)\n").upper()
        wyb = czyOk(wyb,kartka)
        kartka[wyb] = 'X'
        t+=1
        plansza(kartka)
        if (sprawdz(kartka)):
            break
        if t==9:
            print("Remis ^^")
            break
    time.sleep(1)
    print("Dziękujemy za grę ^ ^")
    time.sleep(1)


def komputer(kartka,poziomTrudnosci,t):
    if poziomTrudnosci==1:
        wyb = random.choice(('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'))
        while (kartka[wyb] != ' '):
            wyb = random.choice(('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'))
        return wyb
    if poziomTrudnosci==2:
        
        match t:
            # krok 1
            case 1:
                if (kartka['B2'] == ' '):
                    return 'B2'
                else:
                    return random.choice(('A1', 'A3', 'C1', 'C3'))
            # krok 2
            case 3:
                if (kartka['B2'] == 'X'):
                    if (kartka['A1'] == 'X' and kartka['C3'] == ' '): return 'C3'
                    if (kartka['A2'] == 'X' and kartka['C2'] == ' '): return 'C2'
                    if (kartka['A3'] == 'X' and kartka['C1'] == ' '): return 'C1'
                    if (kartka['B1'] == 'X' and kartka['B3'] == ' '): return 'B3'
                    if (kartka['B3'] == 'X' and kartka['B1'] == ' '): return 'B1'
                    if (kartka['C1'] == 'X' and kartka['A3'] == ' '): return 'A3'
                    if (kartka['C2'] == 'X' and kartka['A2'] == ' '): return 'A2'
                    if (kartka['C3'] == 'X' and kartka['A1'] == ' '): return 'A1'
                    return random.choice([i for i in kartka if kartka[i] == ' '])
                else:
                    if (kartka['A1'] == 'X' and kartka['A3'] == 'X'): return 'A2'
                    if (kartka['A1'] == 'X' and kartka['C1'] == 'X'): return 'B1'
                    if (kartka['A3'] == 'X' and kartka['C3'] == 'X'): return 'B3'
                    if (kartka['C1'] == 'X' and kartka['C3'] == 'X'): return 'C2'

                    if (kartka['A1'] == 'X' and kartka['A2'] == 'X'): return 'A3'
                    if (kartka['A3'] == 'X' and kartka['A2'] == 'X'): return 'A1'
                    if (kartka['A1'] == 'X' and kartka['B1'] == 'X'): return 'C1'
                    if (kartka['B1'] == 'X' and kartka['C1'] == 'X'): return 'A1'
                    if (kartka['C1'] == 'X' and kartka['C2'] == 'X'): return 'C3'
                    if (kartka['C2'] == 'X' and kartka['C3'] == 'X'): return 'C1'
                    if (kartka['B3'] == 'X' and kartka['A3'] == 'X'): return 'C3'
                    if (kartka['B3'] == 'X' and kartka['C3'] == 'X'): return 'A3'
                    return random.choice([i for i in kartka if kartka[i] == ' '])

        return random.choice([i for i in kartka if kartka[i] == ' '])

    if poziomTrudnosci==3:
        match t:
        #krok 1
            case 1:
                if(kartka['B2']==' '):
                    return 'B2'
                else:
                    return random.choice(('A1','A3','C1','C3'))
            #krok 2
            case 3:
                if(kartka['B2']=='X'):
                    if (kartka['A1'] == 'X' and kartka['C3'] == ' '): return 'C3'
                    if (kartka['A2'] == 'X' and kartka['C2'] == ' '): return 'C2'
                    if (kartka['A3'] == 'X' and kartka['C1'] == ' '): return 'C1'
                    if (kartka['B1'] == 'X' and kartka['B3'] == ' '): return 'B3'
                    if (kartka['B3'] == 'X' and kartka['B1'] == ' '): return 'B1'
                    if (kartka['C1'] == 'X' and kartka['A3'] == ' '): return 'A3'
                    if (kartka['C2'] == 'X' and kartka['A2'] == ' '): return 'A2'
                    if (kartka['C3'] == 'X' and kartka['A1'] == ' '): return 'A1'
                    return random.choice([i for i in kartka if kartka[i]==' '])
                else:
                    if (kartka['A1'] == 'X' and kartka['A3'] == 'X'): return 'A2'
                    if (kartka['A1'] == 'X' and kartka['C1'] == 'X'): return 'B1'
                    if (kartka['A3'] == 'X' and kartka['C3'] == 'X'): return 'B3'
                    if (kartka['C1'] == 'X' and kartka['C3'] == 'X'): return 'C2'

                    if (kartka['A1'] == 'X' and kartka['A2'] == 'X'): return 'A3'
                    if (kartka['A3'] == 'X' and kartka['A2'] == 'X'): return 'A1'
                    if (kartka['A1'] == 'X' and kartka['B1'] == 'X'): return 'C1'
                    if (kartka['B1'] == 'X' and kartka['C1'] == 'X'): return 'A1'
                    if (kartka['C1'] == 'X' and kartka['C2'] == 'X'): return 'C3'
                    if (kartka['C2'] == 'X' and kartka['C3'] == 'X'): return 'C1'
                    if (kartka['B3'] == 'X' and kartka['A3'] == 'X'): return 'C3'
                    if (kartka['B3'] == 'X' and kartka['C3'] == 'X'): return 'A3'
                    return random.choice([i for i in kartka if kartka[i] == ' '])
                #krok 3
            case 5:
                #Czy może wygrać?
                #poziomo zewnątrz
                if (kartka['A1'] == 'O' and kartka['A2'] == 'O' and kartka['A3'] == ' '): return 'A3'
                if (kartka['A3'] == 'O' and kartka['A2'] == 'O' and kartka['A1'] == ' '): return 'A1'
                if (kartka['B1'] == 'O' and kartka['B2'] == 'O' and kartka['B3'] == ' '): return 'B3'
                if (kartka['B3'] == 'O' and kartka['B2'] == 'O' and kartka['B1'] == ' '): return 'B1'
                if (kartka['C1'] == 'O' and kartka['C2'] == 'O' and kartka['C3'] == ' '): return 'C3'
                if (kartka['C3'] == 'O' and kartka['C2'] == 'O' and kartka['C1'] == ' '): return 'C1'
                #pionowo zewnątrz
                if (kartka['A1'] == 'O' and kartka['B1'] == 'O' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B1'] == 'O' and kartka['A1'] == 'O' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A2'] == 'O' and kartka['B2'] == 'O' and kartka['C2'] == ' '): return 'C2'
                if (kartka['B2'] == 'O' and kartka['A2'] == 'O' and kartka['A2'] == ' '): return 'A2'
                if (kartka['A3'] == 'O' and kartka['B3'] == 'O' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B3'] == 'O' and kartka['A3'] == 'O' and kartka['A3'] == ' '): return 'A3'
                #skos
                if (kartka['A1'] == 'O' and kartka['B2'] == 'O' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B2'] == 'O' and kartka['C3'] == 'O' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A3'] == 'O' and kartka['B2'] == 'O' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B2'] == 'O' and kartka['C1'] == 'O' and kartka['A3'] == ' '): return 'A3'
                #środki
                if (kartka['A1'] == 'O' and kartka['A3'] == 'O' and kartka['A2'] == ' '): return 'A2'
                if (kartka['C1'] == 'O' and kartka['C3'] == 'O' and kartka['C2'] == ' '): return 'C2'
                if (kartka['A3'] == 'O' and kartka['C3'] == 'O' and kartka['B3'] == ' '): return 'B3'
                if (kartka['A1'] == 'O' and kartka['C1'] == 'O' and kartka['B1'] == ' '): return 'B1'
                #Czy może przegrać
                # poziomo zewnątrz
                if (kartka['A1'] == 'X' and kartka['A2'] == 'X' and kartka['A3'] == ' '): return 'A3'
                if (kartka['A3'] == 'X' and kartka['A2'] == 'X' and kartka['A1'] == ' '): return 'A1'
                if (kartka['B1'] == 'X' and kartka['B2'] == 'X' and kartka['B3'] == ' '): return 'B3'
                if (kartka['B3'] == 'X' and kartka['B2'] == 'X' and kartka['B1'] == ' '): return 'B1'
                if (kartka['C1'] == 'X' and kartka['C2'] == 'X' and kartka['C3'] == ' '): return 'C3'
                if (kartka['C3'] == 'X' and kartka['C2'] == 'X' and kartka['C1'] == ' '): return 'C1'
                # pionowo zewnątrz
                if (kartka['A1'] == 'X' and kartka['B1'] == 'X' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B1'] == 'X' and kartka['A1'] == 'X' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A2'] == 'X' and kartka['B2'] == 'X' and kartka['C2'] == ' '): return 'C2'
                if (kartka['B2'] == 'X' and kartka['A2'] == 'X' and kartka['A2'] == ' '): return 'A2'
                if (kartka['A3'] == 'X' and kartka['B3'] == 'X' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B3'] == 'X' and kartka['A3'] == 'X' and kartka['A3'] == ' '): return 'A3'
                # skos
                if (kartka['A1'] == 'X' and kartka['B2'] == 'X' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B2'] == 'X' and kartka['C3'] == 'X' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A3'] == 'X' and kartka['B2'] == 'X' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B2'] == 'X' and kartka['C1'] == 'X' and kartka['A3'] == ' '): return 'A3'
                # środki
                if (kartka['A1'] == 'X' and kartka['A3'] == 'X' and kartka['A2'] == ' '): return 'A2'
                if (kartka['C1'] == 'X' and kartka['C3'] == 'X' and kartka['C2'] == ' '): return 'C2'
                if (kartka['A3'] == 'X' and kartka['C3'] == 'X' and kartka['B3'] == ' '): return 'B3'
                if (kartka['A1'] == 'X' and kartka['C1'] == 'X' and kartka['B1'] == ' '): return 'B1'
            case 5:
                # Czy może wygrać?
                # poziomo zewnątrz
                if (kartka['A1'] == 'O' and kartka['A2'] == 'O' and kartka['A3'] == ' '): return 'A3'
                if (kartka['A3'] == 'O' and kartka['A2'] == 'O' and kartka['A1'] == ' '): return 'A1'
                if (kartka['B1'] == 'O' and kartka['B2'] == 'O' and kartka['B3'] == ' '): return 'B3'
                if (kartka['B3'] == 'O' and kartka['B2'] == 'O' and kartka['B1'] == ' '): return 'B1'
                if (kartka['C1'] == 'O' and kartka['C2'] == 'O' and kartka['C3'] == ' '): return 'C3'
                if (kartka['C3'] == 'O' and kartka['C2'] == 'O' and kartka['C1'] == ' '): return 'C1'
                # pionowo zewnątrz
                if (kartka['A1'] == 'O' and kartka['B1'] == 'O' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B1'] == 'O' and kartka['A1'] == 'O' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A2'] == 'O' and kartka['B2'] == 'O' and kartka['C2'] == ' '): return 'C2'
                if (kartka['B2'] == 'O' and kartka['A2'] == 'O' and kartka['A2'] == ' '): return 'A2'
                if (kartka['A3'] == 'O' and kartka['B3'] == 'O' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B3'] == 'O' and kartka['A3'] == 'O' and kartka['A3'] == ' '): return 'A3'
                # skos
                if (kartka['A1'] == 'O' and kartka['B2'] == 'O' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B2'] == 'O' and kartka['C3'] == 'O' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A3'] == 'O' and kartka['B2'] == 'O' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B2'] == 'O' and kartka['C1'] == 'O' and kartka['A3'] == ' '): return 'A3'
                # środki
                if (kartka['A1'] == 'O' and kartka['A3'] == 'O' and kartka['A2'] == ' '): return 'A2'
                if (kartka['C1'] == 'O' and kartka['C3'] == 'O' and kartka['C2'] == ' '): return 'C2'
                if (kartka['A3'] == 'O' and kartka['C3'] == 'O' and kartka['B3'] == ' '): return 'B3'
                if (kartka['A1'] == 'O' and kartka['C1'] == 'O' and kartka['B1'] == ' '): return 'B1'

            case 7:
                # Czy może przegrać
                # poziomo zewnątrz
                if (kartka['A1'] == 'X' and kartka['A2'] == 'X' and kartka['A3'] == ' '): return 'A3'
                if (kartka['A3'] == 'X' and kartka['A2'] == 'X' and kartka['A1'] == ' '): return 'A1'
                if (kartka['B1'] == 'X' and kartka['B2'] == 'X' and kartka['B3'] == ' '): return 'B3'
                if (kartka['B3'] == 'X' and kartka['B2'] == 'X' and kartka['B1'] == ' '): return 'B1'
                if (kartka['C1'] == 'X' and kartka['C2'] == 'X' and kartka['C3'] == ' '): return 'C3'
                if (kartka['C3'] == 'X' and kartka['C2'] == 'X' and kartka['C1'] == ' '): return 'C1'
                # pionowo zewnątrz
                if (kartka['A1'] == 'X' and kartka['B1'] == 'X' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B1'] == 'X' and kartka['A1'] == 'X' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A2'] == 'X' and kartka['B2'] == 'X' and kartka['C2'] == ' '): return 'C2'
                if (kartka['B2'] == 'X' and kartka['A2'] == 'X' and kartka['A2'] == ' '): return 'A2'
                if (kartka['A3'] == 'X' and kartka['B3'] == 'X' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B3'] == 'X' and kartka['A3'] == 'X' and kartka['A3'] == ' '): return 'A3'
                # skos
                if (kartka['A1'] == 'X' and kartka['B2'] == 'X' and kartka['C3'] == ' '): return 'C3'
                if (kartka['B2'] == 'X' and kartka['C3'] == 'X' and kartka['A1'] == ' '): return 'A1'
                if (kartka['A3'] == 'X' and kartka['B2'] == 'X' and kartka['C1'] == ' '): return 'C1'
                if (kartka['B2'] == 'X' and kartka['C1'] == 'X' and kartka['A3'] == ' '): return 'A3'
                # środki
                if (kartka['A1'] == 'X' and kartka['A3'] == 'X' and kartka['A2'] == ' '): return 'A2'
                if (kartka['C1'] == 'X' and kartka['C3'] == 'X' and kartka['C2'] == ' '): return 'C2'
                if (kartka['A3'] == 'X' and kartka['C3'] == 'X' and kartka['B3'] == ' '): return 'B3'
                if (kartka['A1'] == 'X' and kartka['C1'] == 'X' and kartka['B1'] == ' '): return 'B1'

            
            
            
        return random.choice([i for i in kartka if kartka[i] == ' '])
    

def single(poziomTrudnosci):
    kartka = dict(A1=" ", A2=' ', A3=' ', B1=' ', B2=' ', B3=' ', C1=' ', C2=" ", C3=' ')
    plansza(kartka)
    wyb = input("Zaczynasz, podaj gdzie chcesz postawić X (np A3)\n").upper()
    wyb=czyOk(wyb,kartka)
    kartka[wyb] = "X"
    plansza(kartka)
    t = 1
    while (True):
        time.sleep(1)
        print("Komputer: hmmm teraz moja kolej")
        time.sleep(1)
        wyb=komputer(kartka,poziomTrudnosci,t)
        kartka[wyb] = 'O'
        t += 1
        plansza(kartka)
        if (sprawdz(kartka,1)):
            break
        wyb = input("Teraz Twoja kolej, podaj gdzie chesz postawić X (np. A3)\n").upper()
        wyb = czyOk(wyb, kartka)
        kartka[wyb] = 'X'
        t += 1
        plansza(kartka)
        if (sprawdz(kartka,1)):
            break
        if t == 9:
            print("Remis ^^")
            break
    time.sleep(1)
    print("Dziękujemy za grę ^ ^")
    time.sleep(1)


def gra():
    poziomTrudnosci=1
    while(True):
        intro()
        print("\t(1) Nowa Gra")
        print("\t(2) Multiplayer")
        print("\t(3) Ustawienia")
        print("\t(x) Wróć")
        w=input()
 #       print('\n')
        match w:
            case '1':
                print("""
    W tej wersji zagrasz przeciwko komputerowi
    Twoim zadanie polega na stawianiu X na planszy 3x3
    tak, żeby utworzyć linię złożoną z trzech X
    Czy jesteś gotowy? (T/N)
    """)
                czy=input().upper()
                if(czy=="N"):
                    print("\tNie ma sprawy, wróć kiedy będziesz gotów ^^")
                while(czy=='T'):
                    single(poziomTrudnosci)
                    czy=input("Czy chcesz zagrać jeszcze raz?(T/N)\n")
            case '2':
                print("""
    W tej wersji zagrasz ze swoim przyjacielem
    Gra polega na naprzemiennym stawianiu X i O
    Wygrywa osoba która jako pierwsza będzie miała trzy znaki 
    w tej samej linii (poziomo, pionowo lub na ukos)
    """)
                czy=input("Jesteście gotowi? (T/N)\n").upper()
                if(czy=="N"):
                    print("W takim razie wróć jak znajdziesz przyjaciela ^^")
                while(czy=='T'):
                    multiplayer()
                    czy = input("Czy chcesz zagrać jeszcze raz? (T/N)\n")
            case '3':
                print("""
    
    Single player:
    Poziom trudności: {}
    1-łatwy 
    2-średni
    3-trudny
    
    Czy chcesz zmienić poziom trudności? (T/N)
    """.format(poziomTrudnosci))
                czy = input().upper()
                if(czy=='T'):
                    z = input ("Wybierz poziom trudności\n")
                    while (z not in ('1','2','3')):
                        z = input("Podaj poziom trudności (1-3)\n")
                    poziomTrudnosci=int(z)
                    print("Zmieniono ^^ \n")
                else:
                    print("\tNa razie brak innych ustawień\n")
            case 'x':
                return
            case _:
                print("Wybierz jedną z opcji powyżej ^ _ ^")
        print('\n')
        time.sleep(1)


if __name__ == "__main__":
    gra()