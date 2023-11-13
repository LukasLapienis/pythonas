#ivedami du skaiciai. did  priskirti didziausia o maz maziausia
# nenaudoti min ir max funkciju
a = int(input('a=...'))
b = int(input('b=...'))

def isvedimas(did, maz):
    print(f'{did} daugiau uz {maz}')
    return did, maz

if a>b:
    isvedimas(a, b)
elif a<b:
    isvedimas(b, a)
else:
    print(f'{a} lygus {b}')

