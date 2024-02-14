prekes = {
    'Duona': 1.25,
    'Vanduo': 0.65,
    'Mėsa' : 7.25,
    'Alus be alc' :0.98,
    'Gerimas':'Cola'
    # 'Cola' : 1.25
}

prekiuSarasas = list(prekes.keys())
print(prekiuSarasas)
print(type(prekiuSarasas))

prekiuKainos = list(prekes.values())
print(prekiuKainos)
print('Zuvis' in prekes.keys())
print('Zuvis' in prekes)
print('Cola' in prekes)
print('Cola' in prekes.values())
de = 0
prekes.setdefault('Pica',de)
print(prekes)


for k, v in prekes.items():
    print(f'Prekes {k} kaina {v} eur.')


for k in prekes.keys():
    print(f'Prekes {k} kaina {prekes[k] } eur.')

print(len(prekes))   
prekiuKopija = prekes.copy()
