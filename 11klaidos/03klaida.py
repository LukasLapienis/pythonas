# apskaiciuoti 100/sk
import math


while True:
    try:
        sk = int(input('ivesk skaiciu = '))
        rez = 100 / sk
        saknis = math.sqrt(sk)
        break
    except ValueError as ex:
        print(f'klaidos pranesimas {ex}. Kartokite ivedima')
    except ZeroDivisionError:
        print(f'dalyba is 0 negalima. Kartokite ivedima')
    except:
        print('ivyko nezinoma klaida')
    else:
        print('panasu, kad viskas gerai')


print(f'sk = {sk}, rez = {rez}, saknis = {saknis}')