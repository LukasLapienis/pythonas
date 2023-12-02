#----------------------------------------1 uzduotis-----------------------------------------

# while True:
#     try:
#         kaina = float(input('iveskite kavos kaina eurais: '))
#         break
#     except:
#         print("blogai ivesta kaina, bandykite dar karta")

# suma = 0
# countBad = 0
# countGood = 0
# while suma < kaina:
#     liko = kaina - suma
#     print(f'liko sumoketi: {round(liko, 2)} euro')
#     try:    
#         Moneta = int(input('Imeskite moneta: '))
#         if Moneta == 1 or Moneta == 2:
#             suma = suma + Moneta
#             countGood = countGood + 1
#         elif Moneta == 10 or Moneta == 20 or Moneta == 50:
#             suma = suma + Moneta * 0.01
#             countGood = countGood + 1
#         else:           
#             print("netinkama moneta, meskite dar karta")
#             countBad = countBad + 1
#     except:
#         print("Nezinau ka idejote, bet ne moneta, bandykite dar karta")
# else:
#     liko = kaina - suma
#     print(f'jusu graza {round(liko * -1, 2)} euro, skanios kavos!')
#     print(f'imesta tikru monetu: {countGood}, padirbtu: {countBad}')


#-------------------------------------------------------------------------------------------
#------------------------------------2 uzduotis---------------------------------------------

while True:
    try:
        number = int(input('iveskite skaiciu ir pavaizduosiu zvaigzdutemis: '))
        break
    except:
        print("blogai ivestas skaicius, bandykite dar karta")

numberStr = str(number)
length = len(numberStr)
print(length)

i = 0
while i != length:
    print("*" * int(numberStr[length-i-1]))
    i += 1


#-------------------------------------------------------------------------------------------

#------------------------------------3 uzduotis---------------------------------------------




#-------------------------------------------------------------------------------------------