p = int(input('Iveskite pazymi...: '))
teiginys = (p<0) or (p>10)
if teiginys:
    print('negalimas balas')
 
elif 1<=p<=3:
    print('blogas')
 
elif 4<=p<=6:
    print('patenkinamas')
 
elif 7<=p<=9:
    print('geras')
 
else:
    print('puiku')