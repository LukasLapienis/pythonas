#petriuko pazymiai
#ivedamas pazymiu kiek ir suvedami pazymiai. rasti vidurki
#sukurti sarasa mamai (tik teigiami) 4 ir didesni ir apskaiciuoti vidurki
#sukurti sarasa teciui (tik teigiami) 6 ir didesni ir apskaiciuoti vidurki

MAMA = 4
TATA = 6
#-------------funkcija grazinanti pazymiu kieki--------------
def kiekis(vardas):
    kiek = int(input(f'kiek {vardas} turi pazymiu? '))
    return kiek

#-------------------------------------------------------------------------------------
#---------------------funkcija pazymiams investi ir grazinti--------------------------
def ivedimas(kiek, vardas):
    p = []
    i = 0
    while i < kiek:
        paz = int(input(f'Iveskite {vardas} {i+1}-aji pazymi: '))
        if 1<=paz<=10:
            p.append(paz)
            i += 1
        else: 
            (print(f'Pazymis {paz} neteisingas, iveskite dar karta: '))
    return p
#-------------------------------------------------------------------------------------
#-------------------------funkcija apskaiciuoja ir grazina vidurki--------------------
def vidurkis(p):
    if len(p)>0:
        return (sum(p) / len(p))
    else:
        return 0
#-------------------------------------------------------------------------------------
#-------------------------sarasas tevams----------------------------------------------
def tevams(p, kriterijus):
    pTev = []
    for i in p:
        if i >= kriterijus:
            pTev.append(i)
    return pTev
#-------------------------------------------------------------------------------------
#--------------------------------Duomenu isvedimas------------------------------------
def isvedimas(vardas):
    # paz = ivedimas(kiekis(vardas), vardas)
    # vidMok = vidurkis(paz)
    # pazMama = tevams(paz, MAMA)
    # pazTetis = tevams(paz, TATA)
    # vidMama = vidurkis(pazMama)
    # vidTetis = vidurkis(pazTetis)
    # print(f'{vardas} pazymiai {paz}. Vidurkis {vidMok}')
    # print(f'{vardas} mamos pazymiai {pazMama}. Vidurkis {vidMama}')
    # print(f'{vardas} tecio pazymiai {pazTetis}. Vidurkis {vidTetis}')
    paz = ivedimas(kiekis(vardas), vardas)
    pazMama = tevams(paz, MAMA)
    pazTetis = tevams(paz, TATA)
    print(f'{vardas} pazymiai {paz}. Vidurkis {vidurkis(paz)}')
    print(f'{vardas} mamos pazymiai {pazMama}. Vidurkis {vidurkis(pazMama)}')
    print(f'{vardas} tecio pazymiai {pazTetis}. Vidurkis {vidurkis(pazTetis)}')

#-------------------------------------------------------------------------------------
klase = ['Petras', 'Antanas']
for i in klase:
    isvedimas(i)