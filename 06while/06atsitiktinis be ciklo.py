#norime sugeneruoti atsitiktini skaiciu....
import random 
n = int(input('n= '))
sk = random.randint(0, n)
print (f'sk = {sk}')
sk1 = random.randrange(1, n, 2)
print(f'sk = {sk1}')
for i in range(10):
    sk2 = random.random()
    print(f'sk = {int(sk2*100)}')