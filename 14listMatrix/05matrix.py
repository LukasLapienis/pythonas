#sugeneruoti atsitiktini masyvo eiluciu ir stulpeliu kiek is reziu nuo 5 iki 25
#sugeneruoti dvimati masyva ir issaugoti jo duomenis byloje [-100 100]
#nuskaityti duomenis
#rez bylos sukurimas ???
import random

def gautiSarasa():
    row = random.randint(5, 25)
    col = random.randint(5, 25)
    duMas = []
    for i in range(row):
        eil = []
        for j in range(col):
            eil.append(random.randint(-100, 100))
        duMas.append(eil)
    return duMas

    
def rezultatas():
    duList = gautiSarasa()
    # print(duList)
    with open('14listMatrix/rez5.txt', 'w') as f:
        for row in duList:
            t = str(row)
            txt = t[1:-1].replace(', ', '\t')
            f.write(f'{txt}\n')
            
rezultatas()

def skaiciavimai():
    pass