def ivedimas():
    n = int(input('iveskite eiluciu skaiciu '))
    m = int(input('iveskite stulpeliu skaiciu '))
    matrix = []
    for i in range(n):
        eil = []
        for j in range(m):
            eil.append(int(input(f'iveskite A({i})({j}) = ')))
        matrix.append(eil)
    return matrix

def spausdinimas():
    A = ivedimas()
    for row in A:
        for element in row:
            print(element, end=' ')
        print()

spausdinimas()