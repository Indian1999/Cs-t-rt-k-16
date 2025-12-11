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

# c, Mennyi lett az osztályátlag (osztályzatok átlaga)

# d, Hány ember írt átlag feletti dolgozatot?

# e, Mekkora volt a százalékos eredmények szórása
# Szórás: Átlagosan mennyivel tér el egy érték az átlagtól

# f, Melyik osztályzatból született a legtöbb?

# g, A diákok hány százaléka bukott meg (1-est kapott)