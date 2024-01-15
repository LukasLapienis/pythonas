print("staciakampis NR1.")
aKrastineX = int(input("Irasykite X krastines ilgi: "))
aKrastineY = int(input("Irasykite Y krastines ilgi: "))
print("staciakampis NR2.")
bKrastineX = int(input("Irasykite X krastines ilgi: "))
bKrastineY = int(input("Irasykite Y krastines ilgi: "))
print("staciakampis NR3.")
cKrastineX = int(input("Irasykite X krastines ilgi: "))
cKrastineY = int(input("Irasykite Y krastines ilgi: "))
aPlotas = aKrastineX*aKrastineY
bPlotas = bKrastineX*bKrastineY
cPlotas = cKrastineX*cKrastineY
if cPlotas >= aPlotas <= bPlotas:
    print(f'maziausio staciakampo plotas = {aPlotas}')
elif cPlotas >= bPlotas <=aPlotas:
    print(f'maziausio staciakampo plotas = {bPlotas}')
else:
    print(f'maziausio staciakampo plotas = {cPlotas}')