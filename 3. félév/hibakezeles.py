try:
    #import seaborn as sns # <class 'ModuleNotFoundError'>
    import os
    #from .player import Player # <class 'ImportError'>
except Exception as ex:
    print("HIBA!")
    print(type(ex))
    print(ex)


try:
    # ValueError: invalid literal for int() with base 10: '9ű'
    a = 2 #int(input("Add meg az osztandót: "))
    b = 3 #int(input("Add meg az osztót: "))
    c = a / b 
    # TypeError: unsupported operand type(s) for /: 'str' and 'str'
    # ZeroDivisionError: division by zero

    print(f"{a} / {b} = {c}")
except ValueError as verro:
    print("Egész számot adj meg!")
except ZeroDivisionError as zderror:
    print("Nullával nem szabad osztani!")
except Exception as ex:
    print(ex)
    print(type(ex))
    print("Ismeretlen hiba!")
finally:
    print("A finally blokk az mindig lefut a végén.")
    print("Akkor is ha volt hiba, akkor is ha nem")



path_forras = os.path.join(os.path.dirname(__file__), "forras")
try:
    with open(os.path.join(path_forras, "adatok.txt")) as f: # FileNotFoundError
        adatok = f.read()
        print(adatok)
except FileNotFoundError:
    print("A megadott fájl nem létezik!")



tiltott = os.path.join("C:\\", "Windows", "System32", "config", "SAM")
print(tiltott)
try:
    with open(tiltott) as f: # PermissionError
        adatok = f.read()
        print(adatok)
except FileNotFoundError:
    print("A megadott fájl nem létezik!")
except PermissionError:
    print("Ehez nincs engedélyed!")


def fakt(n):
    if type(n) != int:
        raise TypeError("A fakt(n) függvény csak egész számokra értelmezett!")
    if n < 0:
        raise ValueError("A fakt(n) függvény csak nemnegatív számokra értelmezett!")
    if n == 0:
        return 1
    return n * fakt(n-1)


try:
    print(fakt(9))
except TypeError as ex:
    print(ex)
except ValueError as ex:
    print(ex)
except RecursionError as ex:
    print(ex)
except Exception as ex:
    print("Ismeretlen hiba!")

# Írjunk egy függvényt, ami kiírja hogy x év óta hány év telt el

def elapsed_years(year):
    if type(year) != int:
        raise TypeError("Az évszámnak egész számnak kell lennie!")
    if year > 2026:
        raise ValueError("Múltbéli évszámot adj meg!")
    return 2026 - year

try:
    print(elapsed_years(1232))
except TypeError:
    print("Típus hiba!")
except ValueError:
    print("Érték hiba!")
except Exception as ex:
    print("Ismeretlen hiba!")

# Feladat: Írjunk egy függvényt, ami meghatározza egy adatszerkezet elemeinek az átlagát.
# Kezeljünk le minden lehetséges hibát

def average(iterable):
    total = 0
    count = 0
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"{type(iterable)} ({iterable}) nem egy iterálható objektum!")
    for item in iterable:
        if type(item) == int or type(item) == float:
            total += item
            count += 1
        else:
            raise TypeError(f"{type(item)} nem átlagolható! Használj 'int' vagy 'float objektumokat!")
    if count == 0:
        raise ZeroDivisionError("Üres adatszerkezet!")
    return total / count
        
# Hívjuk meg a függvényt a lehetséges hibák lekezelésével

try:
    print(average(range(3, 99, 5)))
except ZeroDivisionError as ex:
    print(ex)
except TypeError as ex:
    print(ex)


