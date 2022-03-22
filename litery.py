def pisz (tekst):
    print('\n\n')
    L1=""
    L2=""
    L3=""
    L4=""
    L5=""
    d=0
    m=0
    for c in tekst:
        match c.lower():
            case 'a':
                L1=L1+'    A    '
                L2=L2+'   A A   '
                L3=L3+'  A   A  '
                L4=L4+' AAAAAAA '
                L5=L5+'A       A'
                d+=9
            case 'b':
                 L1 = L1 + 'BBBBB '
                 L2 = L2 + 'BB  BB'
                 L3 = L3 + 'BBBBB '
                 L4 = L4 + 'BB  BB'
                 L5 = L5 + 'BBBBB '
                 d+=6
            case 'c':
                L1 = L1 + ' CCCC '
                L2 = L2 + 'CC  CC'
                L3 = L3 + 'CC    '
                L4 = L4 + 'CC  CC'
                L5 = L5 + ' CCCC '
                d += 6
            case 'd':
                L1 = L1 + 'DDDDD '
                L2 = L2 + 'DD  DD'
                L3 = L3 + 'DD  DD'
                L4 = L4 + 'DD  DD'
                L5 = L5 + 'DDDDD '
                d += 6
            case 'e':
                L1 = L1 + 'EEEEEE'
                L2 = L2 + 'EE    '
                L3 = L3 + 'EEEE  '
                L4 = L4 + 'EE    '
                L5 = L5 + 'EEEEEE'
                d += 6
            case 'f':
                L1 = L1 + 'FFFFFF'
                L2 = L2 + 'FF    '
                L3 = L3 + 'FFFF  '
                L4 = L4 + 'FF    '
                L5 = L5 + 'FF    '
                d += 6
            case 'g':
                L1 = L1 + ' GGGG '
                L2 = L2 + 'GG    '
                L3 = L3 + 'GG GGG'
                L4 = L4 + 'GG  GG'
                L5 = L5 + ' GGGG '
                d += 6
            case 'h':
                L1 = L1 + 'HH  HH'
                L2 = L2 + 'HH  HH'
                L3 = L3 + 'HHHHHH'
                L4 = L4 + 'HH  HH'
                L5 = L5 + 'HH  HH'
                d += 6
            case 'i':
                 L1 = L1 + '  II  '
                 L2 = L2 + '  II  '
                 L3 = L3 + '  II  '
                 L4 = L4 + '  II  '
                 L5 = L5 + '  II  '
                 d+=6
            case 'j':
                L1 = L1 + '    JJ'
                L2 = L2 + '    JJ'
                L3 = L3 + '    JJ'
                L4 = L4 + 'JJ  JJ'
                L5 = L5 + ' JJJJ '
                d += 6
            case 'k':
                 L1 = L1 + 'KK  KK'
                 L2 = L2 + 'KK KK '
                 L3 = L3 + 'KKK   '
                 L4 = L4 + 'KK KK '
                 L5 = L5 + 'KK  KK'
                 d+=6
            case 'l':
                 L1 = L1 + 'LL    '
                 L2 = L2 + 'LL    '
                 L3 = L3 + 'LL    '
                 L4 = L4 + 'LL    '
                 L5 = L5 + 'LLLLLL'
                 d+=6
            case 'ł':
                L1 = L1 + 'ŁŁ    '
                L2 = L2 + 'ŁŁ    '
                L3 = L3 + 'ŁŁŁŁ  '
                L4 = L4 + 'ŁŁ    '
                L5 = L5 + 'ŁŁŁŁŁŁ'
                d += 6
            case 'm':
                L1 = L1 + ' M   M '
                L2 = L2 + 'M M M M'
                L3 = L3 + 'M  M  M'
                L4 = L4 + 'M     M'
                L5 = L5 + 'M     M'
                d += 7
            case 'n':
                L1 = L1 + 'N    N'
                L2 = L2 + 'NN   N'
                L3 = L3 + 'N N  N'
                L4 = L4 + 'N  N N'
                L5 = L5 + 'N   NN'
                d += 6
            case 'o':
                 L1 = L1 + ' OOOO '
                 L2 = L2 + 'OO  OO'
                 L3 = L3 + 'OO  OO'
                 L4 = L4 + 'OO  OO'
                 L5 = L5 + ' OOOO '
                 d+=6
            case 'ó':
                L1 = L1 + '   Ó  '
                L2 = L2 + ' ÓÓÓÓ '
                L3 = L3 + 'ÓÓ  ÓÓ'
                L4 = L4 + 'ÓÓ  ÓÓ'
                L5 = L5 + ' ÓÓÓÓ '
                d += 6
            case 'p':
                L1 = L1 + 'PPPPP '
                L2 = L2 + 'PP  PP'
                L3 = L3 + 'PPPPP '
                L4 = L4 + 'PP    '
                L5 = L5 + 'PP    '
                d += 6
            case 'r':
                 L1 = L1 + 'RRRR  '
                 L2 = L2 + 'RR  R '
                 L3 = L3 + 'RRRR  '
                 L4 = L4 + 'RR RR '
                 L5 = L5 + 'RR  RR'
                 d+=6
            case 's':
                L1 = L1 + 'SSSSSS'
                L2 = L2 + 'SS    '
                L3 = L3 + 'SSSSSS'
                L4 = L4 + '    SS'
                L5 = L5 + 'SSSSSS'
                d += 6
            case 't':
                L1 = L1 + 'TTTTTT'
                L2 = L2 + '  TT  '
                L3 = L3 + '  TT  '
                L4 = L4 + '  TT  '
                L5 = L5 + '  TT  '
                d += 6
            case 'u':
                L1 = L1 + 'UU  UU'
                L2 = L2 + 'UU  UU'
                L3 = L3 + 'UU  UU'
                L4 = L4 + 'UU  UU'
                L5 = L5 + ' UUUU '
                d += 6
            case 'w':
                L1 = L1 + 'W     W'
                L2 = L2 + 'W     W'
                L3 = L3 + 'W  W  W'
                L4 = L4 + 'W W W W'
                L5 = L5 + ' W   W '
                d += 7

            case 'y':
                 L1 = L1 + 'YY  YY'
                 L2 = L2 + ' YYYY '
                 L3 = L3 + '  YY  '
                 L4 = L4 + ' YY   '
                 L5 = L5 + 'YY    '
                 d+=6
            case 'z':
                 L1 = L1 + 'ZZZZZZ'
                 L2 = L2 + '   ZZ '
                 L3 = L3 + '  ZZ  '
                 L4 = L4 + ' ZZ   '
                 L5 = L5 + 'ZZZZZZ'
                 d+=6
            case 'ż':
                L1 = L1 + '   Ż  '
                L2 = L2 + 'ŻŻŻŻŻŻ'
                L3 = L3 + '  ŻŻ  '
                L4 = L4 + ' ŻŻ   '
                L5 = L5 + 'ŻŻŻŻŻŻ'
                d += 6
            case '0':
                L1 = L1 + ' 0000 '
                L2 = L2 + '00  00'
                L3 = L3 + '00  00'
                L4 = L4 + '00  00'
                L5 = L5 + ' 0000 '
                d += 6
            case '1':
                L1 = L1 + '  111 '
                L2 = L2 + ' 1111 '
                L3 = L3 + '   11 '
                L4 = L4 + '   11 '
                L5 = L5 + '   11 '
                d += 6
            case '2':
                L1 = L1 + ' 2222 '
                L2 = L2 + '2  22 '
                L3 = L3 + '  22  '
                L4 = L4 + ' 22   '
                L5 = L5 + '222222'
                d += 6
            case '3':
                L1 = L1 + ' 3333 '
                L2 = L2 + '33  33'
                L3 = L3 + '   33 '
                L4 = L4 + '33  33'
                L5 = L5 + ' 3333 '
                d += 6
            case '4':
                L1 = L1 + '   44 '
                L2 = L2 + '  44  '
                L3 = L3 + ' 44  4'
                L4 = L4 + '444444'
                L5 = L5 + '    44'
                d += 6
            case '5':
                L1 = L1 + '555555'
                L2 = L2 + '55    '
                L3 = L3 + '55555 '
                L4 = L4 + '    55'
                L5 = L5 + '55555 '
                d += 6
            case '6':
                L1 = L1 + ' 6666 '
                L2 = L2 + '66    '
                L3 = L3 + '66666 '
                L4 = L4 + '66  66'
                L5 = L5 + ' 6666 '
                d += 6
            case '7':
                L1 = L1 + '777777'
                L2 = L2 + '   77 '
                L3 = L3 + '  77  '
                L4 = L4 + ' 77   '
                L5 = L5 + '77    '
                d += 6
            case '2':
                L1 = L1 + ' 8888 '
                L2 = L2 + '88  88'
                L3 = L3 + ' 8888 '
                L4 = L4 + '88  88'
                L5 = L5 + ' 8888 '
                d += 6
            case '9':
                L1 = L1 + ' 9999 '
                L2 = L2 + '99  99'
                L3 = L3 + ' 99999'
                L4 = L4 + '    99'
                L5 = L5 + ' 9999 '
                d += 6
            case '\n':
                print("{}\n{}\n{}\n{}\n{}\n".format(L1, L2, L3, L4, L5))
                L1=L2=L3=L4=L5=""
                m=max(m,d)
                d=0
            case ' ':
                L1 = L1 + '    '
                L2 = L2 + '    '
                L3 = L3 + '    '
                L4 = L4 + '    '
                L5 = L5 + '    '
                d+=4
        if c!='\n':
            L1,L2,L3,L4,L5=L1+'  ',L2+'  ',L3+'  ',L4+'  ',L5+'  '
            d+=2
    print("{}\n{}\n{}\n{}\n{}".format(L1,L2,L3,L4,L5))
    m=max(m,d)
    return m

def podpis(odLewej=54,imie="Alex Michalec"):
    print(' '*(odLewej-len(imie)-3)+"by "+imie)

if __name__ == '__main__':
    c = pisz("abcde\nfghij\nklmno\nprst\nuwyz")
    podpis()

