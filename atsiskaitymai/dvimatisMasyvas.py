# ----------------------------------------3 uzduotis-----------------------------------------------

import random

def newMatrix():
    row = random.randint(10, 30)
    col = random.randint(10, 30)
    matrix = []
    for i in range(row):
        eil = []
        for j in range(col):
            eil.append(random.randint(-100, 100))
        matrix.append(eil)
    return matrix
    
def saveMatrix(matrix):
    with open('dvimatisMasyvasRez.txt', 'w') as f:
        for row in matrix:
            t = str(row)
            txt = t[1:-1].replace(', ', '\t')
            f.write(f'{txt}\n')


def averages(matrix):
    averages = []
    for row in matrix:
        averages.append(round(sum(row)/len(row), 2))
    return averages

matrix = newMatrix()
saveMatrix(matrix)
print(averages(matrix))
