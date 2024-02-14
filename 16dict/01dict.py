#vardas tel.nr
komandaA = dict(Jonas = 15, Petras = 17, Stasys = 25, Rimas = 17)
print(type(komandaA))
print(komandaA)
tuscias = dict()

prekes = {
    'Duona': 1.25,
    'Vanduo': 0.65,
    'Mėsa' : 7.25,
    'Alus be alc' :0.98
}
print(prekes)
print(prekes['Alus be alc'])
prekes['Zuvis'] = 15.25
print(prekes)
# print(prekes['Tokios nera'])
print(prekes.get('Tokios nera'))
ats = 'Tokios prekes neturime'
print(prekes.get('Tokios nera', ats))

print(prekes.get('Duona', ats))

komandaB = dict.fromkeys(['Jonas', 'Petras', 'Antanas'])
print(komandaB)

komandaC = dict.fromkeys(['Jonas', 'Petras', 'Antanas'],'Nezaide')
print(komandaC)
komandaC['Jonas'] = 5
print(komandaC)

del prekes['Alus be alc']
print(prekes)
kaIstrynem = prekes.pop('Mėsa')
print(kaIstrynem)
print(prekes)
prekes.popitem()
print(prekes)