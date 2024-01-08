#--------------------------------------Gimnazistai-----------------------------------------------

def clear():
    with open('failai2Atsiskaitymas/gimnazistaiRez.txt', 'w') as f:
        pass

def record(txt):
    with open('failai2Atsiskaitymas/gimnazistaiRez.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

def readAndList():
    with open('failai2Atsiskaitymas/gimnazistai.txt', 'r', encoding='utf-8') as file:
        read = file.readlines()
        for line in read:
            numbers = list(map(int, line.split()))
            
            record(f'{numbers[0]}')


readAndList()
