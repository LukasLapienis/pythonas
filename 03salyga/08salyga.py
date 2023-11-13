#ivedamas pazimys jei nuo -... iki 0 negalimas balas
#nuo 1 iki 3 blogas
# nuo 4 iki 6 patenkinamas
# nuo 7 iki 9 geras
# 10 puiku
# nuo 11 iki +... negalimas balas
p = int(input('Įveskite pažymį....')) 

if p==10:
    print('puiku')
elif 1<=p<=3:
    print('blogas')
elif 4<=p<=6:
    print('patenkinamas')
elif 7<=p<=9:
    print('geras')
else:
    print('negalimas')