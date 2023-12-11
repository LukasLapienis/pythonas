while True:
    try:
        sk = int(input('ivesk skaiciu = '))
        break
    except ValueError:
        print('blogai ivesti duomenys. Reikia sveiko skaiciaus')


print(sk)
