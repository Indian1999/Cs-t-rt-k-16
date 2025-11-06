

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

napok_nevei = ["Hétfői", "Keddi", "Szerdai", "Csütörtöki", "Pénteki", "Szombati", "Vasárnapi"]
for j in range(len(homerseklet[0])):
    összeg = 0
    min_index = 0
    max_index = 0
    for i in range(len(homerseklet)):
        összeg += homerseklet[i][j]
        if homerseklet[i][j] < homerseklet[min_index][j]:
            min_index = i
        if homerseklet[i][j] > homerseklet[max_index][j]:
            max_index = i
    print(f"{napok_nevei[j]} napok adatai:")
    print(f"\tÁtlag hőmérséklet: {round(összeg/len(homerseklet), 1)} °C")
    print(f"\tLegmagasabb hőmérséklet: {homerseklet[max_index][j]} °C")
    print(f"\tLegalacsonyabb hőmérséklet: {homerseklet[min_index][j]} °C")

# 4. feladat: Melyik volt a legátlagosabb hét?
# (az a hét ami átlag hőmérséklete a legközelebb van az éves heti átlag hőmérséklettől)
from math import fabs

heti_atlagok = []
for i in range(len(homerseklet)):
    heti_atlagok.append(sum(homerseklet[i]) / len(homerseklet[i]))

total_atlag = sum(heti_atlagok) / len(heti_atlagok)
        
print(f"Az évi heti szintű átlag hőmérséklet: {total_atlag} °C")
atlag_index = 0
min_különbség = fabs(heti_atlagok[0] - total_atlag)
for i in range(1, len(heti_atlagok)):
    különbség = fabs(heti_atlagok[i] - total_atlag)
    if különbség < min_különbség:
        min_különbség = különbség
        atlag_index = i

print(f"A(z) {atlag_index + 1}. hét volt a legátlagosabb. A heti átlag {heti_atlagok[atlag_index]} °C volt.")

