import os
path_adatok = os.path.join(os.path.dirname(__file__), "minecraft-adatok.txt")
szerverek = []
with open(path_adatok, encoding="UTF-8") as f:
    mezonevek = f.readline().strip().split(";")
    for line in f:
        line = line.strip().split(";")
        szerver = {
            mezonevek[0]: line[0],
            mezonevek[1]: line[1],
            mezonevek[2]: int(line[2]),
            mezonevek[3]: int(line[3])
        }
        szerverek.append(szerver)
print(szerverek)

print(len(szerverek))

maxi = 0
for i  in range(1, len(szerverek)):
    if szerverek[maxi]["jatekosok"] < szerverek[i]["jatekosok"]:
        maxi = i
print(szerverek[maxi]["nev"], szerverek[maxi]["jatekosok"])

def vip_ar(ar):
    return ar * 1.5

s = input()
for i in szerverek:
    if i["nev"] == s:
        print(int(vip_ar(i["havi_dij"])))
        break
else: #nincs break
    print("Nincs ilyen szerver")

path_export = os.path.join(os.path.dirname(__file__), "minecraft-export.txt")
with open(path_export, "w", encoding="UTF-8") as f:
    for i in szerverek:
        if i["mod"] == "survival":
            f.write(i["nev"] + "\n")