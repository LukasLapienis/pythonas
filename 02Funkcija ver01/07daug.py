# x1, x2, x3 apskaiciuoti "pvm"

def pvm1(x1=0, x2=0, x3=0):
    return sum([x1, x2, x3])*0.21

pvmDydis1 = pvm1(15.25, 19.25,21.25) 
print(pvmDydis1)

def pvm2(*args):
    print(type(args))
    # ----------------------
    for i in args:
        print('args= ',i)
    # ----------------------
    return sum(args)*0.21

pvmDydis2 = pvm2(15.25, 19.25,21.25, 8, 15.25, 5.41) 
print(pvmDydis2)