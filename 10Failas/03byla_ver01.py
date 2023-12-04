def sukurtiFaila():
    with open('10Failas/03data.txt', 'w', encoding='utf-8') as f:
        f.write('10, 15, -25, 45, 65, 89, 16, 18, 17, 14\n')
        f.write('15, 36, 41, 55, 47\n')

def nuskaitytiFaila():
    with open('10Failas/03data.txt', 'r', encoding='utf-8') as f:
        eil1 = f.readline().split(', ')
        eil2 = f.readline().split(', ')
        eil1Int = [int(x) for x in eil1]
        eil2Int = [int(x) for x in eil2]
    return eil1Int, eil2Int

def issaugotiDuomenis(failas, duom):
    with open(failas, 'w', encoding='utf-8') as f:
        txtDuom = str(duom)
        f.write(txtDuom[1:-1])
    


sukurtiFaila()
list1, list2 = nuskaitytiFaila()
print(list1)

listNew = [i for i in list1 if i % 2 == 0]
print(listNew)

issaugotiDuomenis('10Failas/03rez.txt', listNew)