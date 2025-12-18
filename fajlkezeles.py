import os

file = open("story.txt", "r", encoding="utf-8")
#szöveg = file.read() # egész szöveget beolvassa
print(file.read(10)) # 10 KARAKTERT beolvas
print(file.read(20))
file.seek(0) # Ez olvasófejet a 0. karakterre helyezi
print(file.read(11))
file.close()

# Context Manager (with), a fájl csak a with-en belül érhető el
with open("story.txt", "r", encoding="utf-8") as f:
    data = f.readlines() # ["sor1\n", "sor2\n", "sor3\n", ...]

with open("homerseklet.txt", "r", encoding="utf-8") as f:
    homersekletek = []
    for line in f:
        line = line.strip() # Leszedi a whitespace karaktereket az elejéről és a végéről
        line = line.split(";") # ['13', '15', '11', '29', '24', '27', '10']
        szamok = [int(item) for item in line]
        print(szamok) # [14, 33, -3, -5, -5, 9, 14]
        homersekletek.append(szamok)


# Feladat: Olvassuk be a pontok.txt fájl tartalmát és tároljuk el egy megfelelő adatszerkezetben.
# Két 3D pont távolsága: ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) ** 0.5

# a, Írjuk ki azt a pontot amelyik a legközelebb van az origóhoz

# b, Írjuk ki az egymástól legtávolabb lévő 2 pontot (***)