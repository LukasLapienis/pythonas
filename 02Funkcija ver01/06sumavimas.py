#parasyti programa, kuri sudeda du skaicius (su funkcijomis)
#  5 + 8 = 13


def ivedimas(txt):
    sk = int(input(f'{txt}=...'))
    return sk

def sumavimas():
    sk1 = ivedimas('Pirmas')
    sk2 = ivedimas('Antras')
    suma = sk1 + sk2 
    return suma, sk1, sk2

def rezultatas():
    sum, a, b = sumavimas()
    #a, b, c = 5, 8, 14  
    print(f'{a}+{b}={sum}')  

rezultatas()