#Petriuko pazymiai. Ivedamas pazymiu kiekis, poto ivedami pazymiai. Apskaiciuoti vidurki. NENAUDOTI MASYVO(Saraso)
from itertools import count
kiek = int(input('Kiek Petriukas turi pazymiu...'))
suma = 0

for i in range(1, kiek+1):
    p = int(input(f'Iveskite Petriuko {i}-aji pazymi...'))
    geras = 1<=p<=10
    if not(geras) :
        for j in count(0):
            print('Pazymys blogas. Kartokite ivedima')
            p = int(input(f'Iveskite Petriuko {i}-aji pazymi...'))
            if 1<=p<=10:
                break
    suma = suma + p
vid = suma / kiek
print(f'Petriuko vidurkis {vid}')
 