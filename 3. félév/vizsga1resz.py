# 1. feladat:
a = int(input("a = "))
b = int(input("b = "))

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ^ 2 = {a**2}")

# 2. feladat:

penz = int(input("Pénz: "))
cimletek = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for cimlet in cimletek:
    print(f"{penz // cimlet} db {cimlet} Ft-os")
    penz %= cimlet

# 3. feladat:
mantissza = float(input("Mantissza: "))
kitevo = int(input("Kitevő: "))

print(f"Tényleges érték: {mantissza * 10**kitevo}")
print(f"Tudományos alak: {mantissza}e{kitevo}")
if mantissza > 0:
    print("Pozitív")
elif mantissza < 0:
    print("Negatív")
else:
    print("Nulla")