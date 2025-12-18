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

s = []
with open("pontok.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip().split(",")
        s.append([int(x) for x in line])
 
 
legkozelebbi = s[0]
min_tav = (legkozelebbi[0]**2 + legkozelebbi[1]**2 + legkozelebbi[2]**2) ** 0.5
for item in s:
    t = (item[0]**2 + item[1]**2 + item[2]**2) ** 0.5
    if t < min_tav:
        min_tav = t
        legkozelebbi = item
print("a)", legkozelebbi)
 
 
max_tav = -1
p1 = p2 = None
for i in range(len(s)-1):
    for j in range(i + 1, len(s)):
        a, b = s[i], s[j]
        t = ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) ** 0.5
        if t > max_tav:
            max_tav = t
            p1, p2 = a, b
print("b)", p1, p2)

print(__file__) # c:\Users\Meggyecske\Desktop\Cs-t-rt-k-16\fajlkezeles.py
kimenetek_path = os.path.dirname(__file__) # c:\Users\Meggyecske\Desktop\Cs-t-rt-k-16
print(kimenetek_path)
kimenetek_path = os.path.join(kimenetek_path, "kimenetek")
print(kimenetek_path) # c:\Users\Meggyecske\Desktop\Cs-t-rt-k-16\kimenetek

with open(os.path.join(kimenetek_path, "pontok_kimenet.txt"), "w", encoding="utf-8") as f:
    f.write(f"a) {legkozelebbi}\n")
    f.write(f"b) {p1}, {p2}\n")
    f.write("Látod itt felül lett írva")

# Ha 'w' módban nyitunk meg egy fájlt és a fájl már létezik, akkor felül fogja írni a teljes tartalmát

# Az 'a' mód az nem törli a fájl addigi tartalmát. de ugyanúgy lehet hozzá írni
with open("story.txt", "a", encoding="utf-8") as f:
    f.write("Kiegészítem a sotry.txt fájlt egy picit...\n")

# A + jel annyit jelent, hogy írni és olvasni is tudunk
# "w+", törli a fájl addigi tartalmát, és tudunk bele írni, de olvasni is tudjuk
with open("story.txt", "w+", encoding="utf-8") as f:
    pass

# Írni és olvasni, nem törli a tartalmát, az olvasó fej a végéről indul
with open("story.txt", "a+", encoding="utf-8") as f:
    pass

# Írni és olvasni, nem törli a tartalmát, az olvasó fej az elejéről indul
with open("story.txt", "r+", encoding="utf-8") as f:
    pass

 