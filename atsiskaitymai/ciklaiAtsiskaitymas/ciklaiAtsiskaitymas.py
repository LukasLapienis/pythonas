#----------------------------------------1 uzduotis-----------------------------------------

while True:
    try:
        price = float(input('iveskite kavos kaina eurais: '))
        if price <= 0:
            print("prasau iveskite teigiama skaiciu")
        else:
            break
    except:
        print("blogai ivesta kaina, bandykite dar karta")

sum = 0
countBad = 0
countGood = 0
while sum < price:
    leftToPay = price - sum
    print(f'liko sumoketi: {round(leftToPay, 2)} euro')
    try:    
        coin = int(input('Imeskite moneta: '))
        if coin == 1 or coin == 2:
            sum = sum + coin
            countGood = countGood + 1
        elif coin == 10 or coin == 20 or coin == 50:
            sum = sum + coin * 0.01
            countGood = countGood + 1
        else:           
            print("netinkama moneta, meskite dar karta")
            countBad = countBad + 1
    except:
        print("Nezinau ka idejote, bet ne moneta, bandykite dar karta")
else:
    leftToPay = price - sum
    print(f'jusu graza {round(leftToPay * -1, 2)} euro, skanios kavos!')
    print(f'imesta tikru monetu: {countGood}, padirbtu: {countBad}')


#-------------------------------------------------------------------------------------------
#------------------------------------2 uzduotis---------------------------------------------

while True:
    try:
        inputNumber = int(input("Input a number: "))
        break
    except:
        print("wrong input, try again.")

numberStr = str(inputNumber)
inputNumberLength = len(numberStr)

i = 0
while i < inputNumberLength:
    print("*" * int(numberStr[inputNumberLength-i-1]))
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