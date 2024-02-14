prekes = {
    'Duona': 1.25,
    'Vanduo': 0.65,
    'Mėsa' : 7.25,
    'Alus be alc' :0.98,
    'Gerimas':2.5,
    'Cola' : 1.25
}

print(sum(prekes.values()))
# print(sum(prekes))

# ivedu prekiu pavadinimus, automatiskai sumojama kaina, baigiasi ivedimas ivedus end
#jei nera tokios prekes paraso nera

def perkam():
    suma = 0
    sarasas = []
    while True:
        vienaPreke = input('ka perkame?')
        if vienaPreke == 'end':
            break
        elif vienaPreke in prekes.keys():
            suma += prekes[vienaPreke]
            sarasas.append(vienaPreke)
        else:
            print('Tokios prekes nera ')
    return f'Pirkiniu sarasas {str(sarasas)[1:-1]}. Isleidome: {suma}' 

print(perkam())