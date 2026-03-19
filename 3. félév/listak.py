import math
import random
import matplotlib.pyplot as plt # pip install matplotlib.pyplot   (terminálba)

# List Comprehension

# Ennek segítségével tudunk listákat generálni könnyen

# Feladat: Legyen egy listánk számokkal 1-től 100-ig

# Hagyományos módszerrel:
lista = []
for i in range(1, 101):
    lista.append(i)

# List comprehension-nel:
lista = [0 for i in range(10)] # 10 -szer belerakunk egy 0-t
print(lista) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lista = [i for i in range(10)] 
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = [i**2 for i in range(1, 11)]
print(lista) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista = [round(math.cos(math.radians(i)), 4) for i in range(0, 361, 15)]
print(lista)

lista = [random.randint(1, 9) for i in range(10)]
print(lista)

def polinom(x):
    return 3*x**2 + 2 *  x - 10

lista = [polinom(i) for i in range(-5, 5)]
print(lista)

matrix = [[] for i in range(10)]
print(matrix)

matrix = [[1,2,3,4] for i in range(5)]
print(matrix) # [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

matrix = [[j*i for j in range(1,6)] for i in range(1,4)]
print(matrix) # [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

kep = [[[random.randint(0, 255) for k in range(3)] for j in range(300)] for i in range(150)]

#plt.imshow(kep)
#plt.show()

# A listák indexelése:

lista = [i**2 for i in range(1, 21)]
print(lista)

print(lista[0])   # 1
print(lista[5])   # 6^2 = 36
print(lista[-1])  # Hátulról az első (20^2 = 400)
print(lista[-5])  # Hátulról az 5. (16^2 = 256)
#print(lista[20])  # IndexError: list index out of range

print(lista[3:10])  # 3. indextől a 10. indexig (10-ik már nincs benne) [16, 25, 36, 49, 64, 81, 100]
print(lista[:5])    # Az elejétől az 5. indexig [1, 4, 9, 16, 25]
print(lista[17:])   # A 17. indextől a végéig [324, 361, 400]
print(lista[:])     # Az elejétől a végéig

print(lista[1:12:2])  # 1-től 12-ig, kettesével lépkedve [4, 16, 36, 64, 100, 144]
print(lista[1:12:-1]) # 1-től 12.ig, hátrafele lépkedve  []
print(lista[8:1:-1])  # 8-tól 1-ig (1 már nincs benne), hátrafelé   [81, 64, 49, 36, 25, 16, 9]
print(lista[::-1])    # megfordítja a listát
print(lista[::5])     # [1, 36, 121, 256]

# lista függvények:

lista.append(441) # A lista végére rakja a 441
print(lista.pop())  # Törli (és visszaadja) az utolsó elemet
print(len(lista))   # 20
print(lista.insert(10, "10. indexre"))
print(lista)
print(lista.pop(10)) # 10. indexet törli
print(lista)
lista.remove(225) # a 225 első előfordulását törli
print(lista)
#lista.remove(4131432) # ValueError: list.remove(x): x not in list
del lista[0] # lista 0. elemét törli
print(lista)


print(max(lista))
print(min(lista))
print(sum(lista))
print(sum(lista)/len(lista))

lista.sort(reverse=True)  # Csökkenő sorrendbe rendezi helyben!
print(lista) # [400, 361, 324, 289, 256, 196, 169, 144, 121, 100, 81, 64, 49, 36, 25, 16, 9, 4]

lista = sorted(lista)  
print(lista) # [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 256, 289, 324, 361, 400]



# List comprehension gyakorlása:

# 1. feladat: Generáljunk egy listát, ami a számokat tartalmazza, 2-13-ig
print([i for i in range(2, 14)])

# 2. feladat: Generáljunk egy listát, ami a számokat tartalmazza, 2-20-ig, de csak a párosak
print([i for i in range(2, 21, 2)])

# 3. feladat: Generáljunk egy listát, ami a számokat tartalmazza, 0-360-ig, 45-ével
print([i for i in range(0, 361, 45)])

# 4. feladat: Generáljunk egy listát, ami egy 10 sorból, 5 oszlopból álló mátrix, 
# és minden sorban ugyan az a szám szerepel, az első sorban 1, a másodikban 2, stb...

print([[i+1 for j in range(5)] for i in range(10)])

# 5. feladat: Generáljunk egy 6x6-os mátrixot, amely minden értéke: sor száma x oszlop száma
matrix = [[i+j for j in range(1, 7)] for i in range(1, 7)]
for row in matrix:
    print(row)

# 6. feladat: 3 kockával:
matrix = [[[i+j+k for k in range(1,7)] for j in range(1, 7)] for i in range(1,7)]
print(matrix)


# Mekkora az esélye annak, hogy 15-öt dobok ha 5 szabályos dobokókockával gurítok?

matrix_5_kocka = [[[[
        [i+j+k+l+m for m in range(1,7)]
        for l in range(1,7)] for k in range(1,7)] for j in range(1,7)] for i in range(1, 7)
    ]

szamlalo = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                for m in range(6):
                    if matrix_5_kocka[i][j][k][l][m] == 15:
                        szamlalo += 1
print(f"5 kokckával a 15-nek dobásának az esélye: {round(szamlalo/6**5 *100 ,2)} %")

# Mekkora az esélye annak, hogy 10-et dobok, ha 3 darab szabályos (6 oldalú) és 1db 4 oldalú kockával dobok?

matrix_3_plus_1 = [[[[
        l + k + j + i for l in range(1,5)] for k in range(1,7)] for j in range(1,7)] for i in range(1, 7)
    ]

szamlalo = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(4):
                if matrix_3_plus_1[i][j][k][l] == 10:
                    szamlalo += 1
print(f"3 d6-tal és 1 d4-el a 10-nek a dobási esélye: {round(szamlalo/(6**3 * 4) *100 ,2)} %")

# Melyik számnak a legnagyobb az esélye, ha 4 darab szabályos kockával dobok?

matrix_4_kocka = [[[[
        l + k + j + i for l in range(1,7)] for k in range(1,7)] for j in range(1,7)] for i in range(1, 7)
    ]

elofordulasok = {}

for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                szam = matrix_4_kocka[i][j][k][l]
                if szam in elofordulasok.keys():
                    elofordulasok[szam] += 1
                else:
                    elofordulasok[szam] = 1

print(elofordulasok)

max_value = 0
max_key = None
for key in elofordulasok:
    if elofordulasok[key] > max_value:
        max_value = elofordulasok[key]
        max_key = key

print(f"4 kockával a {max_key}-es dobásnak a legnagyobb az esélye. {elofordulasok[max_key]/6**4 * 100} %.")
