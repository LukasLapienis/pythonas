# ivedamas skaicius Rasti to skaiciaus skaitmenu suma... 

def sumavimas(skaicius):
    suma = 0
    while skaicius > 0:
        x1 = skaicius % 10
        skaicius = skaicius // 10 # sk //= 10
        suma += x1
    return (suma)

sk = int(input('Iveskite skaiciu...'))
s = sumavimas(sk)
print(f'Skaiciaus {sk} skaitmenu suma = {s}')