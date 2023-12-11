while True:
    try:
        sk = int(input('ivesk skaiciu = '))
        break
    except ValueError as ex:
        print(f'klaidos pranesimas {ex}. Kartokite ivedima')


print(sk)
