def valom():
    with open('10Failas/07data.txt', 'w') as f:
        pass
    
def ivedimas(txt):
    sk = int(input(f'{txt} = '))
    return sk

def irasymas(txt):
    with open('10Failas/07data.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

valom()

kiek = ivedimas('kiek skaiciu sumuosim?')
irasymas(f'Vartotojas ivede kad sumuosim {kiek} skaicius')

sum = 0
list1 = []
for i in range(kiek):
    sk = ivedimas(f'sk{i+1}')
    irasymas(f'sk{i+1} = {sk}')
    sum += sk
    list1.append(sk)

print(f'Suma = {sum}')
irasymas(f'Suma = {sum}')