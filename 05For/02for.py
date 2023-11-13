txt = 'Man rytais labai ž ŽŽ Ą ąčę  patinka anksti keltis ir eiti į mokykląąč'
kiek  = 0
lt ='ąčęėįšųūžĄČĘĖĮŠŲŪŽ'
for i in txt:
    if i in lt:
        kiek += 1 # kiek = kiek + 1
print(f'Sakinyje "{txt}" yra {kiek} lietuviškų simbolių')