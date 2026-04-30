import os
import random

path = os.path.join(os.path.dirname(__file__), "forras", "casino_log.txt")
f = open(path, "a", encoding="utf-8")

bemenet = "valami"
while bemenet != "":
    bemenet = input("Gondoltam egy számra, 1-100 között, találd ki! (Üres string kilépéshez)\n")
    f.write("Gondoltam egy számra, 1-100 között, találd ki! (Üres string kilépéshez)\n")
    f.write(bemenet + "\n")
    if bemenet == "" or not bemenet.isdigit():
        continue
    szam = random.randint(1, 100)
    if int(bemenet) == szam:
        print("Eltaláltad!")
        f.write("Eltaláltad!\n")
    else:
        print(f"Nem talált! A gondolt szám: {szam}. Gondolok egy újat!")
        f.write(f"Nem talált! A gondolt szám: {szam}. Gondolok egy újat!\n")

f.write("Kilépés!\n\n")

f.close()