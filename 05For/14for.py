#Vinis
import math
viniesIlgis = int(input('Kokio ilgio vinis? '))
k = float(input('Kiek cm vinies ikalama? '))
for i in range(1, int(math.ceil(viniesIlgis/k)+1)):
    viniesIlgis = round(viniesIlgis - k,2)
    if viniesIlgis > 0:
         print(f'"Tuk!" {i}-asis smugis. Dar liko {viniesIlgis} cm neikaltos vinies')
    else:
         print(f'"Tuk!" {i}-asis smugis. Vinis ikalta')
         break
        