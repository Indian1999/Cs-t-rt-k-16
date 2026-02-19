# A Dictionary (szótár) adatszerkezet
# olyan mint c++-ben a map

szotar = {} # Üres szótár
szotar = {
    "alma": "apple",
    "banán": "banana",
    "citrom": "lemon",
    "dinnye": "melon",
    "bögre": "mug",
    "kirabolni": "mug",
    3: "three",
    "három": 3,
    "prímek": [2, 3, 5, 7],
    "3": "three",
    "prímek": [2,3,5,7,11,13,17,19]
}

# A kulcsoknak egyedieknek lenniük
# AZ értékekre nincs ilyen megkötés
print(szotar)

print(szotar["dinnye"]) # melon 
# Új elem hozzáadása:
szotar["palack"] = "bottle"
# Egy elem átírása:
# Ha egy olyan kulcsot állítok be ami már létezik, akkor csak átírja
szotar["dinnye"] = "watermelon"
# Egy elem törlése:
del szotar["citrom"]
print(szotar)

# Elemek száma:
print(len(szotar))
print(type(szotar)) # <class 'dict'>

# Függvények:
print(szotar.keys()) # Kulcsok
print(szotar.values()) # értékek
print(szotar.items())  # kulcs-érték párokat (két elemú tuple)

# Szótár bejárása:
for key in szotar.keys():
    print(f"{key} -> {szotar[key]}")

for value in szotar.values():
    # Érték alapján nem tudjuk meghatározni a kulcsot
    print(f"{value}")

for item in szotar.items():
    print(item[0], "->", item[1]) # ('alma', 'apple')

x, y = (50, 30)
print("x =",x)
print("y =",y)

for key, value in szotar.items():
    print(key,"->",value)