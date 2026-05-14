"""
Írj programot, amely:
1. Létrehoz egy tuple-t 5 diák nevével
2. Létrehoz egy listát a jegyeikkel
3. Kiírja párosítva a neveket és jegyeket
4. Megpróbálja módosítani a tuple egyik elemét (try-except)
5. A listában kicseréli a legrosszabb jegyet 5-re
6. Kiírja az új jegy-listát
"""

nevek = ("András", "Béla", "Cecil", "Dénes", "Elemér")
jegyek = [3,5,2,1,4]

for i in range(len(nevek)):
    print(f"{nevek[i]}: {jegyek[i]}")

try:    
    nevek[1] = "Bea" # TypeError: 'tuple' object does not support item assignment
except Exception as ex:
    print("HIBA")
    print(ex)

nevek = list(nevek)
nevek[1] = "Bea"
nevek = tuple(nevek)
print(nevek)


min_index = 0
for i in range(1, len(jegyek)):
    if jegyek[i] < jegyek[min_index]:
        min_index = i

jegyek[min_index] = 5
print(jegyek)

"""
Írj programot, amely bekér egy pozitív egész számot, és eldönti, hogy prímszám-e! A
program addig kérjen be számot, amíg pozitív egész számot nem kap!
"""
import math
#szam = input("Adj meg egy pozitív egész számot: ")
szam = "87178291199"
while not szam.isdigit() or int(szam) <= 0:
    szam = input("Adj meg egy pozitív egész számot: ")
szam = int(szam)

prime = True
if szam % 2 == 0:
    prime = False
else:
    for i in range(3, math.ceil(szam**0.5) + 1, 2):
        if szam % i == 0:
            prime = False
            break

if prime:
    print("Prímszám")
else:
    print("Nem prímszám")


"""
Írj programot, amely létrehoz egy 3×3-as mátrixot a felhasználó által megadott értékek-
kel, majd:
•Kiírja a mátrixot táblázatos formában
•Kiszámítja a főátló elemeinek összegét
•Kiszámítja minden sor összegét
•Megkeresi a legnagyobb elemet és annak pozícióját
"""

matrix = [
    [3, 8, 2],
    [0, 1, 7],
    [9, 5, 7]
]

for row in matrix: # row = [3, 8, 2]
    print(" ".join(str(item) for item in row))

print()

for row in matrix:
    for item in row:
        print(item, end = " ")
    print()

összeg = 0
for i in range(len(matrix)):
    összeg += matrix[i][i]
print(f"A főátló összege: {összeg}")

összegek = [0 for _ in range(len(matrix))]

for i in range(len(matrix)): # i - sorindex
    for j in range(len(matrix[i])): # j - oszlopindex
        összegek[i] += matrix[i][j]

print("Sorok összege:", összegek)

maxi = 0
maxj = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > matrix[maxi][maxj]:
            maxi = i
            maxj = j

print(f"A legnagyobb elem: {matrix[maxi][maxj]} ({maxi+1}. sor, {maxj+1}. oszlop)")

#Gyakorló feladat:

matrix = [
    [ 71,   4,  -7,  84,  25,  21,  18,   7],
    [ 84,   3,  76,  84,  59,   1,  65,  44],
    [ -6,  -7,   1,  17,  19,  54,  67,  -7],
    [ 61,  15,  81,  73,  79,  59,  43,  18],
    [ 47,  65,  25,  93, -10,  87,  93,  10],
    [ 79,  44,  33,  25,   9,  17,  87,  33],
    [  3,   1,  38,   2,  35,  98,  34,  67],
    [ 23,  93,  -5,  83,  48,  58,   5,  38],
    [  0,  60,  27,  96,  70,  69, 100,  36],
    [ 63,  14,  80,  -2,  -5,  74,  19,  88]
]

# Mennyi a mátrix elemeinek összege?

# Hanyadik sorban a legnagyobb az elemek átlaga?

# Hány negatív szám van a mátrixban?

# Mennyi a páros számok összege?

# Hanyadik oszlopban van a legtöbb negatív szám?