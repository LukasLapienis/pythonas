def dalyba(x, y):
    rez = x / y
    return rez


a = 5
b = 10
rez1 = dalyba(a, b)
print(rez1)
rez2 = dalyba(b, a)
print(rez2)

rez3 = dalyba(y=b, x=a)
print(rez3)