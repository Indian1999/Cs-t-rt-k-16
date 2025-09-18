a = 42
b = 13

print(a + b)

print("Hello World!")

print(max([4,2,1,4,6,7,4,3,5]))

def say_hi():
    print("Szia!")
    
say_hi()

def say_hi_to(name): # name - függvény Paraméter
    print(f"Szia {name}!")
    
say_hi_to("András") # András - argumentum
say_hi_to("Béla")
say_hi_to("Cecil")

def f(x): # f(x) = 3x - 2
    print(f"f({x}) = {3*x - 2}")
    
f(0)
f(1)
f(2)

def say_time_hi_to(time, name):
    if time == 1:
        print(f"Jó reggelt {name}!")
    elif time == 2:
        print(f"Jó napot {name}!")
    elif time == 3:
        print(f"Jó estét {name}!")
    else:
        print(f"Szia {name}!")
        
say_time_hi_to(1, "András")
say_time_hi_to(2, "Béla")
say_time_hi_to(3, "Cecil")
say_time_hi_to([8, 5, 3], "Dénes")


print(say_hi()) # None

def g(x):
    return 2 * x + 4

i = -20
while g(i) < 0:
    i += 1
print(f"Az első egész szám amire a g függvény nem negatív értéket ad a {i}.")
   
# Ha egy függvény return-höz ér akkor ott leáll teljesen
def get_animal():
    print("Ez a get_animal() függvény eleje")
    return "Elephant"
    print("Ez a get_animal() függvény vége") # <- Ez sose fut le
    
get_animal()

# Írjunk egy függvényt ami meghatározza egy szám abszolút értékét! ( |-5| = 5,    |3| = 3 )

def abs(x):
    if x < 0:
        return x * -1
    return x

print(abs(-7))
print(abs(-7.16))
print(abs(10))