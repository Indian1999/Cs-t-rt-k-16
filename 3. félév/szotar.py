import os
import random
# A dictionary (szótár) adatszerkezet
"""
szotar = {} # Egy üres dictionaryt hoz létre
szotar = {
    "alma": "apple",
    "banán": "banana",
    "citrom": "lemon",
    "dinnye": "melon",
    "elefánt": "elephant",
    "flakon": "bottle",
    "3": "three",
    3: "three",
    "citrom": "citrus" # felülírja a "citrom" kulcshoz tartozó előző értéket
}
# kulcs - érték párokat tárol
# kulcs alapján azonosítjuk az értékeket.
# a kulcsok egyedi értékek kell hogy legyenek (egy kulcs nem szereplhet többször)
# az értékekre nincs ilyen megkötés

print(szotar)
print(type(szotar)) # <class 'dict'>
print(len(szotar))  # 8
print(szotar[3])
print(szotar["citrom"])

# Egy érték átírása:
szotar["dinnye"] = "watermelon"
print(szotar)

# Új érték hozzáadása:
szotar["narancs"] = "orange"
print(szotar)

# Elem törlése:
del szotar["flakon"]
print(szotar)
"""
###############################
#    DICTIONARY-K BEJÁRÁSA    #
###############################

def opcio1(dict):
    """A dictionary kulcsain iterálunk végig"""
    for key in dict.keys():
        print(f"{key} -> {dict[key]}")

def opcio2(dict):
    """A dictionary értékein iterálunk végig"""
    # Mivel az értékek nem egyediek, ezért értékből nem tudunk kulcsot kapni
    for value in dict.values():
        print(value)

def opcio3(dict):
    """A kulcs-érték párokon megyünk végig"""
    for item in dict.items(): # item = ('alma', 'apple') (tuple)
        print(f"{item[0]} -> {item[1]}")

    for key, value in dict.items(): # key = 'alma', value = 'apple'
        print(f"{key} -> {value}")
"""
#opcio1(szotar)
#opcio2(szotar)
opcio3(szotar)

if "só" in szotar.keys():
    print("Szerepel a só a szótárban")
else:
    print("Nem szerepel a só a szótárban")

if "citrom" in szotar.keys():
    print("Szerepel a citrom a szótárban")
else:
    print("Nem szerepel a citrom a szótárban")

"""

# Feladat: Adott egy txt állomány, olvassuk be és számoljuk meg, hogy melyik hányszor szerepel

