import random
import copy

class Food:
    def __init__(self, nazwa, kcal, bialko, tluszcz, waga=0):
        self.nazwa = nazwa
        self.kcal = kcal
        self.bialko = bialko
        self.tluszcz = tluszcz
        self.waga = waga


mieso = []
mieso.append(Food("cielęcina", 110, 20, 3))
mieso.append(Food("cielęcina gotowana", 196, 32, 7))
mieso.append(Food("gęś (pierś-mięso)", 162, 22.5, 2))
mieso.append(Food("gęś (udo-mięso)", 195, 20, 4.7))
mieso.append(Food("gęś (tuszka)", 339, 14, 32))
mieso.append(Food("indyk (pierś - mięso)", 103, 24, 0.7))
mieso.append(Food("indyk (udo - mięso)", 113, 18, 4))
mieso.append(Food("indyk (tuszka)", 158, 17, 6.8))
mieso.append(Food("jajko całe", 178, 13.6, 11.8))
mieso.append(Food("jajko całe gotowane", 155, 15.3, 11))
mieso.append(Food("jajko żółtko gotowane", 182, 16.7, 15.3))
mieso.append(Food("kurczak (pierś - mięso)", 109, 23, 1.3))
mieso.append(Food("kurczak (udo - mięso)", 114, 19, 4))
mieso.append(Food("kurczak (tuszka)", 158, 18.6, 9.3))
mieso.append(Food("twaróg chudy", 86, 18, 0.2))
mieso.append(Food("twaróg półtłusty", 116, 16, 4))
mieso.append(Food("wieprzowina - nerki", 102, 16.8, 3.8))
mieso.append(Food("wieprzowina - schab", 174, 21, 10))
mieso.append(Food("wieprzowina - serce", 111, 16.9, 4.8))
mieso.append(Food("wieprzowina - szynka surowa", 261, 18, 21.3))
mieso.append(Food("wieprzowina - wątroba", 130, 22, 3.4))
mieso.append(Food("wołowina - nerki", 95, 15.6, 3.6))
mieso.append(Food("wołowina - serce", 117, 16.9, 5.3))
mieso.append(Food("wołowina - wątroba", 125, 20, 3.1))

warzywa = []
warzywa.append(Food("brokuł gotowany", 33.5, 2.4, 0.4))
warzywa.append(Food("burak gotowany", 38, 1.8, 0.1))
warzywa.append(Food("cukinia gotowana", 15, 1.2, 0.1))
warzywa.append(Food("dynia gotowana", 28, 1.3, 0.3))
warzywa.append(Food("groszek zielony", 68, 4, 1))
warzywa.append(Food("jarmuż", 29, 3.3, 0.7))
warzywa.append(Food("kalafior gotowany", 22, 2.4, 0.2))
warzywa.append(Food("marchewka", 57.4, 1.3, 0.3))
warzywa.append(Food("marchewka gotowana", 35, 1, 0.1))
warzywa.append(Food("pietruszka - korzeń", 82, 2.6, 0.5))
warzywa.append(Food("pietruszka - natka", 44, 4.4, 0.4))
warzywa.append(Food("seler gotowany", 13, 1, 0.2))
warzywa.append(Food("szparagi gotowane", 22, 2, 0.1))
warzywa.append(Food("ziemniaki gotowane", 7.5, 1.8, 0.1))
# nie dodaje narazie olejów

wypelniacze = []
wypelniacze.append(Food("ryż brązowy gotowany", 123, 2.7, 0.1))
wypelniacze.append(Food("kasza gryczana", 336, 12.6, 3.1))
wypelniacze.append(Food("otręby pszenne", 351, 9, 3))
wypelniacze.append(Food("otręby żytnie", 343, 6.4, 3.2))
wypelniacze.append(Food("ryż biały gotowany", 344, 3, 0.3))


def wypisz_dane_skladnikow(skladniki):
    for food in skladniki:
        print(str(food.nazwa) + "\n\tkcal:\t\t" + str(round(food.kcal,2)) + "\n\tbialko:\t\t" + str(round(food.bialko,2)) + "g\n\ttluszcz:\t" + str(round(food.tluszcz,2)) + "g\n\twaga:\t\t" + str(int(round(food.waga * 100,0))) + "g")
        print()


def losuj_proporcje(iloscWag):
    if iloscWag == 1:
        return [1]

    elif iloscWag == 2:
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
        waga2 = 1 - waga1
        waga3 = random.uniform(0.3, 0.6)
        waga4 = 1 - waga3
        return waga1/2, waga2/2, waga3/2, waga4/2

    else:
        waga1 = random.uniform(0.3, 0.6)
        waga2 = 1 - waga1
        waga3 = random.uniform(0.3, 0.6)
        waga4 = random.uniform(0.15, 1 - waga3)
        waga5 = 1 - waga3 - waga4
        return waga1/2, waga2/2, waga3/2, waga4/2, waga5/2

def wybierz_skladniki(skladniki, masa, wypelniacze=False):
    if wypelniacze:
        numOfFood = 1
    else:
        numOfFood = random.randint(2,3)
    proporcje = losuj_proporcje(numOfFood)

    wylosowaneSkladniki = random.sample(skladniki, numOfFood)

    i=0
    for food in wylosowaneSkladniki:
        faktycznaWaga = proporcje[i] * masa/3
        food.waga = faktycznaWaga
        food.kcal = food.kcal * faktycznaWaga
        food.bialko = food.bialko * faktycznaWaga
        food.tluszcz = food.tluszcz * faktycznaWaga
        i+=1
    return wylosowaneSkladniki

def oblicz_podobienstwo(kcal, bialko, tluszcz, perfKcal, perfBialko, perfTluszcz):
    kcalSim = 1 - abs(kcal - perfKcal) / max(kcal, perfKcal)
    bialkoSim = 1 - abs(bialko - perfBialko) / max(bialko, perfBialko)
    tluszczSim = 1 - abs(tluszcz - perfTluszcz) / max(tluszcz, perfTluszcz)

    return (kcalSim + bialkoSim + tluszczSim) / 3





perfBialko = 79.95          #dobieranie docelowego białka
perfTluszcz = 24.43         #dobieranie docelowego tłuszczu
perfKcal = 1776.63          #dobieranie docelowych kalorii
masa = 12.07               #całkowita masa karmy, np. 6 = 6*100g = 600g


tries = 0
triesOverall = 0
bestTry = 0
bestSector = 0
while True:
    wybraneMieso = wybierz_skladniki(copy.deepcopy(mieso), masa)
    wybraneWarzywa = wybierz_skladniki(copy.deepcopy(warzywa), masa)
    wybraneWypelniacze = wybierz_skladniki(copy.deepcopy(wypelniacze), masa)

    skladniki = wybraneMieso + wybraneWarzywa + wybraneWypelniacze

    kcal = 0
    bialko = 0
    tluszcz = 0

    x = 0.8
    #skladniki.append(Food("Olej rzepakowy", 93.2*x, 0, 9.99*x, 10*x))
    #skladniki.append(Food("Olej rzepakowy", 139.8, 0, 14.985, 15))

    for food in skladniki:
        kcal += food.kcal
        bialko += food.bialko
        tluszcz += food.tluszcz
    podobienstwo = oblicz_podobienstwo(kcal, bialko, tluszcz, perfKcal, perfBialko, perfTluszcz)

    if bestTry < podobienstwo:
        bestTry = podobienstwo
        print(str(int(bestTry * 10000) / 100) + "% - " + str(triesOverall) + " prób")

    if podobienstwo >= 0.97:
        print("\n--------------------------------")
        wypisz_dane_skladnikow(skladniki)
        print("kcal: \t\t\t" + str(round(kcal, 2)) + "\t/" + str(perfKcal) + " " + str(round(kcal / perfKcal,2)))
        print("bialko: \t\t" + str(round(bialko, 2)) + "g" + "\t/" + str(perfBialko) + "g" + " " + str(round(bialko / perfBialko,2)))
        print("tluszcz: \t\t" + str(round(tluszcz, 2)) + "g" + "\t/" + str(perfTluszcz) + "g" + " " + str(round(tluszcz / perfTluszcz,2)))
        print("podobienstwo: \t" + str(int(podobienstwo * 10000) / 100) + "%")
        print("--------------------------------\n")

    if podobienstwo >= 0.99:            # tutaj wybierasz podobieństwo losowanych wynikow do docelowych wartości
        break

    if bestSector < podobienstwo:
        bestSector = podobienstwo

    if tries >= 50000:
        tries = 0
        print("<" + str(triesOverall) + " prób>")
        print("Najlepszy ostatnie 50000 prób: " + str(int(bestSector * 10000) / 100) + "%")
        bestSector = 0


    triesOverall += 1
    tries += 1

wypisz_dane_skladnikow(skladniki)

print("kcal: \t\t\t" + str(round(kcal,2)) + "\t/" + str(perfKcal) + " " + str(kcal/perfKcal))
print("bialko: \t\t" + str(round(bialko,2)) + "g" + "\t/" + str(perfBialko) + "g" + " " + str(bialko/perfBialko))
print("tluszcz: \t\t" + str(round(tluszcz,2)) + "g" + "\t/" + str(perfTluszcz) + "g" + " " + str(tluszcz/perfTluszcz))
print("podobienstwo: \t" + str(int(podobienstwo*10000)/100) + "%")
print("Łączna ilość prób: ", triesOverall)


