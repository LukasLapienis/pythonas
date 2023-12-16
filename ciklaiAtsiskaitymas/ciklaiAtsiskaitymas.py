#----------------------------------------1 uzduotis-----------------------------------------

while True:
    try:
        kaina = float(input('iveskite kavos kaina eurais: '))
        if kaina <= 0:
            print("prasau iveskite teigiama skaiciu")
        else:
            break
    except:
        print("blogai ivesta kaina, bandykite dar karta")

suma = 0
countBad = 0
countGood = 0
while suma < kaina:
    liko = kaina - suma
    print(f'liko sumoketi: {round(liko, 2)} euro')
    try:    
        Moneta = int(input('Imeskite moneta: '))
        if Moneta == 1 or Moneta == 2:
            suma = suma + Moneta
            countGood = countGood + 1
        elif Moneta == 10 or Moneta == 20 or Moneta == 50:
            suma = suma + Moneta * 0.01
            countGood = countGood + 1
        else:           
            print("netinkama moneta, meskite dar karta")
            countBad = countBad + 1
    except:
        print("Nezinau ka idejote, bet ne moneta, bandykite dar karta")
else:
    liko = kaina - suma
    print(f'jusu graza {round(liko * -1, 2)} euro, skanios kavos!')
    print(f'imesta tikru monetu: {countGood}, padirbtu: {countBad}')


#-------------------------------------------------------------------------------------------
#------------------------------------2 uzduotis---------------------------------------------
#perziureti
# while True:
#     try:
#         number = int(input('iveskite skaiciu ir pavaizduosiu zvaigzdutemis: '))
#         break
#     except:
#         print("blogai ivestas skaicius, bandykite dar karta")

# numberStr = str(number)
# length = len(numberStr)
# print(f'skaicius sudarytas is {length} skaitmenu')

# i = 0
# while i < length:
#     print("*" * int(numberStr[length-i-1]))
#     i += 1


# #-------------------------------------------------------------------------------------------

# #------------------------------------3 uzduotis---------------------------------------------
# #pakeist

import random

def zaidimas():
    n = int(input('Iveskite maksimalu skaiciu n:... '))
    if n <= 0:
      print('Ivestas netinkamas skaicius, iveskite nauja:...')
      return
    sk = random.randint(1, n)
    spejimai = 0
    while True:
        spejimas = int(input(f'Atspekite mano skaiciu nuo 1 iki {n}:... '))
        spejimai += 1
        if spejimas < 1 or spejimas > n: print(f'Spejimas turi būti nuo 1 iki {n}.')
        elif spejimas < sk: 
            print(f'mano skaicius didesnis uz {spejimas}.')
        elif spejimas > sk: 
            print(f'mano skaicius mazesnis uz {spejimas}.')
        else:
            print(f'Sveikiname! Atspejot skaiciu {sk} per {spejimai} spejimus.')
            break

def zaidziam():
    kartot = 't'
    while kartot == 't':
        if kartot == 't':
            zaidimas()
        elif kartot == 'n': 
            print('Aciu, kad zaidet!')
        else: 
            print('klaida')
        kartot = input('Ar norite zaisti dar karta? (t/n): ')

zaidziam()




#-------------------------------------------------------------------------------------------