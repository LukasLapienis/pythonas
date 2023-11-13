Kaina = float(input('iveskite kavos kaina eurais: '))
suma = 0
liko = 0
while suma < Kaina:
    Moneta = int(input('Imeskite moneta: '))
    if Moneta == 1 or Moneta == 2:
        suma = suma + Moneta
        liko = Kaina - suma
        print(f'liko sumoketi: {liko}')
    elif Moneta == 10 or Moneta == 20 or Moneta == 50:
        suma = suma + Moneta * 0.01
        liko = Kaina - suma
        print(f'liko sumoketi: {liko}')
    else:
        print("netinkama moneta")
    

