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

while True:
    try:
        number = int(input('iveskite skaiciu ir pavaizduosiu zvaigzdutemis: '))
        break
    except:
        print("blogai ivestas skaicius, bandykite dar karta")

numberStr = str(number)
length = len(numberStr)
print(f'skaicius sudarytas is {length} skaitmenu')

i = 0
while i < length:
    print("*" * int(numberStr[length-i-1]))
    i += 1

# #-------------------------------------------------------------------------------------------

# #------------------------------------3 uzduotis---------------------------------------------

import random

def guessNumber():
    while True:
        try:
            maxNumber = int(input("enter a number bigger than zero with no decimal and we play a guessing game: "))      
            if maxNumber > 0:
                break
            else: 
                print("wrong input, try again.")
        except:
            print("wrong input, try again.")
    randomNumber = random.randint(1, maxNumber)
    tryCount = 0
    while True:
        try:
            guessNumber = int(input(f'guess a number between 1 and {maxNumber}: '))
            if guessNumber <= 0 or guessNumber > maxNumber:
                print("wrong input, try again.")
            elif guessNumber < randomNumber:
                tryCount += 1
                print(f'my number is higher than {guessNumber}.')
            elif guessNumber > randomNumber:
                tryCount += 1
                print(f'my number is lower than {guessNumber}.')
            else:
                tryCount += 1
                print(f'You guessed the number {randomNumber} right in {tryCount} tries.')
                break
        except:
            print("wrong input, try again.")

def play():
    guessNumber()
    while True:
        tryAgain = input("Do you want to retry? Enter yes or no: ").lower()
        if tryAgain == "no":
            break
        elif tryAgain == "yes":
            guessNumber()
        else:
            print("Please enter yes or no.")

play()

#-------------------------------------------------------------------------------------------