# Mátrixok
import random
import numpy as np
import matplotlib.pyplot

# A mátrix az egy olyan lista, ami listákat tárol

mtx = [
#    0  1  2  3  4  5  6 
    [4, 3, 1, 3, 4, 7, 3], # 0
    [0, 1, 5, 3, 1, 3, 5], # 1
    [7, 3, 0, 6, 4, 0, 2], # 2
    [1, 2, 9, 3, 7, 1, 2], # 3
    [3, 8, 1, 2, 4, 0, 3]  # 4
]
print(mtx)
for row in mtx:
    print(row)
print("indexelés:")
print("mtx[2] =", mtx[2])
print("mtx[2][4] =", mtx[2][4])

# Programozási tételek mátrixokra:
# Sor-oszlop vagy oszlop-sor bejárással

# Összegzés tétele:
összeg = 0
for i in range(len(mtx)): # A sorokon megyünk végig
    for j in range(len(mtx[i])): # Az oszlopokon megyünk végig
        összeg += mtx[i][j]
print("Összeg =", összeg)
print("Átlag =", round(összeg / (len(mtx) * len(mtx[0])), 2))

# Maximum kiválasztás:
maximum = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] > maximum:
            maximum = mtx[i][j]
print("Maximum =", maximum)

# Eldöntés tétele:
# Döntsük, el, hogy tarlmaz-e 7-tel osztható számot a mátrix
feltétel = False
counter = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        counter += 1
        if mtx[i][j] % 7 == 0:
            feltétel = True
            break # kilép a ciklusból
    if feltétel:
        break

print(counter, "elemet ellenőriztünk.")  # 35 -> 19 -> 6
if feltétel:
    print("Van benne 7-tel osztható szám.")
else:
    print("Nincs benne 7-tel osztható szám.")


