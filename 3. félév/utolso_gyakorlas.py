def first_and_last_two(string):
    if len(string) < 2:
        raise ValueError("A stringnek legalább 2 karakter hosszúnak kell lennie!")
    return string[:2] + string[-2:]

def first_and_last_n(string, n = 2):
    if len(string) < n:
        raise ValueError(f"A stringnek legalább n ({n}) karakter hosszúnak kell lennie!")
    return string[:n] + string[-n:]

#print(first_and_last_n("H", 3)) 
print(first_and_last_n("Hello World!", 4)) 
print(first_and_last_n("Hello World!")) 

# Írjunk egy függvényt amely visszaadja az első ismétlődő karaktert egy stringben.
# pl.:     abcddcba -> 4, "d"
# pl.:     abcdefgh -> None, None

def first_repeat(string):
    chars = set() # Üres halmaz (de nyugodtan lehetne egy lista)
    for i in range(len(string)):
        if string[i] in chars:
            return i, string[i]
        else:
            chars.add(string[i])
    return None, None

print(first_repeat("abcddcba"))
print(first_repeat("abcdefgh"))

# Írjunk egy függvényt ami törli a megadott indexen lévő elemet egy tuple-ből!
# A tuple immutable (Nem változtatható)
tup = (2,4,5,5,3,3,4,3,2,4,2)
#del tup[5]  # TypeError: 'tuple' object doesn't support item deletion

def remove_tuple_index(tup, index):
    lista = list(tup)
    del lista[index] 
    #lista.pop(index)   Ezt kikommentelem, mert ne töröljük kétszer
    tup = tuple(lista)
    return tup

print(tup)
tup = remove_tuple_index(tup, 6)
print(tup)


# Írjunk egy függvényt ami rendez egy dictionary-t.

colors = {"red": 1, "green": 6, "blue": 4, "white": 5, "pink": 7, "gray": 5, "black": 2}

def sort_dict(myDict, reverse = False, key = None):
    myDict = dict(sorted(myDict.items(), reverse=reverse, key=key))
    return myDict

print(sort_dict(colors, reverse = True, key = lambda x: x[1]))
print(sort_dict(colors, key = lambda x: x[1]))

lista = [4,2,5,6,6]
print(lista)
print(sorted(lista)) # NEM helyben rendezi, hanem csinál egy újat
print(lista)
lista.sort() # helyben rendezi a listát
print(lista)

# Írjunk egy függvényt ami egy lista minden 3. elemét törli

def del_every_third(lista):
    new_list = []
    for i in range(len(lista)):
        if i % 3 != 2:
            new_list.append(lista[i])
    return new_list

def del_every_nth(lista, n = 2):
    new_list = []
    for i in range(len(lista)):
        if i % n != (n-1):
            new_list.append(lista[i])
    return new_list

lista = [4,5,7,8,23,3,2,11,43,34,64,56,4,23,32,43]
print(lista)
print(del_every_third(lista))
print(del_every_nth(lista, 8))
print(del_every_nth(lista, 1))
print(del_every_nth(lista))

# Anna, Béla, Cecil, Dénes, Elemér moziba mennek, hányféleképpen tudnak leülni egymás mellé?
# Írjuk ki az összes lehetséges elrendezést
# Erre írjunk egy általános függvényt (ism. nélküli permutációs feladat)

def permutations(lista):
    if len(lista) <= 1:
        return [lista[:]]
    result = []
    for i in range(len(lista)):
        item = lista[i]
        others = lista[:i] + lista[i+1:]
        for p in permutations(others):
            result.append([item] + p)
    return result

print(permutations(["Anna", "Béla", "Cecil", "Dénes", "Elemér"]))

# 1. feladat: Írjunk egy függvényt ami egy mátrixot listává alakít
# pl.: [[1,2,3], [4,5,6], [4, 5], [3]] -> [1,2,3,4,5,6,4,5,3]

def matrix_to_list(matrix):
    lista = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            lista.append(matrix[i][j])
    return lista

print(matrix_to_list([[1,2,3], [4,5,6], [4, 5], [3]]))

# 2. feladat: Írjunk egy string titkosító függvényt.
# A páros indexű karakterek kerüljenek az új string elejére, a páratlanok a végére
# pl.: "Hello World!" -> "HloWrdel wl!"

# 3. feladat: Ítrjunk egy olyan függvényt, amely egy ilyen módon kódolt szöveget tud dekódolni!

def encode(text):
    return text[::2] + text[1::2]

print(encode("Egy almafa"))
print(encode("A programozás órákon programozunk."))

def decode(text):
    halfway = len(text) // 2
    output = ""
    for i in range(halfway):
        output += text[i]
        output += text[halfway+i]
    return output

print(decode("Eyamfg laa"))
print(decode("Apormzsóáo rgaouk rgaoá rknpormzn."))