import random

def valom():
    with open('failaiAtsiskaitymas/reg.txt', 'w') as f:
        pass

def irasymas(txt):
    with open('failaiAtsiskaitymas/reg.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

# def zaidimas():
#     n = int(input('Iveskite maksimalu skaiciu n:... '))
#     irasymas(f'Vartotojas ivede skaiciu {n}.')
#     if n <= 0:
#       print('Ivestas netinkamas skaicius, iveskite nauja:...')
#       return
#     sk = random.randint(1, n)
#     irasymas(f'Sugeneruotas atsitiktinis skaicius {sk}')
#     spejimai = 0
#     while True:
#         spejimas = int(input(f'Atspekite mano skaiciu nuo 1 iki {n}:... '))
#         spejimai += 1
#         if spejimas < 1 or spejimas > n: print(f'Spejimas turi būti nuo 1 iki {n}.')
#         elif spejimas < sk: 
#             print(f'mano skaicius didesnis uz {spejimas}.')
#             irasymas(f'{spejimai} spejimu vartotojas ivede {spejimas}. Atsakymas - sugeneruotas skaicius didesnis')
#         elif spejimas > sk: 
#             print(f'mano skaicius mazesnis uz {spejimas}.')
#             irasymas(f'{spejimai} spejimu vartotojas ivede {spejimas}. Atsakymas - sugeneruotas skaicius mazesnis')
#         else:
#             print(f'Sveikiname! Atspejot skaiciu {sk} per {spejimai} spejimus.')
#             irasymas(f'{spejimai} spejimu vartotojas atspejo skaiciu')
#             break
#     # kartot = input('Ar norite zaisti dar karta? (t/n): ')
#     # if kartot == 't':
#     #     irasymas(f'i uzklausa "Ar zaisite dar" pasirinko "taip"') 
#     #     zaidimas()
#     # elif kartot == 'n':
#     #     irasymas(f'i uzklausa "Ar zaisite dar" pasirinko "ne"\nVartotojas zaide kartus(u)') 
#     #     print('Aciu, kad zaidet!')
#     # else: 
#     #     print('klaida')

# valom()
# zaidimas()
zaidimuSkaicius = 1
kartot = 't'
while kartot == 't':
    if kartot == 't':
        irasymas(f'i uzklausa "Ar zaisite dar" pasirinko "taip"') 
        # zaidimas()
        zaidimuSkaicius += 1
    elif kartot == 'n': 
        print('Aciu, kad zaidet!')
    else: 
        print('klaida')
    kartot = input('Ar norite zaisti dar karta? (t/n): ')

irasymas(f'i uzklausa "Ar zaisite dar" pasirinko "ne"\nVartotojas zaide {zaidimuSkaicius} kartus(u)')


