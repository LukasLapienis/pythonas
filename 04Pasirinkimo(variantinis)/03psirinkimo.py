# suprogramuoti skaiciuotuva veiksmai +, -, *, /, ^ (kelimas laipsniu) ir &-Šaknies traukimas
import math
a =float(input('a= '))
op = input('Pasirinkite aritmetine operacija (+, -, *, /, ^, #).')
if op in ('+', '/', '-', '*', '^') : #     op!='#'   a
    b =float(input('b= '))
arViskasGerai = True
match op:
    case '+':
        rezultatas = a + b
    case '-':
        rezultatas = a - b
    case '*':
       rezultatas = a * b
    case '/':
        if b != 0:
            rezultatas = a / b
        else:
            print('Dalyba iš nulio negalima')
            arViskasGerai = False
    case '#':
        if a >= 0:
            rezultatas = math.sqrt(a)
            print(f'Iš skaiciaus {a} ištraukus šaknį gausim {rezultatas}')
        else:
            print('Šaknies traukti is neigiamo negalime')
        arViskasGerai = False
    case '^':
        rezultatas = a ** b
    case _ :
        print(f'{op} tokia operacija negalima')
        arViskasGerai = False
if arViskasGerai :
    print(f'{a} {op} {b} = {rezultatas}')