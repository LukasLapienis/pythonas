#-----------------------------------1 uzduotis-----------------------------------------------------

import random

def valom():
    with open('failaiAtsiskaitymas/skaiciuSpejimai.txt', 'w') as f:
        pass

def irasymas(txt):
    with open('failaiAtsiskaitymas/skaiciuSpejimai.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

def zaidimas():
    n = int(input('Iveskite maksimalu skaiciu n:... '))
    irasymas(f'Vartotojas ivede skaiciu {n}.')
    if n <= 0:
      print('Ivestas netinkamas skaicius, iveskite nauja:...')
      return
    sk = random.randint(1, n)
    irasymas(f'Sugeneruotas atsitiktinis skaicius {sk}')
    spejimai = 0
    while True:
        spejimas = int(input(f'Atspekite mano skaiciu nuo 1 iki {n}:... '))
        spejimai += 1
        if spejimas < 1 or spejimas > n: print(f'Spejimas turi būti nuo 1 iki {n}.')
        elif spejimas < sk: 
            print(f'mano skaicius didesnis uz {spejimas}.')
            irasymas(f'{spejimai} spejimu vartotojas ivede {spejimas}. Atsakymas - sugeneruotas skaicius didesnis')
        elif spejimas > sk: 
            print(f'mano skaicius mazesnis uz {spejimas}.')
            irasymas(f'{spejimai} spejimu vartotojas ivede {spejimas}. Atsakymas - sugeneruotas skaicius mazesnis')
        else:
            print(f'Sveikiname! Atspejot skaiciu {sk} per {spejimai} spejimus.')
            irasymas(f'{spejimai} spejimu vartotojas atspejo skaiciu')
            break

valom()
zaidimas()
zaidimuSkaicius = 1
kartot = 't'
while kartot == 't':
    kartot = input('Ar norite zaisti dar karta? (t/n): ')
    if kartot == 't':
        irasymas(f'i uzklausa "Ar zaisite dar" pasirinko "taip"') 
        zaidimas()
        zaidimuSkaicius += 1
    elif kartot == 'n': 
        print('Aciu, kad zaidet!')
    else: 
        print('klaida')

irasymas(f'i uzklausa "Ar zaisite dar" pasirinko "ne"\nVartotojas zaide {zaidimuSkaicius} kartus(u)')

# ------------------------------------2 uzduotis-----------------------------------------------------

def clear():
    with open('failaiAtsiskaitymas/chineseGame.txt', 'w') as f:
        pass

def record(txt):
    with open('failaiAtsiskaitymas/chineseGame.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

def chineseGame():
    player1 = input("enter first player name: ")
    player2 = input("enter second player name: ")
    record(f'player names: {player1} and {player2}.')
    while True:
        try:
            sticks = int(input('How many sticks you want to play with?\nEnter a number between 1 and 30: '))
            if sticks > 0 and sticks <= 30:
                break
        except:
            print('wrong input, try again')
    record(f'game starts with {sticks} sticks.')

    players = [player1, player2]
    firstPlayer = random.choice(players)
    secondPlayer = player1 if firstPlayer == player2 else player2
    record(f'{firstPlayer} starts the game.')

    while sticks > 0:
        print(f'{firstPlayer} turn. {sticks} sticks left')
        while True:
            takeSticks = input('How many sticks you want to take? Enter number between 1 and 3: ')
            if takeSticks in ('1', '2', '3'):
                takeSticks = int(takeSticks)
                if takeSticks <= sticks:
                    sticks -= takeSticks
                    record(f'{firstPlayer} takes {takeSticks} sticks. {sticks} left')
                    break
                else:
                    print("you can't take more sticks than there is left")
            else: 
                print("Wrong input, try again")
        
        firstPlayer, secondPlayer = secondPlayer, firstPlayer

    print(f"{firstPlayer} wins the game!")
    record(f"{firstPlayer} wins the game.")


def playChineseGame():
    chineseGame()
    gamesCount = 1
    tryAgain = 'yes'
    while tryAgain == 'yes':
        tryAgain = input("Do you want to retry? Enter yes or no: ").lower()
        if tryAgain == "no":
            record(f'Player chose to not play again')
            break
        elif tryAgain == "yes":
            record(f'Player chose to play again')
            gamesCount += 1
            chineseGame()
        else:
            print("Please enter yes or no.")
    record(f'{gamesCount} game(es) played')
  
clear()
playChineseGame()

