# 7777777
n = int(input('Kiek skaitmenu '))
k = int(input('koks skaitmuo '))
sk = 0
suma = 0
for i in range(n):
    if i < n-1:
        txt = ' + '
    else:
        txt = ' = '
    sk = sk * 10 + k
    print(sk, end=(txt))
    suma += sk
print(f'{suma}')