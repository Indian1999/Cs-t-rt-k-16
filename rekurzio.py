# Egy függvényt rekurzív függvénynek nevezünk, ha az meghívja önmagát.
# Rekurzió lényege: Van egy bonyolult feladatunk és azt egy picit kevésbé bonyolult
# részfeladattá alakítjuk, egészen addig amíg meg nem tudjuk oldani.

def say_hi_n_times(n):
    if n < 1:
        return
    print("Szia!")
    if n > 1:
        say_hi_n_times(n - 1)

say_hi_n_times(2)

# n! = n * (n-1)!       (n >= 1 természetes szám)
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1
# 0! = 1

def fakt(n):
    if n == 1 or n == 0:
        return 1
    return n * fakt(n-1)

print(fakt(5))

# Rekurzív sorozatok:
# a(n) = 7 + a(n-1)
# a(1) = 3
# a(n) -> 3, 10, 17, 24, 31, 38, ...

def a(n):
    if n == 1:
        return 3
    return 7 + a(n-1)

print(a(5))

# b(n) = 1.2 * b(n-1) - 3
# b(1) = 1

def b(n):
    if n == 1:
        return 1
    return 1.2 * b(n-1) - 3

for i in range(1, 11):
    print(f"b({i}) = {b(i)}")

# c(n) = 0.5 * c(n-1) + 0.25 * c(n-2)
# c(1) = 0
# c(2) = 1
# 0, 1, 0.5, 0.5, ...

def c(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return 0.5 * c(n-1) + 0.25 * c(n-2)


for i in range(1, 11):
    print(f"c({i}) = {c(i)}")

# d(n) = 8 + 2 * d(n-1)
# d(1) = -3

def d(n):
    if n == 1:
        return -3
    return 8 + 2*d(n-1)

print([d(i) for i in range(1, 11)])

# e(n) = e(n-1) * e(n-1) = e(n-1)^2
# e(1) = 2
# 2, 4, 16, 256, ...
def e(n):
    if n == 1:
        return 2
    return e(n-1)**2

print(e(10))

# fib(n) = fib(n-1) + fib(n-2)
# fib(1) = fib(2) = 1
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

from functools import cache

@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

i = 1
while True:
    print(f"fib({i}) digit count = {len(str(fib(i)))}")
    i += 1
    if i > 20000:
        break

