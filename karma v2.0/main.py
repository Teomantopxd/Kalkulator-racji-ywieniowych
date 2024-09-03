import random
import copy

class Food:
    def __init__(self, nazwa, SM, ES, bialko, wapn, fosfor, sod, wlokno, waga = 1.0):
        self.nazwa = nazwa
        self.SM = SM
        self.ES = ES
        self.bialko = bialko
        self.wapn = wapn
        self.fosfor = fosfor
        self.sod = sod
        self.wlokno = wlokno
        self.waga = waga

skl = []
sianko = []
skl.append(Food("siano z traw 1. pokos kłoszenie", 0.896, 7.8, 71, 5, 2.8, 0.5, 259))
skl.append(Food("siano z traw 1. pokos początek kwitnienia", 0.868, 7.9, 63, 6, 2.9, 0.5, 261))
skl.append(Food("siano z lucerny 2 pokos", 0.889, 8.6, 84, 14, 2.2, 0.5, 284))
skl.append(Food("siano z traw 1. pokos w kwiecie", 0.890, 7.7, 52, 7, 3, 0.5, 294))
skl.append(Food("pastwisko 2 rotacja maj/czerwiec", 0.199, 2.3, 31, 1, 0.6, 0.2, 47))
skl.append(Food("pastwisko 5 rotacja sierpień/wrzesień", 0.207, 2.4, 25, 1.5, 0.7, 0.2, 50))
skl.append(Food("łąka, strzelanie w źdźbło", 0.192, 2.3, 36, 1.6, 0.6, 0.2, 45))
skl.append(Food("łąka przed i początek kwitnienia", 0.196, 1.8, 21, 1.7, 0.7, 0.2, 53))
skl.append(Food("łąka w kwiecie", 0.202, 1.7, 13, 1.8, 0.6, 0.2, 64))
skl.append(Food("koniczyna ściernianka", 0.217, 2.1, 31, 2.8, 0.5, 0.2, 47))
skl.append(Food("pastwisko/łąka 3 pokos odrost 6 tygodni", 0.322, 3.6, 36, 0.7, 0.4, 0.1, 79))
skl.append(Food("lucerna 1 pokos początek kwitnienia", 0.329, 3.8, 42, 0.9, 0.4, 0.1, 88))
skl.append(Food("mieszanka traw z koniczyną cz. lub lucerną 1 pokos", 0.345, 3.9, 38, 0.9, 0.4, 0.1, 100))
skl.append(Food("mieszanka traw z koniczyną cz. lub lucerną 2 pokos", 0.368, 4, 38, 1, 0.4, 0.1, 117))
skl.append(Food("kiszonka z kukurydzy 30-35% SM", 0.323, 3.9, 21, 3.3, 1.1, 0.1, 72))
skl.append(Food("kiszonka z kukurydzy 25-30% SM", 0.277, 3.5, 21, 0.4, 1.1, 0.1, 55))
skl.append(Food("susz z traw", 0.914, 10.3, 76, 8, 3.7, 0.7, 229))
skl.append(Food("susz z lucerny", 0.917, 10.3, 121, 17, 2.9, 0.6, 274))
skl.append(Food("słoma owsiana", 0.865, 5.8, 11, 3, 1.1, 1.6, 333))
skl.append(Food("słoma jęczmienna", 0.860, 5.5, 10, 2.5, 0.9, 1.3, 324))
skl.append(Food("słoma pszenna", 0.875, 5.1, 12, 2.5, 0.9, 1.2, 397))
#skl.append(Food("marchew", 0.120, 1.1, 0.6, 0.4, 0.3, 0.3, 1))
#skl.append(Food("buraki pastewne", 0.156, 1.9, 7, 0.5, 0.4, 0.4, 8))
skl.append(Food("wysłodki prasowane 18-24% SM", 0.192, 2.2, 14, 1.4, 0.8, 0.4, 35))
skl.append(Food("owies", 0.895, 12.1, 80, 1.1, 3.2, 0.2, 114))
skl.append(Food("jęczmień", 0.881, 11.7, 82, 0.6, 4.1, 0.2, 47))
skl.append(Food("kukurydza", 0.887, 12.9, 73, 0.4, 3.2, 0.1, 23))
skl.append(Food("pszenica", 0.881, 12.4, 92, 0.4, 3.7, 0.1, 31))
skl.append(Food("pszenżyto", 0.888, 10.1, 88, 0.4, 3.6, 0.1, 26))
skl.append(Food("bobik", 0.890, 13.2, 201, 1.2, 4.8, 0.2, 82))
skl.append(Food("otręby pszenne", 0.882, 9.7, 107, 1.3, 11.6, 0.4, 79))
skl.append(Food("otręby jęczmienne", 0.875, 10.2, 89, 1.2, 10.2, 0.4, 110))
skl.append(Food("młóto suszone", 0.9, 11.3, 184, 3.1, 4.6, 0.3, 207))
skl.append(Food("śruta poekstrakcyjna sojowa >46% BO", 0.89, 14.7, 367, 3, 6.4, 0.3, 50))
skl.append(Food("śruta poekstrakcyjna sojowa 42-46% BO", 0.894, 14.6, 320, 3, 6.3, 0.3, 61))
skl.append(Food("wysłodki suche", 0.899, 10.2, 58, 6.7, 10, 2.2, 199))
skl.append(Food("łubin biały", 0.888, 13.6, 265, 2, 4.9, 0.4, 145))
skl.append(Food("łubin żółty słodki", 0.896, 13.8, 281, 2.1, 4.9, 0.4, 135))
skl.append(Food("drożdże piwne suszone", 0.936, 13.9, 393, 2.1, 15.2, 1.4, 0))
skl.append(Food("wywar gorzeln. z kukurydzy", 0.924, 14.1, 224, 0.7, 5.3, 0.1, 100))

def wypisz_dane_skladnikow(skladniki):
    for food in skladniki:
        print(str(food.nazwa)
              + "\n\tmasa:\t\t" + str(round(food.waga,4))
              + "kg\n\tsucha masa:\t\t" + str(round(food.SM,4))
              + "kg\n\tenergia strawna:\t\t" + str(round(food.ES,4))
              + "MJ\n\tbialko:\t" + str(round(food.bialko,4))
              + "g\n\twapń:\t\t" + str(round(food.wapn,4))
              + "g\n\tfosfor:\t\t" + str(round(food.fosfor,4))
              + "g\n\tsod:\t\t" + str(round(food.sod,4))
              + "g\n\twlokna:\t\t" + str(round(food.wlokno,4)) + "g")

        print()


def losuj_proporcje(iloscWag):
    if iloscWag == 2:
        waga1 = random.uniform(0.3, 0.6)
        waga2 = 1-waga1
        return waga1, waga2

    elif iloscWag == 3:
        waga1 = random.uniform(0.3, 0.6)
        waga2 = random.uniform(0.15, 1-waga1)
        waga3 = 1 - waga1 - waga2
        return waga1, waga2, waga3

    elif iloscWag == 4:
        waga1 = random.uniform(0.3, 0.6)
        waga2 = 1-waga1
        waga3 = random.uniform(0.3, 0.6)
        waga4 = 1-waga3
        return waga1/2, waga2/2, waga3/2, waga4/2

    elif iloscWag == 5:
        waga1 = random.uniform(0.3, 0.6)
        waga2 = random.uniform(0.15, 1 - waga1)
        waga3 = 1 - waga1 - waga2
        waga4 = random.uniform(0.2, 0.7)
        waga5 = 1 - waga4
        return waga1/2, waga2/2, waga3/2, waga4/2, waga5/2

    else:
        waga1 = random.uniform(0.2, 0.8)
        waga2 = 1 - waga1
        waga3 = random.uniform(0.2, 0.8)
        waga4 = 1 - waga3
        waga5 = random.uniform(0.2, 0.8)
        waga6 = 1 - waga5
        return waga1/3, waga2/3, waga3/3, waga4/3, waga5/3, waga6/3

def wybierz_skladniki(skladniki, masa, sianko):
    if sianko == True:
        numOfFood = 2
    else:
        numOfFood = random.randint(5,6)
    proporcje = losuj_proporcje(numOfFood)

    wylosowaneSkladniki = random.sample(skladniki, numOfFood)

    i = 0
    for food in wylosowaneSkladniki:
        wsp = proporcje[i] * masa / food.SM
        food.waga *= wsp
        food.SM *= wsp
        food.ES *= wsp
        food.bialko *= wsp
        food.wapn *= wsp
        food.fosfor *= wsp
        food.sod *= wsp
        food.wlokno *= wsp
        i += 1
    return wylosowaneSkladniki




def oblicz_podobienstwo(ES, bialko, wapn, fosfor, sod, wlokno, waga):
    ESSim = 1 - abs(ES - perfES) / max(ES, perfES)
    bialkoSim = 1 - abs(bialko - perfBialko) / max(bialko, perfBialko)
    wapnSim = 1 - abs(wapn - perfWapn) / max(wapn, perfWapn)
    fosforSim = 1 - abs(fosfor - perfFosfor) / max(fosfor, perfFosfor)
    sodSim = 1 - abs(sod - perfSod) / max(sod, perfSod)
    wloknoSim = 1 - abs(wlokno - perfWlokno * waga) / max(wlokno, perfWlokno * waga)

    return (ESSim + bialkoSim + wapnSim + fosforSim + sodSim + wloknoSim) / 6


suchaMasa = 8     # sucha masa = 1kg * 5.5 = 5.5kg
perfES = 115.025      # 80MJ
perfBialko = 575.125  # 400g
perfWapn = 24.725     # 21.5g
perfFosfor = 12.9     # 12.9g
perfSod = 60.5        # 8.6g
perfWlokno = 0.15 * 1000

tries = 0
triesOverall = 0
bestTry = 0
while True:
    wybraneSkladniki = wybierz_skladniki(copy.deepcopy(skl), suchaMasa, sianko=False)

    skladniki = wybraneSkladniki

    ES = 0
    SM = 0
    bialko = 0
    wapn = 0
    fosfor = 0
    sod = 0
    waga = 0
    wlokno = 0

    for food in skladniki:
        ES += food.ES
        SM += food.SM
        bialko += food.bialko
        wapn += food.wapn
        fosfor += food.fosfor
        sod += food.sod
        waga += food.waga
        wlokno += food.wlokno

    roznicaSod = perfSod - sod
    dzielnik = 365/roznicaSod
    skladniki.append(Food("Sól paszowa", 0.99/dzielnik, 0, 0, 25/dzielnik, 0, 365/dzielnik, 0, 1/dzielnik))
    SM += (0.99/dzielnik)
    wapn += (25/dzielnik)
    sod += (365/dzielnik)
    waga += (1/dzielnik)

    #roznicaES = perfES - ES
    #dzielnik = 35.4/roznicaES
    dzielnik = 3
    skladniki.append(Food("Oleje roślinne", 0.9907/dzielnik, 35.4/dzielnik, 0, 0, 0, 0, 0, 1/dzielnik))
    SM += (0.9907 / dzielnik)
    ES += (35.4 / dzielnik)
    waga += (1 / dzielnik)

    podobienstwo = oblicz_podobienstwo(ES, bialko, wapn, fosfor, sod, wlokno, waga)

    if bestTry < podobienstwo:
        bestTry = podobienstwo
        print(str(int(bestTry * 10000) / 100) + "% - " + str(triesOverall) + " prób")

    if podobienstwo >= 0.91:            # tutaj wybierasz podobieństwo losowanych wynikow do docelowych wartości
        wypisz_dane_skladnikow(skladniki)

        print(bestTry)
        print("Energia strawna: \t" + str(round(ES, 4)) + "\t/" + str(perfES) + "\t\t// " + str(round(ES / perfES, 4)))
        print("Białko strawne: \t" + str(round(bialko, 4)) + "\t/" + str(perfBialko) + "\t// " + str(round(bialko / perfBialko, 4)))
        print("Wapń: \t\t\t\t" + str(round(wapn, 4)) + "\t/" + str(perfWapn) + "\t// " + str(round(wapn / perfWapn, 4)))
        print("Fosfor: \t\t\t" + str(round(fosfor, 4)) + "\t/" + str(perfFosfor) + "\t// " + str(round(fosfor / perfFosfor, 4)))
        print("Sód: \t\t\t\t" + str(round(sod, 4)) + "\t/" + str(perfSod) + "\t// " + str(round(sod / perfSod, 4)))
        print("Włókno: \t\t\t" + str(round(wlokno, 4)) + "\t/" + str(perfWlokno * waga) + "\t// " + str(round(wlokno / (perfWlokno * waga), 4)))
        print("Masa sucha: \t\t" + str(SM))
        print("Masa calkowita: \t" + str(waga))
        print("Łączna ilość prób: ", triesOverall)

    if podobienstwo >= 0.996:
        break

    triesOverall += 1

wypisz_dane_skladnikow(skladniki)

print(bestTry)
print("Energia strawna: \t" + str(round(ES, 4)) + "\t/" + str(perfES) + "\t\t// " + str(round(ES / perfES, 4)))
print("Białko strawne: \t" + str(round(bialko, 4)) + "\t/" + str(perfBialko) + "\t// " + str(round(bialko / perfBialko, 4)))
print("Wapń: \t\t\t\t" + str(round(wapn, 4)) + "\t/" + str(perfWapn) + "\t// " + str(round(wapn / perfWapn, 4)))
print("Fosfor: \t\t\t" + str(round(fosfor, 4)) + "\t/" + str(perfFosfor) + "\t// " + str(round(fosfor / perfFosfor, 4)))
print("Sód: \t\t\t\t" + str(round(sod, 4)) + "\t/" + str(perfSod) + "\t// " + str(round(sod / perfSod, 4)))
print("Włókno: \t\t\t" + str(round(wlokno, 4)) + "\t/" + str(perfWlokno) + "\t// " + str(round(wlokno / perfWlokno, 4)))
print("Masa sucha: \t\t" + str(SM))
print("Masa calkowita: \t" + str(waga))
print("Łączna ilość prób: ", triesOverall)


