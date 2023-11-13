# ivedu savaites diena skaiciumi 1 man atspausdina pavadinima Pirmadienis

diena = int(input('Kokia savaites diena? '))
viskasOk = True
match diena:
    case 1:
        txt = 'Pirmadienis'
    case 2:
        txt = 'Antradienis'
    case 3:
        txt = 'Trečiadienis'
    case 4:
        txt = 'Ketvirtadienis'
    case 5:
        txt = 'Penktadienis'
    case 6:
        txt = 'Šeštadienis'
    case 7:
        txt ='Sekmadienis'
    case _:
        print('Blogai įvesti duomenys')  #txt = 'Blogai įvesti duomenys'
        viskasOk = False
if viskasOk :
    print(f'{diena} - {txt}')