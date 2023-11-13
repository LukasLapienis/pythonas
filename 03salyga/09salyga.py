# ar blogas pazymys

# if p<=0 or p>=11:
#     print('Netinkamas')
#   1<=p<=10

def ivedimas():
    p = int(input('p = '))
    if  not(1<=p<=10):
        print('Netinkamas. Kartokite ivedima')
        return ivedimas()
    else:
        return p


paz = ivedimas()
print('pazymys =',paz)



