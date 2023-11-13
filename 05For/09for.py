# ATSPAUSDINTI visus keturženklius skaičius, kurių skaitmenų suma lygi skaitmenų sandaugai. 
# kiek tokių skaičių yra???
# 1111 suma yra 4 sandauga 1 (netinka)
#4211  suma 8  sandauga 8 (tinka)
#Mintis užsukti cikla nuo 1000 iki 9999 ....
kiek = 0
for i in range(1000, 10000):
    x1 = i // 1000
    x2 = i // 100 % 10
    x3 = i // 10 % 10
    x4 = i % 10
    suma = x1 + x2 + x3 + x4
    sd = x1 * x2 * x3 * x4
    if suma == sd:
        print(i, end=", ")
        kiek += 1
print(f'tokiu skaiciu yra {kiek}')
    


