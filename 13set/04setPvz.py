import time 

def fun(*args):
    sar = []
    for i in args:
        for j in i:
            if j not in sar:
                sar.append(j)
    return sar

sarA = list(range(10000))
sarB = list(range(2500, 16000))
sarC = list(range(1000, 30000))
sarG = []
pradzia1 = time.time()
sarG = fun(sarA, sarB, sarC)
pabaiga1 = time.time() - pradzia1
print(pabaiga1)

pradzia2 = time.time()
aibe1 = set(sarA)
aibe2 = aibe1.union(set(sarB), set(sarC))
pabaiga2 = time.time() - pradzia2
print(pabaiga2)