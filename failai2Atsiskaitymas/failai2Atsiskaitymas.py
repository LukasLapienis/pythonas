# -----------------------------------Skaiciu kovos---------------------------------------------------------------

def clear():
    with open('failai2Atsiskaitymas/skaiciuKovos.txt', 'w') as f:
        pass

def record(txt):
    with open('failai2Atsiskaitymas/skaiciuKovos.txt', 'a', encoding='utf-8') as file:
        file.write(f'{txt}\n')

def read():
    with open('failai2Atsiskaitymas/skaiciuKovos.txt', 'r', encoding='utf-8') as file:
        file.read
        readFile = file.readline()
        print((readFile))

read()