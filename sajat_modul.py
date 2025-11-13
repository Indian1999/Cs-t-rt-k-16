import LogiLib # Lefuttatja a LogiLib mappában lévő __init__.py-t
from LogiLib import constants # (Ez akkor is működik, ha az init.py-ban nincs import)
from LogiLib.constants import nevek
from LogiLib.funcs import fib

print(LogiLib.constants.golden_ratio)
print(constants.pi)
print(nevek)

print(LogiLib.funcs.factorial(8))

print(fib(11))
