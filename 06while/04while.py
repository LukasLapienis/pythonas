# ivedamas skaicius Rasti to skaiciaus skaitmenu suma... 
sk = int(input('Iveskite skaiciu...'))
suma = 0
kopija = sk
while sk > 0:
    x1 = sk % 10
    sk = sk // 10 # sk //= 10
    suma += x1

print(f'Skaiciaus {kopija} skaitmenu suma = {suma}')