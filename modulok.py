from random import randrange, seed
import math as matek
import numpy as np              # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
from matplotlib.colors import LinearSegmentedColormap

def modulok_bevezeto():
    seed(123456789)
    print(randrange(1, 11)) # 1-10 között random egész szám
    print(randrange(1, 11)) # 1-10 között random egész szám

    print(matek.pi) # 3.141592653589793
    print(matek.e)  # 2.718
    print(matek.tau)
    print(matek.sqrt(2))
    print(matek.floor(4.000021)) # Lefelé kerekít
    print(matek.ceil(4.000021)) # Felfelé kerekít
    print(matek.sin(matek.radians(180))) # 1.22e-16 = 1.22 * 10^-16

    sugár = 7
    print(f"A {sugár} egység sugarú kör kerülete: {sugár * 2 * matek.pi}")
    print(f"A {sugár} egység sugarú kör kerülete: {sugár * 2 * 3.14}")

def numpy_bevezeto():
    tomb = np.array([32, 42, 32, 12, 32])
    print(type(tomb)) # <class 'numpy.ndarray'>
    print(tomb) # [32 42 32 12 32]
    print([1,2,3,4])  # [1, 2, 3, 4]
    print(tomb[3]) #12
    #tomb.append(32) A tömb mérete NEM módosítható
    tomb[3] = 11
    print(tomb[3]) # 11

    matrix = np.array([[1, 2, 3], [6, 9, 1]])
    print(matrix)
    print(matrix.shape) # (2, 3) - 2 szám -> 2 dimenziós, 2 sor 3 oszlop
    matrix = matrix.reshape(3, -1)
    print(matrix)
    print(matrix.shape)
    matrix = matrix.reshape(-1)
    print(matrix)
    print(matrix.shape)  # (6,)   - 1 dimenzió, 6 elem
    print(matrix.sum())
    print(matrix.mean())
    print(matrix.std())
    print(tomb[1:3])

   
mtx = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,0],
    [0,1,1,0,0,1,1,0],
    [0,0,0,1,1,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,0,0,1,0,0]
]
for row in mtx:
    print(row)


paletta = LinearSegmentedColormap.from_list("creeper", ["green", "black"])
plt.imshow(mtx, cmap=paletta)
plt.axis("off")
plt.savefig("creeper.png")
plt.show()