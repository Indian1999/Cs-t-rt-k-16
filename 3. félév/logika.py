x = 13
y = 4

print(x > y and y < x) # True
print(x > y and y > x) # False
print(x > y or  y > x) # True
print(x > y and not y > x)   # True


# and előbb hajtódik végre mint az or
# de a tagadás mindig az első
# A zárójel mindent visz
print( True and False or True and True) # False or True -> True

print(False or True and False)  # False or False -> False
print(False or True and not False)  # False or True and True
# False or True -> True

print(False or True and False) # False
print((False or True) and True) # True


# Feladat:
# Adott az A halmaz, amely 7-tel osztható 3 jegyű számokat tartalmazza.
# B halmaz: 13-mal osztható számok, melyek számjegyeinek összege: 12, 1000-től kisebb
# Alakítsuk ki a C halmazt, amely az A és B halmazok metszete.

def szamjegy_osszeg(num):
    if num == 0:
        return 0
    return num % 10 + szamjegy_osszeg(num // 10)

A = []
B = []
C = []

for i in range(1, 1000):
    if i % 7 == 0 and i >= 100 and i <= 999:
        A.append(i)
    if i % 13 == 0 and szamjegy_osszeg(i) == 12:
        B.append(i)
    if i % 7 == 0 and i >= 100 and i <= 999 and i % 13 == 0 and szamjegy_osszeg(i) == 12:
        C.append(i)

print(A)
print(B)
print(C) # [273]

# Feladat: Írjunk egy függvényt ami megkap egy egész számot, és visszadja a 2-es számrendszerbeli alakját stringként
# pl.: 38   -> 100110

def dec_to_bin(num):
    output = ""
    while num != 0:
        output += str(num % 2)
        num //= 2
    return output[::-1]

print(dec_to_bin(42))
print(dec_to_bin(4096))

# Feladat: Írjunk egy függvényt, ami megkap egy egész számot és visszaadja stringként a 'n' számrendszerbeli
# alakját.
# dec_to_base_n(42, 8) -> "52"

def num_to_letter(num):
    letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[num]

def dec_to_base_n(num, base):
    if base < 2 or base > 36:
        raise ValueError("The base has to be between 2 and 36.")
    output = ""
    while num != 0:
        output += num_to_letter(num % base)
        num //= base
    return output[::-1]

print(dec_to_base_n(42, 8))
print(dec_to_base_n(42, 16))
print(dec_to_base_n(42, 2))
print(dec_to_base_n(42, 36))
print(dec_to_base_n(42, 2))

# Írjunk egy függvényt ami 2-es (stringként kapjuk meg)-ből vált 10-esbe

def bin_to_dec(binary):
    bin_reversed = binary[::-1]
    összeg = 0
    for i in range(len(bin_reversed)):
        összeg += int(bin_reversed[i]) * 2**i
    return összeg

print(bin_to_dec("101010")) # 42
print(bin_to_dec("11010101110101")) # 13685


# Írjunk egy függvényt ami n alapú számrendszerből (stringként) vált 10-esebe
# base_n_to_dec("2A", 16) -> 42

def letter_to_num(letter):
    letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters.find(letter)
    

def base_n_to_dec(num, base):
    num_reversed = num[::-1]
    összeg = 0
    for i in range(len(num_reversed)):
        összeg += letter_to_num(num_reversed[i]) * base**i
    return összeg

print(base_n_to_dec("57", 8))
print(base_n_to_dec("1001011", 2))
print(base_n_to_dec("12AF", 16))


# Írjunk egy függvényt, ami n alapból átvált m alapba egy számot! (stringként kezeljük a számot végig)

def base_n_to_base_m(num, base_n, base_m):
    tizes = base_n_to_dec(num, base_n)
    m_es = dec_to_base_n(tizes, base_m)
    return m_es

print(base_n_to_base_m("10101010101010111110111", 2, 16)) # 5555F7
print(base_n_to_base_m("111111000010", 2, 16)) # FC2
print(base_n_to_base_m("ACDC", 16, 2)) # 1010110011011100


