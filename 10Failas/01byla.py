# r
# a
# w
# try:
#     f = open('01data.txt', 'w', encoding='utf-8')
#     f.write('Pirmas kartas su failu\n')
#     f.write('ĄČĘĖĮŠŲŪŽ')
#     a = [5, 8, 9, 7, 9]
#     f.write(a)
#     f.write(str(a))
#     x = 5
#     y = 8
#     f.write(f'\n{x} + {y} = {x+y}\n')
# finally:
#     f.close()

with open('10Failas/01data.txt', 'w', encoding='utf-8') as f:
    f.write('Pirmas kartas su failu\n')
    f.write('ĄČĘĖĮŠŲŪŽ')
    a = [5, 8, 9, 7, 9]
    f.write(a) # klaida
    f.write(str(a))
    x = 5
    y = 8
    f.write(f'\n{x} + {y} = {x+y}\n')