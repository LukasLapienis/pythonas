#547896
sk = int(input('Iveskite sesiazenkli skaiciu...'))
x1 = sk // 100000       # 547896 // 100000 --> 5
x2 = sk // 10000 % 10   # 547896 // 10000 --> 54 % 10 --> 4
x3 = sk // 1000 % 10    # 547896 // 1000 --> 547 % 10 -->7
x4 = sk // 100 % 10     # 547896 // 100 --> 5478 % 10 -->8
x5 = sk // 10 % 10      # 547896 // 10 --> 54789 % 10 -->9
x6 = sk  % 10           # 547896 % 10-->6
suma = x1+x2+x3+x4+x5+x6
print(f'skaiciaus {sk} skaitmenu suma lygi {suma}')
