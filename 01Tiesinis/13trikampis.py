#duota stataus trikampio statinis a ir izambine c. Rasti tikampio plota
import math
a = float(input('a= '))
c = float(input('c= '))
# b = math.sqrt(c**2 - a**2)
b = math.sqrt(math.pow(c,2)-math.pow(a,2))
S = (1/2) * a * b
print(f'Plotas = {S}')

