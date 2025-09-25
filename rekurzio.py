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

