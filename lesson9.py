print('něco')

while True:
    vstup = input('Zadej číslo: ')
    try:
        cislo = int(vstup)
        vysledek = 100 / cislo
    except (ValueError, ZeroDivisionError):
        print('ČÍSLO!!!')
    else:
        print(vysledek)
        nasobek = vstup * 3
        print(nasobek)
        break    
