import random
import sys
import time
import litery



class Worek:
    def __init__(self):
        self.kafelki = list(kafelki())
        self.ile = len(self.kafelki)
        random.shuffle(self.kafelki)

    def __str__(self):
        return "worek z " + str(self.ile) + " kafelkami.\n"

    def dobierz(self, k=7):
        if self.ile<k:
            k=self.ile
        random.shuffle(self.kafelki)
        wyn = self.kafelki[0:k]
        self.kafelki = self.kafelki[k:]
        self.ile -= len(wyn)
        return wyn

    def wymien(self,kafelki):
        self.kafelki +=kafelki
        random.shuffle(self.kafelki)
        wyn = self.kafelki[0:len(kafelki)]
        self.kafelki = self.kafelki[len(kafelki):]
        return wyn


class Plansza:
    def __init__(self):
        self.ile_slow = 0
        self.wymiar = 15
        self.tablica = [[" "]*15 for i in range(15)]
        self.litery = []
        self.gracze = []

    def wypisz(self,czyInstrukcja=True):

        borderTop = "\n" + \
                    self.gracze[1].imie.upper().center(63) + "\n" + \
                    ("[ ]"*len(self.gracze[1].reka)).center(63) + \
                    "\n"

        handBottom="["+"][".join(self.gracze[3].reka)+"]"
        borderBottom = handBottom.center(63) + "\n" + \
                       self.gracze[3].imie.upper().center(63) + "\n" + \
                       "\n"

        borderLeftCol1 = self.gracze[0].imie.upper().center(15)
        borderLeftCol2 = ("["*len(self.gracze[0].reka)).center(15)
        borderLeftCol3 = ("]" * len(self.gracze[0].reka)).center(15)

        borderRightCol3 = self.gracze[2].imie.upper().center(15)
        borderRightCol2 = ("]" * len(self.gracze[2].reka)).center(15)
        borderRightCol1 = ("[" * len(self.gracze[2].reka)).center(15)


        borderRightInfo = ["       Wyniki:"]
        wynikiTab = [[g.punkty,g.imie] for g in self.gracze]
        wynikiTab.sort(reverse=True)
        self.winner = wynikiTab[0][1]
        for w in wynikiTab:
            borderRightInfo.append("{:_<25}".format(w[1])+("{:_>3}").format(w[0]))



        if czyInstrukcja:
            borderRightInfo += ["W woreczku pozosta??o " + str(self.gracze[0].worek.ile) + " kafelk??w"]
            borderRightInfo +=["",
                                "       Instrukcja:",
                               "Postaraj si?? u??o??y?? s??owo o jak najwi??kszej ",
                               "liczbie punkt??w u??ywaj??c kafelk??w, kt??re masz",
                               "przed sob??. S??owo musi ????czy?? si?? z jednym ",
                               "z ju?? u??o??onych na planszy tak jak w krzy????wce",
                               "       Specjalne akcje:",
                               "w - wymie?? wybrane kafelki",
                               "s - sprawd?? ile punkt??w ma podane s??owo",
                               "p - popro?? o podpowied??",
                               "c - czekaj/omi?? tur?? | z - zamknij gr??"]
        else:
            borderRightInfo += ["", "W woreczku pozosta??o ", kaf(self.gracze[0].worek.ile)]

        print("\n")
        print(borderTop,end=" "*72)
        print(borderRightInfo[0])
        for j,i in enumerate(self.tablica):
            print(" " + borderLeftCol1[j],borderLeftCol2[j],borderLeftCol3[j]+"   ",end="")
            for ii in i:
                print("["+ii.upper()+"]",end="")


            print("   "+borderRightCol1[j],borderRightCol2[j],borderRightCol3[j]+" ",end="")
            if j+1 < len(borderRightInfo):
                print(" "*9+borderRightInfo[j+1])
            else:
                print("")
        if czyInstrukcja:
            print(" "*72+borderRightInfo[-1])
        else:
            print("")
        print(borderBottom)
        print("\n")

    def doloz(self,slowo,tryb=True,reka=[]):
        if self.ile_slow == 0:
            pocz = (self.wymiar-len(slowo))//2
            for i,s in enumerate(slowo):
                if tryb:
                    self.tablica[self.wymiar//2][i+pocz] = s
            if tryb:
                self.ile_slow += 1
            return list(slowo)
        else:
            for i in range(self.wymiar):
                for j in range(self.wymiar):
                    for k,l in enumerate(slowo):
                        if self.tablica[i][j] == l:
                            if kaf:=self.czy_da_sie_dolozyc(i,j,k,slowo,tryb,reka):
                                if tryb:
                                    self.ile_slow += 1
                                return kaf
            return False

    def czy_da_sie_dolozyc(self,i,j,k,slowo,tryb,reka):
        return self.czy_da_sie_pionowo(i,j,k,slowo,tryb,reka) or self.czy_da_sie_poziomo(i,j,k,slowo,tryb,reka)

    def czy_da_sie_pionowo(self,i,j,k,slowo,tryb,reka):
        if i-k<0:
            return False
        if i+len(slowo)-k>self.wymiar:
            return False
        if i-k>0:
            if self.tablica[i-k-1][j]!=" ":
                return False
        if i+len(slowo)-k<self.wymiar:
            if self.tablica[i+len(slowo)-k][j]!=" ":
                return False

        pom = [-1,1]
        if j == 0:
            pom[0] = 0
        if j == self.wymiar-1:
            pom[1] = 0

        uzytekafelki = []
        for kk,ll in enumerate(slowo):
            if self.tablica[i-k+kk][j] == " ":
                uzytekafelki.append(ll)
            if not (self.tablica[i-k+kk][j] == ll or self.tablica[i-k+kk][j] == " " and self.tablica[i-k+kk][j+pom[0]]==" " and self.tablica[i-k+kk][j+pom[1]] == " "):
                return False

        for u in uzytekafelki:
            if uzytekafelki.count(u)>reka.count(u):
                return False

        for kk, ll in enumerate(slowo):
            if tryb:
                self.tablica[i-k+kk][j] = ll
        return uzytekafelki

    def czy_da_sie_poziomo(self, i, j, k, slowo,tryb,reka):
        if j - k < 0:
            return False
        if j + len(slowo) - k > self.wymiar:
            return False
        if j - k > 0:
            if self.tablica[i][j-k-1] != " ":
                return False
        if j + len(slowo) - k  < self.wymiar:
            if self.tablica[i][j + len(slowo) - k] != " ":
                return False

        pom = [-1, 1]
        if i == 0:
            pom[0] = 0
        if i == self.wymiar - 1:
            pom[1] = 0

        uzytekafelki = []
        for kk, ll in enumerate(slowo):
            if self.tablica[i][j-k+kk] == " ":
                uzytekafelki.append(ll)
            if not (self.tablica[i][j - k + kk] == ll or self.tablica[i][j - k + kk] == " " and
                    self.tablica[i + pom[0]][j - k + kk] == " " and self.tablica[i + pom[1]][j - k + kk] == " "):
                return False


        for u in uzytekafelki:
            if uzytekafelki.count(u)>reka.count(u):
                return False

        for kk, ll in enumerate(slowo):
            if tryb:
                self.tablica[i][j - k + kk] = ll
        return uzytekafelki


class Gracz:
    def __init__(self,worek,plansza,imie="Anonymous"):
        self.imie = imie
        self.reka = []
        self.punkty = 0
        self.worek = worek
        self.plansza = plansza

    def __str__(self):
        r_pom = ""
        for i in self.reka:
            r_pom += "[" + i + "]"
        return "Gracz: " + self.imie + \
               "\nPunkty: " + str(self.punkty) + \
               "\nR??ka: " + r_pom + "\n\n"

    def dobierz(self):
        self.reka += self.worek.dobierz(7-len(self.reka))
        if len(self.reka) == 7:
            return True
        else:
            return False

    def doloz(self):
        kafelki_na_stole = set()
        for i in range(self.plansza.wymiar):
            for j in range(self.plansza.wymiar):
                kafelki_na_stole.add(self.plansza.tablica[i][j])
        kafelki_na_stole = list(kafelki_na_stole)
        kafelki_na_stole.remove(" ")
        lista_slow = []
        if len(kafelki_na_stole) == 0:
            lista_slow = najlepszeSlowo(self.reka,tryb=True)
        else:
            for k in kafelki_na_stole:
                lista_slow += najlepszeSlowo (self.reka+list(k),k,True)
        lista_slow=list(set(lista_slow))
        lista_slow.sort(key=wartosc_slowa, reverse=True)
        lista_slow = easy(lista_slow)
        for s in lista_slow:
            result = self.plansza.doloz(s,True,self.reka)
            if not result:
                continue
            self.punkty += wartosc_slowa(s)
            for r in result:
                self.reka.remove(r)
            return [s,wartosc_slowa(s)]
        return False

    def pre_ruch(self):
        self.plansza.wypisz(False)
        kwestia = random.choice(["Hmmm","Niech si?? zastanowi??","Niech pomy??l??","Hmmmmmm","Dajcie mi chwil??",
                                 "Co by tu u??o??y??","Mam to na ko??cu j??zyka","Zaraz, zaraz"])
        print(self.imie+": "+kwestia,end="")
        dotts = random.randint(3,7)
        for i in range(dotts):
            print(".",end="")
            sys.stdout.flush()
            wait(1)
        print("")

    def ruch(self):
        self.pre_ruch()
        if temp:=self.doloz():
            self.dobierz()
        else:
            temp=min(len(self.reka),random.randint(3,7),self.worek.ile)
            self.wymien(temp)
            temp=[temp]
        return self.post_ruch(temp)

    def post_ruch(self,temp):
        if len(temp)==1:
            if temp[0]==0:
                print("Nie mam ju?? co do??o??y??")
            else:
                print("Wymieniam ",kaf(temp[0]))
            return 0
        else:
            kwestia = random.choice(["Ju?? wiem!","Niech b??dzie:","Spr??bujmy","Uk??adam:"])
            print(kwestia,temp[0].upper(),", otrzymuj??: ",pkt(temp[1]))
            wait(2)
            return 1

    def wymien(self,k=4,doWymiany="!"):
        if doWymiany != "!":
            for d in doWymiany:
                self.reka.remove(d)
            self.reka += self.worek.wymien(doWymiany)
        else:
            random.shuffle(self.reka)
            self.reka[:k] = self.worek.wymien(self.reka[:k])


class ZywyGracz(Gracz):
    def ruch(self):
        self.pre_ruch()
        temp = self.decyzja()
        return self.post_ruch(temp)

    def pre_ruch(self):
        self.plansza.wypisz(True)
        print("Teraz Twoja kolej, wpisz s??owo, kt??re chcesz u??o??y??:")

    def post_ruch(self,temp):
        if temp == ["quit"]:
            return -1
        if len(temp)==0:
            print("Czekasz kolejk??")
            return 0
        if len(temp)==1:
            print("Wymieniasz",kaf(temp[0]))
            return 0
        else:
            print("Otrzymujesz: ",pkt(temp[1]))
            wait(2)
            return 1

    def decyzja(self):
        temp=False
        slowo=input().lower()
        while not temp:
            if len(slowo) == 1:
                if slowo == "w":
                    dowymiany = input("Kt??re kafelki chcesz wymieni???\n")
                    while len([i for i in dowymiany if i not in self.reka])>0:
                        dowymiany = input("Podaj jeszcze raz (upewnij si??, ??e posiadasz wszystkie kafelki,kt??re chcesz wymieni??\n")
                    self.wymien(doWymiany=dowymiany)
                    return [len(dowymiany)]
                if slowo == "s":
                    slowo = input("Podaj s??owo:\n")
                    print ("To s??owo jest warte: "+pkt(wartosc_slowa(slowo.lower())))
                    slowo = input("Wpisz s??owo lub wybierz akcj?? specjaln??\n").lower()
                    continue
                if slowo == "c":
                    return []
                if slowo == "z":
                    return ["quit"]
                if slowo == "p":
                    self.wskazowka()
                    slowo = input("Wpisz s??owo lub wybierz akcj?? specjaln??\n").lower()
                    continue

            temp=self.plansza.doloz(slowo,reka=self.reka)
            if not temp:
                slowo=input("Nie uda??o si?? u??o??y?? s??owa, spr??buj poda?? inne:\n").lower()
        self.punkty += wartosc_slowa(slowo)
        for t in temp:
            self.reka.remove(t)
        self.dobierz()
        return [slowo,wartosc_slowa(slowo)]
    
    def wskazowka(self):
        for r in range(100):
            i = random.randint(0,14)
            j = random.randint(0,14)
            z = self.plansza.tablica[i][j]
            temp = najlepszeSlowo(self.reka+[z],z,True)
            for t in temp:
                if self.plansza.doloz(t,tryb=False,reka=self.reka):
                    print("Spr??buj: "+ t)
                    return
        print("Spr??buj dobra?? kafelki, je??li woreczek nie jest jeszcze pusty")
        return



class Gra:
    def __init__(self):
        self.plansza = Plansza()
        self.worek = Worek()
        self.gracze = []
        for i in range (3):
            self.gracze.append(Gracz(self.worek,self.plansza))
        self.gracze.append(ZywyGracz(self.worek,self.plansza))
        self.plansza.gracze=self.gracze

    def rozgrywka(self):
        self.poczatek()
        i = 0
        counter = 0
        k=0
        while(self.gracze[i].reka!=[] and k!=-1 and counter!=4):
            k = self.gracze[i].ruch()
            if k==0:
                counter+=1
            else:
                counter=0
            wait(1)
            i=(i+1)%4
        self.koniec(k)

    def poczatek(self):
        self.gracze[-1].imie=input("\n\n\nWitaj w grze Scrabble!\nPodaj swoje imi??:\n").capitalize()
        if len(self.gracze[-1].imie) >23:
            self.gracze[-1].imie = self.gracze[-1].imie[:20]+"..."
        self.gracze[0].imie,self.gracze[1].imie,self.gracze[2].imie = losuj_imie(3,self.gracze[-1].imie)
        print("\nDzi??kujemy\n")
        wait(1)
        print("Dzisiaj b??dziesz gra?? z:")
        for g in self.gracze[0:-1]:
            print(g.imie,end="  ")
        sys.stdout.flush()
        wait(2)
        print("\n\nZaczynajmy ^^\n")
        wait(2)
        for g in self.gracze:
            g.dobierz()

    def koniec(self,czyPrzerwana):
        self.plansza.wypisz(False)
        if not czyPrzerwana:
            print("Koniec gry\n\nWygrywa {}! Gratulacje ^^".format(self.plansza.winner))
            wait(1)
        print("\nDzi??kujemy za gr?? ^^")
        wait(2)


def start():
    litery.pisz("Scrabble")
    wait(1)
    litery.podpis()
    wait(1)
    while True:
        print("""
        1. Nowa Gra
        2. Instrukcja
        3. Ustawienia
        4. Wyj??cie""")
        wait(1)
        choice = input("\n    Wybierz akcj??(1-4)\n")
        match choice:
            case "1":
                g=Gra()
                g.rozgrywka()
            case "2":
                instrukcja()
            case "3":
                ustawienia()
            case "4":
                print("Do zobaczenia :D")
                return

def instrukcja():
    text = """
    Witaj w grze Scrabble, 
    a przynajmniej jej prostszej konsolowej wersji.
    Celem gry jest uzyskanie jak najwi??kszej liczby
    punkt??w uk??adaj??c kafelki z literami na planszy.
    Kafelki powinny tworzy?? s??owa w taki spos??b, ??eby
    czytane poziomo i pionowo zawsze tworzy??y poprawne
    s??owa w j??zyku polskim. Ilo???? punkt??w uzyskanych 
    zale??y od warto??ci u??ytych liter (aby zobaczy?? 
    pe??n?? rozpisk?? wpisz P). Ze wzgl??du na ograniczenia
    graficzne ta werjsa nie posiada premii za konkretne
    pola. W grze bierze udzia?? od dw??ch do czterech
    graczy, ich ilo???? mo??na zmieni?? w ustawieniach.
    
    Je??li chcesz zobacy?? pe??n?? tabel?? punkt??w 
    wpisz P, aby wyj???? wpisz X"""
    points = """
    Tabela punkt??w:
    (Litera: | Warto????: | Ilo???? w woreczku:)
    || A | 1p| x9| | F | 5p| x1| | M | 2p| x3| | ?? | 5p| x1|| 
    || ?? | 5p| x1| | G | 3p| x2| | N | 1p| x5| | T | 2p| x3|| 
    || B | 3p| x2| | H | 3p| x2| | ?? | 7p| x1| | U | 3p| x2|| 
    || C | 2p| x3| | I | 1p| x8| | O | 1p| x6| | W | 1p| x4|| 
    || ?? | 6p| x1| | J | 3p| x2| | ?? | 5p| x1| | Y | 2p| x4|| 
    || D | 2p| x3| | K | 2p| x3| | P | 2p| x3| | Z | 1p| x5|| 
    || E | 1p| x7| | L | 2p| x3| | R | 1p| x4| | ?? | 9p| x1|| 
    || ?? | 5p| x1| | ?? | 3p| x2| | S | 1p| x4| | ?? | 5p| x1|| 
    
    Aby wyj???? wpisz X:
    """
    print(text)
    p=input()
    while p not in "XP":
        p = input(" Wpisz X lub P i klinknij enter\n")
    if p == "X":
        return
    print(points)
    p = input()
    while p != "X":
        p = input(" Wpisz X aby wyj???? i kliknij enter\n")

def ustawienia():
    global PREDKOSC
    global POZIOM_TRUDNOSCI
    global ILOSC_GRACZY
    while True:
        tpg = ("ekspresowa","szybka","normalna","wolna")[PREDKOSC]
        tpt = ("??atwy","??redni","trudny")[POZIOM_TRUDNOSCI]
        til = ("{} w tym {} ??ywy".format(*ILOSC_GRACZY))
        print("""
        1. Pr??dko???? gry: {} 
        2. Poziom trudno??ci: {}
        3. Liczba graczy: {}
        """.format(tpg,tpt,til))
        wait(1)
        wybor = input("Wybierz co chcesz zmieni??(1-3) lub wpisz x ??eby wyj????\n")
        match wybor:
            case "1":
                ust = input("Opcje: (1)wolna (2)normalna (3)szybka (4)ekspresowa\n")
                while ust not in ("1","2","3","4"):
                    ust = input ("wpisz 1, 2, 3 lub 4")
                PREDKOSC = 4-int(ust)
            case "2":
                ust = input("Opcje: (1)??atwy (2)??redni (3)trudny\n")
                while ust not in ("1","2","3"):
                    ust = input ("wpisz 1, 2 lub 3\n")
                POZIOM_TRUDNOSCI = int(ust) - 1
            case "3":
                print ("Tej opcji jeszcze nie mo??na zmieni?? :c")
            case "x":
                wait(1)
                return
            case "X":
                wait(1)
                return



def losuj_imie(k=1,imie="Quebo"):
    lista_imion = ["Arek", "Beata", "Czarek", "Dorota", "Eryk", "Faustyna", "Gienek", "Hania", "Irek", "Jola", "Kacper",
                   "Lidia", "Marek", "Nina", "Olaf", "Paula", "Romek", "Sylwia", "Teodor", "Ula", "Witek", "Zuzanna"]
    lista_imion = [i for i in lista_imion if i[0]!=imie[0].upper()]
    if k==1:
        return random.choice(lista_imion)
    else:
        return random.sample(lista_imion,k)

def kafelki():
    temp = "a" * 9
    temp += "??" * 1
    temp += "b" * 2
    temp += "c" * 3
    temp += "??" * 1
    temp += "d" * 3
    temp += "e" * 7
    temp += "??" * 1
    temp += "f" * 1
    temp += "g" * 2
    temp += "h" * 2
    temp += "i" * 8
    temp += "j" * 2
    temp += "k" * 3
    temp += "l" * 3
    temp += "??" * 2
    temp += "m" * 3
    temp += "n" * 5
    temp += "??" * 1
    temp += "o" * 6
    temp += "??" * 1
    temp += "p" * 3
    temp += "r" * 4
    temp += "s" * 4
    temp += "??" * 1
    temp += "t" * 3
    temp += "u" * 2
    temp += "w" * 4
    temp += "y" * 4
    temp += "z" * 5
    temp += "??" * 1
    temp += "??" * 1
    return temp

def kaf(number):
    if number == 1:
        return "1 kafelek"
    if number%10 in (2,3,4) and number not in (12,13,14):
        return str(number) + " kafelki"
    else:
        return str(number) + " kafelk??w"

def pkt(number):
    if number == 1:
        return "1 punkt"
    if number%10 in (2,3,4) and number not in (12,13,14):
        return str(number) + " punkty"
    else:
        return str(number) + " punkt??w"

def wait(period):
    time.sleep(period*PREDKOSC/2)

def easy(lista):
    a=0
    b=0
    match POZIOM_TRUDNOSCI:
        case 0:
            a = len(lista)//4
            b = len(lista)-1
            if a>=b:
                return lista
        case 1:
            a = len(lista)//20
            b = len(lista)//2
            if a>=b:
                return lista
        case 2:
            a = 0
            b = 10
            if len(lista)<10:
                b = len(lista)-2
            if b<=0:
                return lista
    r = random.randint(a,b)
    return lista[r:]
        

def wartosc_litery(a):
    litery=list("a??bc??de??fghijkl??mn??o??prs??tuwyz????")
    wartosci=[1,5,3,2,6,2,1,5,5,3,3,1,3,2,2,3,2,1,7,1,5,2,1,1,5,2,3,1,2,1,9,5]
    return wartosci[litery.index(a)]

def wartosc_slowa(slowo):
    if slowo == '-':
        return 0
    wyn = 0
    for z in slowo:
        wyn+=wartosc_litery(z)
    return wyn

def czy_mozna_ulozyc(kafelki):
    def inner(slowo):
        for s in slowo:
            if slowo.count(s) > kafelki.count(s):
                return False
        return True
    return inner

def najlepszeSlowo(tab,kryt='!',tryb=False):
    litery=list("a??bc??de??fghijkl??mn??o??prs??tuwyz????x*v9?>1q")
    pom = [a for a in litery if a not in tab]
    with open("LITEROWKA.txt",'r') as file:
        temp = file.read().split()
        for z in pom:
            temp = list(filter(lambda a: z not in a,temp ))
        temp.sort(key=wartosc_slowa, reverse=True)
        funkcja = czy_mozna_ulozyc(tab)
        temp=list(filter(funkcja,temp))
    if kryt!='!':
        temp = [ i for i in temp if kryt in i]
    if tryb:
        return temp
    if len(temp)==0:
        temp.append("-")
    return temp[0]

def doloz(slowo,tab):
    naj_slowo = ""
    naj_wart = 0
    for s in slowo:
        t = najlepszeSlowo(tab+list(s),s)
        w = wartosc_slowa(t)
        if w > naj_wart:
            naj_wart = w
            naj_slowo = t
    print("najlepsze: ",naj_slowo,naj_wart)
    return naj_slowo


if __name__ == "__main__":
    POZIOM_TRUDNOSCI = 1
    PREDKOSC = 2
    ILOSC_GRACZY = (4,1)
    start()
