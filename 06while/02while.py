#Petriukas....
kiek = int(input('Kiek Petriukas turi pažymių? '))
kelintas = 0
suma = 0
while kiek > kelintas:
    kelintas +=1
    paz = int(input(f'Įveskite Petriuko {kelintas}-ąjį pažymį '))
    if 1<=paz<=10:
        suma+=paz
    else:
        print('Blogas pažymys. Kartokite įvedimą')
        kelintas -= 1
vid = suma / kiek
print(vid)
