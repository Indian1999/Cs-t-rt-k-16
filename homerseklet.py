

file = open("homerseklet.txt", "r", encoding = "utf-8")

homerseklet = []
for line in file:
    line = line.strip() # ELejéről és végéről leszedi a whitespace karaktereket
    line = line.split(";") # ['18', '13', '3', '33', '2', '27', '-4']
    het_adatai = [int(item) for item in line]
    homerseklet.append(het_adatai)

file.close()

# 1. feladat: Hanyadik nap volt a leghidegebb az évben?
min_sor = 0
min_oszlop = 0
for i in range(len(homerseklet)):
    for j in range(len(homerseklet[i])):
        if homerseklet[i][j] < homerseklet[min_sor][min_oszlop]:
            min_sor = i
            min_oszlop = j
leghidegebb_nap = 7 * min_sor + min_oszlop + 1
print(f"Az év leghidegebb napja a {leghidegebb_nap}. nap volt, {homerseklet[min_sor][min_oszlop]} °C volt aznap.")


# 2. feladat: Írjuk ki, hogy melyik héten mennyi volt az átlag, max, min hőmérséklet
for i in range(len(homerseklet)):
    print(f"{i+1}. hét adatai:")
    print(f"\tÁtlag hőmérséklet: {round(sum(homerseklet[i]) / len(homerseklet[i]), 1)} °C")
    print(f"\tLegmagasabb hőmérséklet: {max(homerseklet[i])} °C")
    print(f"\tLegalacsonyabb hőmérséklet: {min(homerseklet[i])} °C")

# 3. feladat: Írjuk ki, hogy milyen napokon mennyi volt az átlag, max, min hőmérséklet
# pl.: 
# Hétfői napok:
#       Átlag: 19.0
#       Min: 18
#       Max: 35

for j in range(len(homerseklet[0])):
    for i in range(len(homerseklet)):
        pass
