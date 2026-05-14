#Hány kettőskeresztet ír ki a program?
for i in range(12, 19, 2):
    print("#")

#4-et

#Hány kettőskeresztet ír ki a program?
for i in range(5, 18, 3): 
    print("#"*(i%2))

#3-at

#Hány kettőskeresztet ír ki a program?
for i in range(5): 
    print("#"*i)
else:
    print("#")

# 11-et

#Hány kettőskeresztet ír ki a program?
for i in range(20, 15):
    print("#")
else:
    print("#"*4)

# 4-et

# Mit ír ki a program?
def f(x):
    return x**2

print(f(3) + f(f(2))) # 25

print(f(3) + f(4) == f(5)) # True

def a():
    num = 10
    while True:
        num += 3
        yield num
        if num > 25:
            break

print([i for i in a()])  # [13, 16, 19, 22, 25, 28]

def b(from_num, to_num):
    while from_num < to_num:
        yield from_num**2
        from_num += 1

print([i for i in b(2, 11)]) # [4, 9, 16, 25, 36, 49, 64, 81, 100]

def c(text):
    for ch in text.lower():
        yield ch

print([i for i in c("AlmaFa")]) # ['a', 'l', 'm', 'a', 'f', 'a']

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_finder():
    n = 1
    while True:
        yield (n, fib(n))
        n += 1

import random
def random_point():
    return random.randint(-10, 10), random.randint(-10, 10)

print(random_point())

point = random_point()
print(point)
print(type(point))

x, y = random_point()
print(x)
print(y)
print(type(x)) # <class 'int'>

szamok = (6, 3, 7)
a, b, c = szamok
print(a)

a, *b, c = [1,2,3,4,5]
print(b) # [2, 3, 4]


def create_list(*args, ordered = False, reverse = False, duplicates = True):
    lista = [item for item in args] 
    if not duplicates:
        lista = list(set(lista))
    if ordered:
        lista.sort(reverse=reverse)
    return lista

print(create_list(1,93,8,5,11,5))
# [1, 93, 8, 5, 11, 5]
print(create_list(1,93,8,5,11,5, ordered = True))
# [1, 5, 5, 8, 11, 93]
print(create_list(1,93,8,5,11,5, ordered = True, reverse = True))
# [93, 11, 8, 5, 5, 1]
print(create_list(1,93,8,5,11,5, ordered = True, reverse = True, duplicates=False))
# [1, 5, 8, 11, 93]


# Készíts egy generátor függvényt, amely két paramétert vár.
# a-tól b-ig
# a generátor visszaadogtja a. fibonacci számtól a b-ik fibonacci számig az értékek
# (b. nincs benne)

def fib_gen(a, b):
    for i in range(a, b):
        yield fib(i)

print([item for item in fib_gen(5, 10)])

# Készíts egy generátor függvényt, aminek 3 paramétere van.
# a-tól b-ig,
# 3. paraméter egy függvényt, amit alkalmazunk számokra- a és b között
# a függvény ezeket az a eredményeket adogassa vissza

def apply_func(a, b, func):
    for i in range(a, b):
        yield func(i)

# pl.: apply_func(1, 6, square)   -> 1, 4, 9, 16, 25

print([item for item in apply_func(2, 10, fib)])
print([item for item in apply_func(2, 10, lambda x: x**3)])


