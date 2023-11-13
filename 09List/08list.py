#petriuko pazymiai
#ivedamas pazymiu kiek ir suvedami pazymiai. rasti vidurki
#sukurti sarasa mamai (tik teigiami) 4 ir didesni ir apskaiciuoti vidurki
#sukurti sarasa teciui (tik teigiami) 6 ir didesni ir apskaiciuoti vidurki

kiek = int(input('kiek petriukas turi pazymiu? '))
p = []
i = 0

while i < kiek:
    paz = int(input(f'Iveskite {i+1}-aji pazymi: '))
    if 1<=paz<=10:
        p.append(paz)
        i += 1
    else: 
        (print(f'Pazymis {paz} neteisingas, iveskite dar karta: '))

minPaz = int(input('koks maziausias pazymys pagerintui vidurkiui? '))

def pagerinta():
    bandymai = 0
    a = p.pop(bandymai)
    while a => minPaz: 






suma = 0
for i in p:
    suma += i
vidurkis = suma/len(p)
print(f'Petriuko vidrukis {vidurkis}')