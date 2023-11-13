#Atspausdinti skaicius nuo 1 iki n
n = int(input('n=...'))
k = 1
while n >= k:
    print(k, end=(', ')) 
    k += 1
    k = k - 1 
    