txt = 'mano batai buvo Du, bet kazkas atsitiko tai nerandu'
print(len(txt))

print(txt[len(txt)-1])
raide_a = txt.count('a')
print(raide_a)
kiekZodziu = txt.count(' ')
print(kiekZodziu) #ar tikrai taip???

print(txt.capitalize())

# ar zaisim dar (Taip \ Ne)
#taip
#TAIP
#tAip
#   Taip
print(txt.upper())
print(txt.lower())
mazasTxt = txt.lower()
print(mazasTxt.islower())
print(mazasTxt.isupper())

print(txt.find('a'))
print(txt[3:].find('a'))
print(txt.find('a', 3))
print(txt.find('a', 8, 20))
print(txt.rfind('a'))

t = '123abc456'
print(t.isalnum())
t1 = '123ab.c456'
t2 = 'asff'
print(t1.isalnum())
print(t.isalpha()) # ar tik raides
print(t2.isalpha())
t3 = '   '
t4 = ''
print(t3.isspace()) # ar tik tarpai
print(t4 == '') # ar tuscia

t5 = ' Tadas  '
beTarpu = t5.strip()
print(beTarpu)
