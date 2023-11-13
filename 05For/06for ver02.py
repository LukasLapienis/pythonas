#Petriuko pazymiai. Ivedamas pazymiu kiekis, poto ivedami pazymiai. Apskaiciuoti vidurki. NENAUDOTI MASYVO(Saraso)
def ivedimas(kelintas):
    p = int(input(f'Iveskite Petriuko {kelintas}-aji pazymi...'))
    geras = 1<=p<=10
    if not(geras) :
            print('Pazymys blogas. Kartokite ivedima')
            return ivedimas(kelintas)
    else:
         return p
           


kiek = int(input('Kiek Petriukas turi pazymiu...'))
suma = 0
for i in range(1, kiek+1):
    paz = ivedimas(i)
    suma = suma + paz
vid = suma / kiek
print(f'Petriuko vidurkis {vid}')
 