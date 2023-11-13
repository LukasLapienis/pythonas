# petriuko pazymiai
#ivedamas pazymiu kiekis ir suvedami pazymiai. rasti vidurki

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

    # if not(1<=paz<=10):
    #     (print(f'Pazymis {paz} neteisingas, iveskite dar karta: '))
    #     continue
    # p.append(paz)


print(f'petriuko pazymiai {p}')

suma = 0
for i in p:
    suma += i
vidurkis = suma/len(p)
print(f'Petriuko vidrukis {vidurkis}')