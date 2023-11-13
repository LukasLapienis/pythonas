#apskaiciuoti suma s = 1 +1/2 - 1/3 + 1/4 - 1/5 + 1/6-...+-1/n, n - musu skaicius 
import math
n = int(input('n=...'))
suma1 = suma = 1
for i in range(2, n):
    # if i % 2 == 0:
    #     suma = suma  + 1/i
    # else :
    #     suma = suma - 1/i 
    if i == 1:
        l = 2
    else:
        l = i
    suma1 = suma1  +(pow(-1, l)*1/i )
print(suma)
print(suma1)

