# Kartais žmonėms būna sunku prisiminti, kokia šiandien yra savaitės diena, o ir 
# kalendorius ne visada būna po ranka. Parašykite programą, kuri išspausdintų 
# vieno mėnesio savaitės dienų sąrašą nuo a dienos iki b dienos, jei žinoma, 
# kad mėnuo prasidėjo m-tąją savaitės dieną. Savaitės dienos numeruojamos taip: 
# 1-pirmadienis, 2-antradienis ... 7 - sekmadienis.

savDiena = int(input('Kokia  savaites diena prasideda menuo? '))
a =int(input('Kokia saraso pradzia...')) 
b =int(input('Kokia saraso pabaiga...')) 
for i in range(1, 32):
    if a<=i<=b:
        print(f'{i}-oji menesio diena bus {savDiena} savaites diena')
    if savDiena == 7:
        savDiena = 1
    else:
        savDiena += 1
    if i==b:
        break
