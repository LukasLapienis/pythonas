#ivedamas skaicius sk = 5 
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

sk = int(input('sk = '))
for j in range(1, sk+1):
    for i in range(1, sk+1):
        print(j, end=(' '))
    print()