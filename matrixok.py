# Mátrixok
import random
import numpy as np
import matplotlib.pyplot as plt

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

# Megszámlálás tétele:
# Hány elem van a mátrixban ami 3-mal osztható?
z = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] % 3 == 0:
            z += 1
print("A hárommal oszthatók száma:", z)
# Feltételes összegzés:
# Határozzuk meg a páratlan számok összegét a listában
l = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] % 2 == 1:
            l += mtx[i][j]
print("A páratlan számok összege:", l)

# Bónusz:
# Hozzunk létre egy új listát, ennek a listának az elemei, a mtx sorainak elemeinek a szorzata 

lista = []
for i in range(len(mtx)):
    szorzat = 1
    for j in range(len(mtx[i])):
        szorzat *= mtx[i][j]
    lista.append(szorzat)
print("Soronkénti szorzatok =", lista)

# List comprehension
lista = [i for i in range(10)]
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = [0 for i in range(5)]
print(lista) # [0, 0, 0, 0, 0]
lista = [i**2 - 3*i + 1 for i in range(15)]
print(lista)
lista = [random.randint(0, 100) for i in range(30)]
print(lista) #[14, 29, 62, 26, ..., 11, 24, 68, 63, 100, 27, 65]
lista = [[] for i in range(10)] 
print(lista) # [[], [], [], [], [], [], [], [], [], []]
lista = [[i, i**2, "kiscica"] for i in range(2,5)]
print(lista) # [[2, 4, 'kiscica'], [3, 9, 'kiscica'], [4, 16, 'kiscica']]
lista = [[j for j in range(8)] for i in range(10)]
for item in lista:
    print(item)
mtx3d = [[[random.randint(-20, 20) for k in range(5)] for j in range(3)] for i in range(2)]
print(mtx3d) 

# Összegzés tétele 3D mátrixra
# Annyi for ciklus kell, ahány dimenziós a lista
összeg = 0
for i in range(len(mtx3d)):
    for j in range(len(mtx3d[i])):
        for k in range(len(mtx3d[i][j])):
            összeg += mtx3d[i][j][k]
print(összeg)

# 1D listát  bejárni: n lépésből
# 2D listát (nxn-es): n*n lépésből (n^2)
# 3D listát: n*n*n lépésből (n^3)
# aD listát: n^a lépésből

# Kokckák ábrázolása egy 3D koordináta rendszerben:
axes = [5, 5, 5]
cube = np.ones(axes) # 5*5*5-ös mátrixot fog létrehozni, tele egyesekkel
colors = np.empty(axes + [3]) # 5*5*5*3-as mátrix, nem állít be alap értéket
print(type(colors[0][0][0][0])) # <class 'numpy.float64'>
print(colors[0][0][0])

colors[0] = [1,0,0] # Piros
colors[1] = [0,1,0] # Zöld
colors[2] = [0,0,1] # Kék
colors[3] = [1,1,0] # Sárga
colors[4] = [0,1,1] # Türkíz

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(cube, facecolors=colors, edgecolors="black", alpha=0.8)
plt.show()





