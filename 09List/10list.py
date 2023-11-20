# duotas sarasas m = [5, 8, 8, 5, 7, 4, 1, 1, 'labas', 5, 8, -7, -7, 'labas']
# atspausdinti kiek kiekvieno elemento yra 
# pav 5 yra 3
#     8 yra 3 
#     7 yra 1
#     4 yra 1
#     1 yra 2
#     labas yra 2
#     -7 yra 2
# negalima naudoti dict, set !!

m = [0, 5, 8, 8, 5, 7, 4, 1, 1, 'labas', 5, 8, -7, -7, 'labas', 'geras', 'geras', True, True, False, False]
nepas = set(m)
print(nepas)
# for i in m:
#     if not(i in nepas):
#         nepas.append(i)
for i in nepas:
    print(f'{i} yra {m.count(i)}')

