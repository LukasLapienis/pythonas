# -----------------------------------Skaiciu kovos---------------------------------------------------------------

def clear():
    with open('failai2Atsiskaitymas/rez.txt', 'w') as f:
        pass

def record(txt):
    with open('failai2Atsiskaitymas/rez.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

def readAndList():
    with open('failai2Atsiskaitymas/skaiciuKovos.txt', 'r', encoding='utf-8') as file:
        file.read
        readFile = file.read()
        splited = [int(i) for i in readFile.split(' ')]
    return splited

startingNumbers = readAndList()

def fight():
    clear()
    round = 0
    while len(startingNumbers) > 1:
        round += 1
        if startingNumbers[0] == startingNumbers[1]:
            startingNumbers[0] = startingNumbers[0] + startingNumbers[1]
            startingNumbers.pop(1)
            record(f'{round} kova. Lygiosios. Skaiciai susijungia.')
        elif startingNumbers[0] > startingNumbers[1]:
            startingNumbers[0] = startingNumbers[0] + startingNumbers[0] - startingNumbers[1]
            startingNumbers.pop(1)
            record(f'{round} kova. Pirmas skaicius sunaikina antra skaiciu.')
        elif startingNumbers[0] < startingNumbers[1]:
            startingNumbers[0] = startingNumbers[1] + startingNumbers[1] - startingNumbers[0]
            startingNumbers.pop(1)
            record(f'{round} kova. Antras skaicius sunaikina pirma skaiciu.')
        
        extractedList = ' '.join(str(x) for x in startingNumbers)
        record(f'Rezultatas {extractedList}')
        
fight()
