#Petriuko pazymiai. Ivedamas pazymiu kiekis, poto ivedami pazymiai. Surasti didziausia. NENAUDOTI MASYVO(Saraso)
def ivedimas(kelintas):
    p = int(input(f'Iveskite Petriuko {kelintas}-aji pazymi...'))
    geras = 1<=p<=10
    if not(geras) :
            print('Pazymys blogas. Kartokite ivedima')
            return ivedimas(kelintas)
    else:
         return p
           
kiek = int(input('Kiek Petriukas turi pazymiu...'))
for i in range(1, kiek+1):
    paz = ivedimas(i)
    if i == 1:
         did = paz
         kelintasDid = i
    elif paz > did:
        did = paz
        kelintasDid = i
print(f'Petriuko didziausias pazymys {did}. Jo vieta {kelintasDid}')
 