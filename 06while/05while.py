#ivedamas skaicius. perrasyti ta skaiciu atvirksciai
#12354 >> 45321; 1201200 >> 21021
def atvirkstinis(skaicius):
    at = 0
    while skaicius > 0:
        x1 = skaicius % 10
        skaicius = skaicius // 10 # sk //= 10
        at = at * 10 + x1
    return (at)

sk = int(input('Iveskite skaiciu...'))
s = atvirkstinis(sk)
print(f'Skaiciaus {sk} perrasius atvirskciai gausim = {s}')