#atspausdinti visus kaicius nuo 1 iki n, jei n daugiau už 13 spausdinti iki 13
n = int(input('n='))
for i in range(1, n+1):
    print(i, end=', ' )
    if i == 13:
        break
else:
    print('\nViskas ok, ciklas nenutruko....')
print('\nPrograma baige darba....')