#ivedamas skaicius sk = 5 
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

sk = int(input('sk = '))
for j in range(sk):
    for i in range(1, sk - j + 1):
        print(i, end=(' '))
    print()