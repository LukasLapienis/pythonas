def sukurtBylas(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)

# kuriam daug bylu
for i in range(1, 21):
    sukurtBylas(f'10Failas/04byla/{i}byla.txt', f'{i} byloje irasyta informacija\n')


def nuskaitytiBylas(failas):
    with open(failas, 'r', encoding='utf-8') as f:
        txt = f.read()
    return txt


#spausdinam duomenis
for i in range(1, 21):
    print(nuskaitytiBylas(f'10Failas/04byla/{i}byla.txt'))

