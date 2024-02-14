def skaitomFaila():
    with open('16dict/10data.txt', 'r', encoding='utf-8') as f:
        txt = f.readlines()
        duomenys = dict()
        print(txt)
        for eilute in txt:
            vardas = eilute[:20].strip()
            likusiEilute = eilute[20:].strip()
            duomenys[vardas] = [int(i) for i in likusiEilute.split()]
    return duomenys

def spausdinti(komanda):
    with open('16dict/10rez.txt', 'a', encoding='utf-8') as f:
        f.write('\n-------------------------------------------------------\n')
        f.write('| Vardas             | Viso | 3 t. | 2 t. | 1 t. | Pr |\n')
        f.write('\n-------------------------------------------------------\n')
        for vardas, taskai in komanda.items():
            f.write(f'| {vardas:18} | {taskai[4]:4} | {taskai[0]:4} | {taskai[1]:4} | {taskai[2]:4} | {taskai[3]:4} |\n')
        f.write('\n-------------------------------------------------------\n')

def rezultatas():
    komanda = skaitomFaila()
    for key, value in komanda.items():
        komanda[key].append(3*value[0] + 2*value[1] + value[2])
    return komanda

def valyti():
    with open('16dict/10rez.txt', 'w', encoding='utf-8') as f:
        pass

valyti()
komanda = rezultatas()
spausdinti(komanda)

komanda1 = dict(sorted(komanda.items(), key=lambda keyValue: -keyValue[1][4]))
spausdinti(komanda1)

komanda2 = dict(sorted(komanda.items(), key=lambda keyValue: (-keyValue[1][4], -keyValue[1][0], -keyValue[1][1], -keyValue[1][2], keyValue[1][3])))
spausdinti(komanda2)

komanda3 = dict(sorted(komanda.items(), key=lambda keyValue: (-keyValue[1][4], -keyValue[1][0], -keyValue[1][1], -keyValue[1][2], keyValue[1][3], keyValue[0])))
spausdinti(komanda3)