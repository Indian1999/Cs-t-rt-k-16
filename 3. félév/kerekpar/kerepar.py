import os

path_adatok = os.path.join(os.path.dirname(__file__), "kerekpar-adatok.txt")
print(path_adatok)
print(type(path_adatok))

boltok = []

with open(path_adatok, encoding="utf-8") as f:
    mezonevek = f.readline().strip().split(";") # ['nev', 'telepules', 'szerviz_ar']
    for line in f:
        line = line.strip().split(";")
        if len(line) != 3:
            break
        bolt = {
            mezonevek[0]: line[0],
            mezonevek[1]: line[1],
            mezonevek[2]: int(line[2])
        }
        boltok.append(bolt)


#1. Írd ki, hogy hány kerékpárbolt van összesen!
print(f"Összesen {len(boltok)} kerékpár bolt van eltárolva.")

#2. Írd ki, hogy melyik boltban a legdrágább egy kerékpár szervizelése és mennyibe kerül!
max_index = 0
for i in range(1, len(boltok)):
    if boltok[i]["szerviz_ar"] > boltok[max_index]["szerviz_ar"]:
        max_index = i

print(f"A legdrágább bolt a {boltok[max_index]['nev']}, egy szervíz {boltok[max_index]['szerviz_ar']} Ft-ba kerül.")

#3.  Írj  egy  függvényt  akcio  néven,  ami  paraméterként  megkapja  a  szerviz  árát  és
#visszaadja, hogy mennyibe kerülne 20%-os kedvezménnyel!

def akcio(ar: int) -> int:
    return int(ar * 0.8)

#4. Kérj be a felhasználótól egy bolt nevet, majd írd ki, hogy az adott boltban mennyi
#lenne  a  szerviz  ár  20%-os  kedvezménnyel!  (az  előző  feladatban  lévő  függvényt
#használd fel hozzá) Ha nincs ilyen nevű bolt, akkor írd ki, hogy nincs ilyen bolt!

boltnev = input("Add meg egy bolt nevét: ")
for bolt in boltok:
    if bolt["nev"] == boltnev:
        print(f"Ebben a boltban 20% kedvezménnyel {akcio(bolt['szerviz_ar'])} Ft lenne a szervíz.")
        break
else:
    # Akkor fut le, ha NEM break-kel léptünk ki.
    print("Nincs ilyen nevű bolt!")

#5. Írd ki a kerekpar-export.txt fájlba a Budapesti boltok neveit!

path_export = os.path.join(os.path.dirname(__file__), "kerekpar-export.txt")

with open(path_export, "w", encoding="utf-8") as f:
    print("'kerekpar-export.txt' létrehozva.")
    for bolt in boltok:
        if bolt["telepules"] == "Budapest":
            f.write(bolt["nev"] + "\n")