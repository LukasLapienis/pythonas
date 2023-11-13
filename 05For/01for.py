txt = 'Man rytais labai patinka anksti keltis ir eiti į mokyklą'
kiek  = 1
for i in txt:
    print(i)
    if i ==' ':
        kiek += 1 # kiek = kiek + 1
print(f'Sakinyje "{txt}" yra {kiek} žodžių')