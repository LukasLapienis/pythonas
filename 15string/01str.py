print('daug \'teksto\' ir "įvairių" kabučių. "Ir" kitas tekstas')
kelias = "c:\\new\\tadas.txt"
print(kelias)
kelias1 = "c:/new/tadas.txt" #linux
kitasKelias = r'c:\new\tada.txt'
print(kitasKelias)
print('labas \trytas')
#\n naujas eilute \t tabuliacija

t1 = 'labas rytas'
print(t1)
print(t1[6])
print(t1[-1])
# t1[6] = 'R' #negalim keisti str
print(t1[3:])
print(t1[3:8])
print(t1[::2])

t2 = "labai"
t3 = "noriu"
t4 = "namo"
t5 = t2 + t3 + t4
print(t5)
t6 = t2 + ' ' + t3 + ' ' + t4
print(t6)

# %s
print("%s %s %s" % (t3, t2, t4))
t7 = "%s %s %s" % (t3, t2, t4)
print(t7)

print('{} {} {}'.format(t4, t2, t3))
print(f'{t2} {t3} {t4}')

print(f'{(t2+" ")*3} {t3} {t4}')

# print(2 + '3')

