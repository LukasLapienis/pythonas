import random

def gautiSarasa():
    row = random.randint(10, 30)
    col = random.randint(10, 30)
    duMas = []
    for i in range(row):
        eil = []
        for j in range(col):
            eil.append(random.randint(-100, 100))
        duMas.append(eil)
    return duMas
    
# def rezultatas():
#     duList = gautiSarasa()
#     print(duList)
#     with open('dvimatisMasyvasRez.txt', 'w') as f:
#         for row in duList:
#             t = str(row)
#             txt = t[1:-1].replace(', ', '\t')
#             f.write(f'{txt}\n')
            
# rezultatas()

# sk = random.randint(-100, 100)
# print(sk)
matrix = gautiSarasa()
averages = []
for row in matrix: 
 print(row)
 print(sum(row)/len(row))
 averages.append(sum(row)/len(row))
print(averages)