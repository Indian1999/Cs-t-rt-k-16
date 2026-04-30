import os

path = os.path.join(os.path.dirname(__file__), "forras", "morze_bemenet.txt")

with open(path, "r", encoding="utf-8") as f:
    adat = f.read()

# Az adat feldolgozása
# 1. lépés, legyen minden betű kisbetűs
adat = adat.lower()
for char in ",.'();":
    adat = adat.replace(char, "")

morze_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

morze = ""
for char in adat:
    if char in morze_dict:
        morze += morze_dict[char]
    elif char == " ":
        morze +=  "_"
    else:
        morze += char

path_output = os.path.join(os.path.dirname(__file__), "forras", "morze_kimenet.txt")
f = open(path_output, "w", encoding="utf-8")
f.write(morze)

f.close()

path = os.path.join(os.path.dirname(__file__), "forras", "adatok.txt")
with open(path, "a", encoding="utf-8") as f:
    f.write("Ide írok még valamit\n")

path = os.path.join(os.path.dirname(__file__), "forras", "adatok2.txt")
with open(path, "w+", encoding="utf-8") as f:
    f.write("Szia! Hogy vagy?")
    f.seek(0) # Olvasó fej a fájl elejére
    print(f.read())

with open(path, "r+", encoding="utf-8") as f:
    f.write("r+ mód\n")
    f.seek(0)
    print(f.read())


with open(path, "a+", encoding="utf-8") as f:
    f.write("a+ mód\n")
    f.seek(0)
    print(f.read())

# r: Csak olvasás; Olvasófej az elejéről; nem törli a fájl tartalmát
# w: Csak írás;    Olvasófej az elejéről; törli a fájl tartalmát
# a: Csak írás;    Olvasófej a végéről;   nem törli a fájl tarlamát

# +: írás és olvasás
# r+: Írás és Olvasás; Olvasófej az elejéről; nem törli a fájl tartalmát
# w+: Írás és Olvasás; Olvasófej az elejéről; törli a fájl tartalmát
# a+: Írás és Olvasás; Olvasófej a végéről;   nem törli a fájl tartalmát


# Kép beolvasása
import cv2 as cv # pip install cv

path = os.path.join(os.path.dirname(__file__), "file_modes.png")
out_path = os.path.join(os.path.dirname(__file__), "forras", "img_modified.png")

image = cv.imread("lista_tomb_memoria.png")
#image = cv.resize(image, (1000, 1300))
image = cv.rotate(image, 90)

cv.imwrite("mod.png", image)


