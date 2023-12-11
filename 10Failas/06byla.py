# w, r, a, w+, a+ 
# w+ rewrite everytime, r+ read + append (r+ negali sukurti failo)
# byloje norime irasyti 3 skaicius, nuskaityti ir susumuoti ir pabaigoje irasyti

def viskas(txt):
    with open('10Failas/06data.txt', 'r+') as file:
        file.write('5\n')
        file.write('15\n')
        file.write('20\n')
        file.seek(0)
        sk1 = int(file.readline())
        sk2 = int(file.readline())
        sk3 = int(file.readline())
        suma = sk1 + sk2 + sk3
        file.write(txt + '\n')
        file.write(f'{sk1} + {sk2} + {sk3} = {suma}\n')

for i in range(1, 6):
    viskas(f'rezultatas Nr.{i}')