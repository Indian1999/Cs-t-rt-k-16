import random
import math
# Feladat: Adott egy 30 fős osztály matematika dolgozatainak az eredményei (százalélban)
# gauss(átlag, szórás)
szazalekok = [max(0, min(int(random.gauss(60, 30)), 100)) for i in range(30)]

# a, Hozz létre egy lsitát ami tuple-öket fog tartalmazni, minden tuple pontosan 2
# értéket tárol, egy adott diák százalékos eredményét, és az abból számolt osztályzatot
# pl.: [(45, 2), (85, 4), (99, 5) ...]

eredmenyek = []
for item in szazalekok:
    if item >= 89:
        eredmenyek.append((item, 5))
    elif item >= 72:
        eredmenyek.append((item, 4))
    elif item >= 60:
        eredmenyek.append((item, 3))
    elif item >= 40:
        eredmenyek.append((item, 2))
    else:
        eredmenyek.append((item, 1))
print(eredmenyek)

# b, Átlagosan hány százalékos dolgozatokat írtak a diákok?
összeg = 0
for item in eredmenyek: # item példa: (50, 2)
    összeg += item[0]
atlag_szazalek = összeg / len(eredmenyek)
print(f"A százalékos eredmények átlaga: {round(atlag_szazalek, 2)} %.")

# c, Mennyi lett az osztályátlag (osztályzatok átlaga)
összeg = 0
for item in eredmenyek: # item példa: (50, 2)
    összeg += item[1]
atlag_osztalyzat = összeg / len(eredmenyek)
print(f"Az osztályzatok átlaga: {round(atlag_osztalyzat, 2)}.")

# d, Hány ember írt átlag feletti dolgozatot?
szamlalo = 0
for item in eredmenyek:
    if item[0] > atlag_szazalek:
        szamlalo += 1
print(f"{szamlalo} diák írt átlag feletti dolgozatot.")

# e, A diákok hány százaléka bukott meg (1-est kapott)
szamlalo = 0
for item in eredmenyek:
    if item[1] == 1:
        szamlalo += 1
print(f"{round(szamlalo/30 * 100, 2)} diák bukott meg.")

# f, Mekkora volt a százalékos eredmények szórása
# Szórás: Átlagosan mennyivel tér el egy érték az átlagtól
összeg = 0
for item in eredmenyek:
    összeg += (item[0] - atlag_szazalek)**2
szórás_százalék = (összeg / len(eredmenyek)) ** 0.5
print(f"A százalékos eredmények szórása: {round(szórás_százalék,2)}")

# g, Melyik osztályzatból született a legtöbb?
osztalyzat_szamlalo = ["buffer", 0, 0, 0, 0, 0]
for item in eredmenyek:
    osztalyzat_szamlalo[item[1]] += 1
print(osztalyzat_szamlalo)

max_index = 1
for i in range(2, len(osztalyzat_szamlalo)):
    if osztalyzat_szamlalo[i] > osztalyzat_szamlalo[max_index]:
        max_index = i
print(f"A legtöbbet előforduló osztályzat a {max_index}, összesen {osztalyzat_szamlalo[max_index]} darab ilyen osztályzat született.")

# h, Rendezzük a listát százalékok szerint csökkenő sorrendbe
eredmenyek.sort(reverse=True)
print(eredmenyek)

# Feladat: adott 40 darab pont egy koordináta rendszerben
# Pont az egy 2 élemű tuple, pl.: (x, y)
pontok = [(random.randint(-50, 50), random.randint(-50, 50)) for i in range(40)]
print(pontok)

# a, Melyik pont van a legközelebb az orgióhoz?
min_index = 0
min_value = (pontok[0][0]**2 + pontok[0][1]**2) ** 0.5
for i in range(1, len(pontok)):
    distance = (pontok[i][0]**2 + pontok[i][1]**2) ** 0.5
    if distance < min_value:
        min_value = distance
        min_index = i
print(f"Az origóhoz legközelebbi pont: {pontok[min_index]}")

# b, Hol található ezeknek a pontoknak a mértani közepe (súlypontja)
összeg_x = 0
összeg_y = 0
for pont in pontok:
    összeg_x += pont[0]
    összeg_y += pont[1]
mertani_kozep = (round(összeg_x / len(pontok), 2), round(összeg_y / len(pontok), 2))
print("A pontok mértani közepe:", mertani_kozep)