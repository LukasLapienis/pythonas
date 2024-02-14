def skaitomFaila():
    with open('16dict/11data.txt', 'r', encoding='utf-8') as f:
        txt = f.readlines()
        duomenys = dict()
        print(txt)
        for eilute in txt:
            kerpamPerKableli = eilute.split(', ')
            vardas = kerpamPerKableli[0]
            pazTxt = kerpamPerKableli[1].split()
            pazymiai = [int(paz) for paz in pazTxt]
            duomenys[vardas] = pazymiai
    return duomenys

def spausdinti(klase):
    with open('16dict/11rez.txt', 'a', encoding='utf-8') as f:
        for vardas, pazymiai in klase.items():
            f.write(f'{vardas:18} {str(pazymiai)[1:-1]}\n')
        f.write('\n------------------------------------------\n')

def valyti():
    with open('16dict/11rez.txt', 'w', encoding='utf-8') as f:
        pass

valyti()
duomenys = skaitomFaila()
spausdinti(duomenys)
duomenys1 = dict(sorted(duomenys.items(), key = lambda keyValue : -sum(keyValue[1])/len(keyValue[1])))
spausdinti(duomenys1)
duomenys2 = dict(sorted(duomenys.items(), key = lambda keyValue : -len(keyValue[1])))
spausdinti(duomenys2)