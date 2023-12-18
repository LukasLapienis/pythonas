#sugeneruoti atsitiktini masyvo eiluciu ir stulpeliu kiek is reziu nuo 5 iki 25
#sugeneruoti dvimati masyva ir issaugoti jo duomenis byloje [-100 100]
#nuskaityti duomenis
#rez bylos sukurimas ???
import random

def duomenuFailas():
    rows = random.randint(5, 25)
    columns = random.randint(5, 25)
    # print(f'{rows}, {columns}')
    listSk = []
    for i in range(rows*columns):
        sk = random.randint(-100, 100)
        listSk.append(sk)
    with open('14listMatrix/data.txt', 'w') as f:
        t = str(listSk)
        txt = t[1:-1]
        f.write(txt)
    return rows, columns

def skaitomFaila():
    rows, columns = duomenuFailas()
    with open('14listMatrix/data.txt', 'r') as f:
        listTxt = f.read().split(', ')
        listInt = [int(i) for i in listTxt]
        # print(listInt)
        pradzia = 0
        galas = columns
        matrix = []
        for i in range(rows):
            matrix.append(listInt[pradzia:galas])
            pradzia = galas
            galas += columns
        return matrix
    
def rezultatas():
    matrix = skaitomFaila()
    with open('14listMatrix/rez.txt', 'w') as f:
        for row in matrix:
            t = str(row)
            txt = t[1:-1].replace(', ', '\t')
            f.write(f'{txt}\n')
            
rezultatas()