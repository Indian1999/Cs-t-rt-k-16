# tuple letrehozasa
import random
ures_tuple = ()
tuple1 = (1, 2, 3, 4)
tuple2 = (1, "valami", True, [1, 2, 3], tuple1)
print(ures_tuple)
print(tuple1)
print(tuple2)
print(tuple2[3])
tuple2[3][2] = "pisti"
print(tuple2)

tuple3 = (3,)
print(tuple3)
print(type(tuple3))

tuple4 = 1,2,2,2,2
print(tuple4)
print(type(tuple4))

tuple5 = tuple([23,123,4432,53])
print(tuple5)

lista = [1,2,3,4,5,6,7,8,9,0]
tuple6 = 1,2,3,4,5,6,7,8,9,0
print(lista[6])
print(tuple6[6])
print(lista[:6], tuple6[:6])
print(lista[-3:-1], tuple6[-3:-1])
print(lista[4:], tuple6[4:])
print(len(lista), len(tuple6))


#random tuple 1-100-ig 20 elemű

lista = [random.randint(1,100) for i in range(20)]
print(lista)

random_tuple = tuple(random.randint(1,100) for i in range(20))
print(random_tuple)

paros = []
paratlan = []
#print(tuple(paros.append(i) for i in random_tuple if i % 2 == 0 else paratlan.append(i)))
for i in random_tuple:
    if i % 2 == 0:
        paros.append(i)
    else:
        paratlan.append(i)
print(paros)
print(paratlan)


tuple7 = tuple(random.randint(1,100) for i in range(5))
tuple8 = tuple(random.randint(1,100) for i in range(5))
print(tuple7, tuple8)
print(tuple7 + tuple8)
print(tuple(i * 3 for i in tuple7 ))


tuple10 = (1,2,3,4,5,6,7,8,9,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,4,2,5,7,6,43,6)
print(tuple10.index(4))
print(tuple10.count(4))

tup1 = 5,6,7
a, b, c = tup1

print(b*a+c)

print(tup1)
lista_tup = list(tup1)
lista_tup[0] = 4
tup1 = tuple(lista_tup)
print(tup1)
tup1 = tup1[:1]+(5,)+tup1[1:]
print(tup1)
tup1 = tup1+(8,)
print(tup1)
lista_tup = list(tup1)
lista_tup.pop(0)
tup1 = tuple(lista_tup)
print(tup1)

if 5 in tup1:
    print("van benne 5")
else:
    print("nincs benne 5")

tupleok = ((1,2,3),(4,5),(12,24,36),(5,9,1))
atlagok = []
for i in tupleok:
    atlagok.append(sum(i) / len(i))
print(atlagok)









