# -----------------------------------Skaiciu kovos---------------------------------------------------------------

def clear():
    with open('failai2Atsiskaitymas/skaiciuKovos.txt', 'w') as f:
        pass

def record(txt):
    with open('failai2Atsiskaitymas/skaiciuKovos.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

def readAndList():
    with open('failai2Atsiskaitymas/skaiciuKovos.txt', 'r', encoding='utf-8') as file:
        file.read
        readFile = file.read()
        splited = [int(i) for i in readFile.split(' ')]
    return splited

startingNumbers = readAndList()
print(startingNumbers)


while len(startingNumbers) > 1:
    if startingNumbers[0] == startingNumbers[1]:
        startingNumbers[0] = startingNumbers[0] + startingNumbers[1]
        startingNumbers.pop(1)
    elif startingNumbers[0] > startingNumbers[1]:
        startingNumbers[0] = startingNumbers[0] + startingNumbers[0] - startingNumbers[1]
        startingNumbers.pop(1)
    elif startingNumbers[0] < startingNumbers[1]:
        startingNumbers[0] = startingNumbers[1] + startingNumbers[1] - startingNumbers[0]
        startingNumbers.pop(1)
    
    print(startingNumbers)

