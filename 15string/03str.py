#atspausdinti visas a raides vietas (indexus)
txt = 'mano batai buvo Du, bet kazkas atsitiko tai nerandu'
a = 0
raide_a = txt.count('a')
masyvas = []
for i in range(raide_a):
    c = txt.find('a', a)
    a = c + 1
    masyvas.append(c)

print(masyvas)

t1 = 'pirmas kartas o gal ir ne'
print(t1.startswith('pi'))
print(t1.endswith('as'))

sp1 = t1.split(' ')
print(sp1)

sp2 = t1.split(' ', 2)
print(sp2)

sar = ['Jonas', '+', 'Ona', '=', 'KM']
txt1 = ' '.join(sar)
print(txt1)

meile = 'Man labai patinka Coca cola'
meile1 = meile.replace('Coca', 'Pepsi')
print(meile1)

pi = 3.141592

print(f'skaicius pi ={pi:1.2f}')
print(f'skaicius pi ={pi:10.2f}')