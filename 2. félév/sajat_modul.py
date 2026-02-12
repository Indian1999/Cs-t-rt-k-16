import LogiLib # Lefuttatja a LogiLib mappában lévő __init__.py-t
from LogiLib import constants # (Ez akkor is működik, ha az init.py-ban nincs import)
from LogiLib.constants import nevek
from LogiLib.funcs import fib
import datetime
import time
import pendulum as p # pip install pendulum

print(datetime.date.today()) # 2025-11-13

today = datetime.date.today()
print(today.weekday()) # 3 (csütörtök)
print(today.day)
print(today.month)
print(today.year)
print(today.strftime("Év: %Y, Hónap: %m, nap: %d\n%H:%M:%S"))

this_moment = datetime.datetime.now()
print(this_moment.strftime("Év: %Y, Hónap: %m, nap: %d\n%H:%M:%S"))

print(time.time()) # 1763051472.362606
print(time.strftime("%Y-%m-%d %H:%M:%S"))

city = "Australia/Sydney"
city_now = p.now(city)
print(city_now.to_datetime_string())

duriation = p.duration(seconds=time.time())
print(duriation.in_days())

