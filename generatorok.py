import random
from rekurzio import fib

def func(x):
    for i in range(10):
        if i == x:
            return  # return kilép függvényből
    print("A függvény vége")

func(5) # Nem ír ki semmit
func(50) # Függvény vége

# Felsoroló függvények: (yield)

def négyzet_számok():
    i = 1
    while True:
        yield i*i # visszaadja i négyzetét, de nem állítja le a függvényt
        i += 1

for num in négyzet_számok():
    print(num, end = " ")
    if num > 99:
        break
print()

for i in range(5):
    print(i, end = " ")
print()

def myRange(upperBound):
    i = 0
    while i < upperBound:
        yield i
        i += 1

for i in myRange(10):
    print(i, end=" ")
print()

# Írjunk egy generátor-függvényt ami visszaadja a fibonacci számokat

def fib_generator(from_index, to_index):
    for i in range(from_index, to_index):
        yield fib(i)

for num in fib_generator(5, 13):
    print(num, end=" ")
print()

print(fib_generator(3,7)) # <generator object fib_generator at 0x0000024769E0E880>
print(range(20)) # range(0, 20)

# Írjunk egy generátor függvényt ami visszadobálgatja egy listából a páros számokat

def yield_evens(lista):
    for item in lista:
        if item % 2 == 0:
            yield item

for num in yield_evens([5,43,75,76,56,54,75,23,2,0,1,32,321,2,45]):
    print(num, end=" ")
print()

# 1. feladat: Írjunk egy generátort ami az
# a(n) = a(n-1) + 5
# a(1) = 2
# sorozat elemeit sorolja fel
# Ha a generátor függvény paraméterbe x-et írok, akkor az első x elemet sorolja fel
def a(n):
    value = 2
    for i in range(1, n+1):
        yield value
        value += 5

print([item for item in a(10)])

# 2. feladat: Írjunk egy generátort ami megkap egy stringet, és felsorolja a stringben
# található magánhangzókat
def yield_vowels(string):
    vowels = "óüöűúőoieáéaí"
    for char in string:
        if char in vowels or char in vowels.upper():
            yield char

print([char for char in yield_vowels("A kiscica felmászott a fára.")])

# 3. feladat: Írjunk egy prímszámokat felsoroló generátort, a függvény 
# egy n természetes számot kap paraméterül, és felsorolja az első n db prímszámot

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    counter = 0
    num = 2
    while counter < n:
        if is_prime(num):
            yield num
            counter += 1
        num += 1

print([num for num in prime_generator(20)])

# Készítsünk egy függvényt ami egy bármilyen szűrőt alkalmaz egy listán

def divisible_by_5(num):
    return num % 5 == 0

def filter_list(lista, func):
    for item in lista:
        if func(item):
            yield item

lista = [random.randint(-20, 100) for i in range(30)]
primes = [item for item in filter_list(lista, is_prime)]
divs_by_5 = [item for item in filter_list(lista, divisible_by_5)]
negs = [item for item in filter_list(lista, lambda x: x < 0)]
single_digits = [item for item in filter_list(lista, lambda x: x < 10 and x > -10)]

print(lista)
print(primes)
print(divs_by_5)
print(negs)
print(single_digits)

