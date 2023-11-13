#ivedamas skaicius sk = 5 
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

sk = int(input('sk = '))
for j in range(1, sk+1):
    for i in range(1, j+1):
        print(i, end=(' '))
    print()