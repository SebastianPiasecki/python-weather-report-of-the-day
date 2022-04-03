DATA = """
monday;1250
tuesday;1405
wednesday;1750
thursday;1100
friday;0800
saturday;1225
sunday;1355
"""

def przelicz_wartosci(value):
    wskazanie_licznika = 0
    if value >= 1400:
        wskazanie_licznika = value / 22.5
    elif value < 1400 and value > 1200:
        wskazanie_licznika = value / 23.1
    else:
        wskazanie_licznika = value / 23.5
    # Wypisz temperaturę z dokładnością do trzeciego miejsca po przecinku (tak jak na przykładzie) i ze znakiem specjalnym ℃ (\u2103)
    print(f'{wskazanie_licznika:.3f} \u2103')
    # 0℃ |#########-----------| 100℃
    plotki = int(wskazanie_licznika//5)*'#'
    myslniki = int(20 - (wskazanie_licznika//5))*'-'
    print(f'0\u2103 |{plotki}{myslniki}| 100\u2103')

def zczytaj_dane():
    dane_slownik = {}
    data = DATA.strip('\n')
    data = data.split('\n')
    for entry in data:
        pair = entry.split(';')
        dane_slownik[pair[0]] = int(pair[1])
    return dane_slownik

def main():        
    dzien = input("Podaj dzien tygodnia:\n")
    dzien = dzien.lower()
    dane_slownik = zczytaj_dane()
    if dane_slownik.get(dzien, None):
        value = dane_slownik.get(dzien, None)
        przelicz_wartosci(value)
    else:
        print('Nie ma takiego dnia')

if __name__ == '__main__':
    main()