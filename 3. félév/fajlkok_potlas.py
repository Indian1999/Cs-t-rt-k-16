import os

path = os.path.join(os.path.dirname(__file__), "forras", "adatok.txt")

f = open(path, "r", encoding="utf-8")

print(f.read())

f.close()

with open(path, "a", encoding="utf-8") as f:
    f.write("context manager\n")

path = os.path.join(os.path.dirname(__file__), "forras", "adatok3.txt")

with open(path, "w", encoding= "utf-8") as f:
    f.write("Ez törtli a fájl addigi tartalmát\n")
    f.write("és szépen fel lehet tölteni\n")
    f.write("valami újjal.\n")
