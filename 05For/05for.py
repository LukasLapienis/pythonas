#atspausdinti visus kaicius nuo 1 iki n, jei n lygu  13 jo nespausdinti
n = int(input('n='))
for i in range(1, n+1):
    if i == 13:
        continue
    print(i, end=', ' )
else:
    print('\nViskas ok, ciklas nenutruko....')
print('\nPrograma baige darba....')