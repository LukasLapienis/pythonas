def skaitomFaila():
    with open('16dict/09data.txt', 'r', encoding='utf-8') as f:
        txt = f.readlines()
        print(txt)
    return txt

def apdorotiDuomenys():
    dalyviai = dict()
    duomenys = skaitomFaila()
    for eil in duomenys:
        vardas, taskai = eil.split()
        print(vardas, taskai)
        taskai = int(taskai)
        if vardas in dalyviai:
            dalyviai[vardas].append(taskai)
        else:
            dalyviai[vardas] = [taskai]
    return dalyviai

def spausdinti(rez):
    with open('16dict/09rez.txt', 'a', encoding='utf-8') as f:
        f.write('\n-------------------------\n')
        f.write('| Vardas  | Sum | Max |\n')
        f.write('\n-------------------------\n')
        for vardas, suma, max_t in rez:
            f.write(f'| {vardas:8} | {suma:3} | {max_t:3} |\n')
        f.write('\n-------------------------\n')

def valyti():
    with open('16dict/09rez.txt', 'w', encoding='utf-8') as f:
        pass

valyti()
komanda = apdorotiDuomenys()
print(komanda)

rez1 = [(vard, sum(task), max(task)) for vard, task in komanda.items()]

print(rez1)
spausdinti(rez1)

spausdinti(sorted(rez1))

spausdinti(sorted(rez1, key=lambda e: e[2], reverse=True))

spausdinti(sorted(rez1, key=lambda e: -e[1]))