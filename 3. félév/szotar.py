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

path = os.path.join(os.path.dirname(__file__), "forras", "story.txt")

with open(path, encoding="utf-8") as f:
    text = f.read()
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace('"', "")
    text = text.replace("'re", " are")
    text = text.replace("'ve", " have")
    text = text.replace("'s", "")
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    text = text.lower()
    text = text.split(" ")

word_counter = {}
for word in text:
    if word not in word_counter.keys():
        word_counter[word] = 1
    else:
        word_counter[word] += 1

word_counter = list(word_counter.items()) # [('the', 143), ('morning', 3), ('sun', 1)]
# x, a word_counter egy eleme, azaz pl.: x = ('the', 143)
word_counter.sort(key=lambda x: x[1], reverse=True)
word_counter = dict(word_counter)
i = 0
for key, value in word_counter.items():
    i += 1
    print(f"{key} -> {value}")
    if i >= 15:
        break

################################
#      PLAYERS FELADAT         #
################################

players = []
for i in range(10):
    players.append(
        {
            "level": random.randint(1, 80),
            "class": random.choice(["Warrior", "Mage", "Priest", "Paladin"]),
            "gold": random.randint(100, 24000),
            "kill_count": random.randint(0, 200)
        }
    )

# Írd ki a leggazdagabb játékos adatait!
max_index = 0
for i in range(1, len(players)):
    if players[i]["gold"] > players[max_index]["gold"]:
        max_index = i

print(players[max_index])

# Írd ki a játékosok átlagos killcountját:

total = 0
for player in players:
    total += player["kill_count"]
print(f"A játékosok átlagoss kill count-ja:", round(total/len(players) ,1))