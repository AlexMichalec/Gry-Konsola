import litery
import random
import time

def intro():
    litery.pisz('365 słów')
    time.sleep(0.5)
    litery.podpis()
    time.sleep(0.5)

def nowagra():
    plik=open("slowa.txt")
    S=plik.read()
    plik.close()
    S=list(S.split())
    plik=open("odgadniete.txt",'a')
    while(len(S)):
        slowo=random.choice(S).lower()
        licznikpodpowiedzi=1
        print("\nSłowo ma {} liter, kliknij x aby wyjść, kliknij p aby uzyskać podpowiedź (max 3 razy)".format(len(slowo)))
        print('[ ]'*len(slowo),end='')
        los=input("<-Zgadnij slowo lub wpisz x aby wyjść ").lower()
        while(los!='x'):
            if(los=='p'):
                if(licznikpodpowiedzi<4):
                    podp=list(random.sample(range(0,len(slowo)-1),licznikpodpowiedzi))
                    for i in range(len(slowo)):
                        if i in podp:
                            print("["+slowo[i].upper()+"]",end='')
                        else:
                            print("[ ]",end='')
                    print("<-To Twoja podpowiedź ",end='')
                    licznikpodpowiedzi+=1
                else:
                    print("Wykorzystałeś już wszystkie podpowiedzi, zgaduj!",end='')
                los=input()
                continue
            if(len(los)!=len(slowo)):
                print('[ ]' * len(slowo), end='')
                print("<-Szukane słowo ma %d liter, spróbuj jeszcze raz:" % (len(slowo)),end='')
                los=input()
                continue

            for (a,b) in zip(slowo,los):
                if(a==b):
                    print('[%s]'%(a.upper()),end='')
                else:
                    if(b in slowo):
                        print('[?]',end='')
                    else:
                        print("[ ]",end='')
            if(slowo==los):
                print("  Gratulacje udalo Ci się :D")
                plik.write(" " + slowo.capitalize())
                S.remove(slowo)
                break
            else:
                n=random.choice(("Już prawie :D       ",
                                 "Spróbuj ponownie ^^ ",
                                 "Spróbuj jeszcze raz ",
                                 "Prawie, prawie  ^^  ",
                                 "Jesteś coraz bliżej "))
                los=input( "<-"+n).lower()
        if(los=='x'):
            print("Dzięki za grę, do zobaczenia ^^\n")
            break
        if (len(S)!=0):
            u=input("\nCzy chcesz zagrać jeszcze raz?(T/N)\n").upper()
            if(u=='N'):
                print("\nDzięki za grę, do zobaczenia ^^\n")
                time.sleep(1)
                break

    else:
        print("\nGratulacje, odgadłeś/aś wszystkie słowa :D")

    plik.close()
    S=' '.join(S)
    plik=open("slowa.txt",'w')
    plik.write(S)
    plik.close()

def reset():
    plik=open("slownik.txt")
    L=list(plik.read().split())
    K=random.sample(L,365)
    plik2=open("slowa.txt",'w')
    plik2.write(" ".join(K))
    plik3=open("odgadniete.txt",'w')
    plik.close()
    plik2.close()
    plik3.close()

def gra():
    intro()
    i='1'
    while(i!='x'):
        print("\n1. Nowa Gra \n2. Instrukcja\n3. Odgadnięte słowa\n4. Wyjście")
        i=input("Wybierz akcję (1-4)\n")
        match i:
            case '1':
                nowagra()
                intro()
            case '2':
                print("\nWitaj w grze 365 słów ^^\n\n"
                      "Jest to skromna wariacja na podstawie internetowej\n"
                      "gry Wordle, którą pewnie widziałeś/aś na twitterze.\n"
                      "W naszej wersji niestety nie możesz podzielić się\n"
                      "swoimi wynikami ze znajomymi (o ile nie namówisz ich\n"
                      "żeby też usiedli przy tej konsoli) za to masz możliwość\n"
                      "nawet w jeden dzień odgadnąć więcej słów niż oni w ciągu roku ^^\n"
                      "Dodatkowo gra jest w 100% po polsku i zawiera podpowiedzi :3\n\n"
                      "Ale na czym to polega? :o - możesz zapytać\n"
                      "W każdej grze losujemy słowo ze zbioru 365 wyrazów\n"
                      "słowo ma od 4 do 8 liter, które się nie powtarzają\n"
                      "Twoim zadaniem jest zgadnięcie tego słowa\n\n"
                      "No ok, ale skąd mam wiedzieć jak? :/ \n"
                      "Już tłumaczę, na początek wyświetli Ci się ilośc liter\n"
                      "Np dla słowa \"lato\" będzie to [ ][ ][ ][ ]\n"
                      "załóżym że zgadujesz że to słowo to 'kino', wtedy\n"
                      "wyświetli Ci się [ ][ ][ ][O], gdyż literka o jest na właściwym\n"
                      "miejscu, załóżmy że dalej zgadujesz 'iglo' wtedy pojawi Ci się:\n"
                      "[ ][ ][?][O] oznacza to, że litela l znajduje się w tym słowie, ale\n"
                      "w innym miejscu. Litery w słowie się nie powtarzają, poza tym jest\n"
                      "to gra made in Poland więć pamiętaj o polskich znakach ^^\n\n"
                      "A co z podpowiedziami? :P\n"
                      "Rzeczywiście, zapomniałbym. Polski język nie jest prosty, więc\n"
                      "aby nieco ułatwić rozgrywkę dodaliśmy opcję podpowiedzi. Jeżeli\n"
                      "w czasie gry wpisz samą literkę p komputer wylosuje dla Ciebie\n"
                      "literę ze słowa, którą Ci pokaże. Masz trzy podpowiedzi do wykorzystania\n"
                      "Za pierwszym razem będzie to jedna litera, potem dwie, a na końcu trzy.\n"
                      "Oczywiście zachęcamy do własnej dedukcji, ale ta gra ma sprawiać przyjemność,\n"
                      "więc nie wahaj się użyć p jeśli tylko poczujesz taką potrzebę. ^^\n"
                      "W przypadku znudzenia grą zawsze możesz wpisać x by powrócić do menu głównego.\n\n")
                pyt=input("\nCzy wszystko jasne?(T/N)\n").upper()
                if(pyt=='T'):
                    print("\nSuper w takim razie, aby zacząć wybierz opcję 1 ^^\n")
                else:
                    print("\nSpokojnie, zawsze możesz wrócić do konsoli wybrać inną grę ^^\n")
            case '3':
                plik=open("odgadniete.txt")
                S=plik.read()
                L=list(S.split())
                L.sort()
                S=", ".join(L)
                plik = open("slowa.txt")
                SS = plik.read()
                LL = list(SS.split())

                print("\nOdgadnięte słowa:\n"+S+"\n\nProcent odgadniętych: %.2f" % (100*len(L)/(len(L)+len(LL)))+"%")
                xx=input("\nCzy chcesz zresetować grę (T/N)\n\n").upper()
                if(xx=='T'):
                    xx=input("Czy na pewno? (T/N)")
                    if (xx=='T'):
                        reset()
            case'4':
                print("\nDo Zobaczenia ^^\n")
                time.sleep(1)
                return
            case _ :
                print("\nPodaj poprawną wartość (1-4)\n")
        time.sleep(1)

def sortujslowa():
    plik = open('slowa.txt')
    S = plik.read().lower()
    S = list(S.split())
    S.sort()
    plik.close()
    plik = open('slowa.txt', 'w')
    plik.write(" ".join(S))
    plik.close()


if __name__ == '__main__':
    gra()

"""
Do zrobienia:
Logo?
poprawpić instrukcję"""