sk = int(input('sk = '))
#teiginys = (sk>=5 and sk<=10) or (sk>=20 and sk<=25)
teiginys = (5<=sk<=10) or (20<=sk<=25)

if teiginys:
    print('laimingas ')
else:
    print('nelaimingas')