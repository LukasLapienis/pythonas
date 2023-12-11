# apskaiciuoti 100/sk
import math

veikia = True
while veikia:
    try:
        sk = int(input('ivesk skaiciu = '))
        rez = 100 / sk
        saknis = math.sqrt(sk)
        veikia = False
    except ValueError as ex:
        print(f'klaidos pranesimas {ex}. Kartokite ivedima')
    except ZeroDivisionError:
        print(f'dalyba is 0 negalima. Kartokite ivedima')
    except:
        print('ivyko nezinoma klaida')
    else:
        print('veikiu kai viskas gerai')
    finally:
        print('as visada veikiu')


print(f'sk = {sk}, rez = {rez}, saknis = {saknis}')