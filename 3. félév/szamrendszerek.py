# 2-es számrendszerbe váltás
binaris = bin(923)

print(binaris)           # 0b1110011011
print(type(binaris))     # <class 'str'>

# 16-os számrendszerbe váltás
hexa = hex(923)

print(hexa)              # 0x39b
print(type(hexa))        # <class 'str'>

# 8-as számrendszerbe váltás
okta = oct(923)

print(okta)              # 0o1633
print(type(okta))        # <class 'str'>

a = int("923")

print(a) #923

a = int("11100110011")
print(a) # 11100110011  (10-es számrendserzbe)

a = int("11100110011", 2)
print(a) # 1843   (10-es számrendszerbe)

a = int("F3CC21", 16)
print(a) # 15977505



a = 52     # 110100
b = 39     # 100111

print(a & b) # 0b100100 = 36
print(a | b) # 0b110111 = 55       (alt gr + W)
print(a ^ b) # 0b010011 = 19       (alt gr + 3)
print(~b)    # szám + 1 negálva    (alt gr + 1) -40
print(b >> 1)# maradék nélkül oszt 2-vel  # 19
print(a << 3)# szoroz 2 vel 3 alkalommal (416 = 52 * 8)

# cmd: ipconfig
# IPv4 Address. . . . . . . . . . . : 192.168.1.105
# Subnet Mask . . . . . . . . . . . : 255.255.255.0

ip = [192, 168, 1, 105]
mask = [255, 255, 192, 0]

print("Az eszközöd IP-címe:", ".".join([str(i) for i in ip]))
print("A hálózati maszkod:", ".".join([str(i) for i in mask]))

network_ip = [ip[i] & mask[i] for i in range(4)]
print("A hálózat IP-címe:", ".".join([str(i) for i in network_ip]))

# Adott egy színkód "AC3F1B" alakban, alakítsuk át (172, 63, 27)

color_code = "AC3F1B"
color_code_int = int(color_code, 16)
red_filter = int("FF0000", 16)
green_filter = int("00FF00", 16)
blue_filter = int("0000FF", 16)
red = (color_code_int & red_filter) >> 16
green = (color_code_int & green_filter) >> 8
blue = (color_code_int & blue_filter)
dec_code = (red, green, blue)
print(f"{color_code} = {dec_code}")

# Adott egy lista amelyben minden szám, pontosan kétszer szerepel
# Találd meg azt amelyik csak 1-szer szerepel XOR (^) segítségével

lista = [9, 2, 4, 1, 5 ,3, 7, 3, 7, 2, 9, 4, 1, 0, 0, 6, 10, 10, 6]
szam = None
for i in range(len(lista)):
    csak_egy = True
    for j in range(i+1, len(lista)):
        if lista[i] ^ lista[j] == 0:
            csak_egy = False
            break
    if csak_egy:
        szam = lista[i]
        break
print(lista)
print(f"A szám ami csak egyszer szerepel: {szam}")



# Linuxon a chmod parancs használata:
# 1 olvasás, 2 írás, 4 futtatás
# chmod 777 fajl
# chmod 644 fajl

def set_permission(num):
    permissions = []
    if num & 1 == 1:
        permissions.append("olvasás")
    if num & 2 == 2:
        permissions.append("írás")
    if num & 4 == 4:
        permissions.append("futtatás")
    return permissions

for i in range(8):
    print(f"{i}: {set_permission(i)}")

# % operátor nélkül ellenőrizzük, hogy egy szám páros, vagy páratlan

def is_even(num):
    if num & 1:
        print("Páratlan")
    else:
        print("Páros")

is_even(8)
is_even(11)
