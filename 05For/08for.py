# ivedame skaiciu 12:
#   1.  atspausdina visus daliklius 1, 2, 3, 4, 6
#   1.1 kiek tu dalikliu yra
#   2. Apskaiciuoja dalikliu suma
sk = int(input('sk=... '))
kiek = suma = 0
for i in range(1, sk):
    if sk % i == 0:
        print(i,end=(', '))
        suma += i
        kiek += 1
print(f' Ju yra {kiek}')
print(f'Dalikliu suma = {suma}')
