a = int(input('a=...'))
b = int(input('b=...'))
c = int(input('c=...'))

def didziausias(x, y):
    if x>y:
        return x
    else:
        return y
    
# did = didziausias(a, b)
# did = (didziausias(c, did))
did = (didziausias(c, didziausias(a, b)))
print(did)