def valytiByla(byla):
    with open(byla, 'w') as f:
        pass

def rasytiIByla(byla, txt):
    with open(byla, 'a', encoding='utf-8') as f:
        f.write(txt + '\n')

def skaitytiByla(byla, bylosDuomenys):
    with open(byla, 'r', encoding='utf-8') as f:
        while True:
            eilute = f.readline()
            if len(eilute) != 0:
                bylosDuomenys.append(eilute)
                print(bylosDuomenys)
            else:
                break
    return bylosDuomenys

######################################################################################

valytiByla('rez.txt')
kodas = []
kodas = skaitytiByla('duom.txt', kodas)

issifruotasKodas = []

for i in kodas:
    zodis = str(i)
    # print(zodis)
    issisfruota = []
    for j in range(len(zodis)):
        if 64 < ord(zodis[j]) < 91:
            issisfruota.append(chr(155 - ord(zodis[j])))
        elif 96 < ord(zodis[j]) < 123:
            issisfruota.append(chr(219 - ord(zodis[j])))
        else:
            issisfruota.append(zodis[j])
    issZodis = ''.join(issisfruota)
    issifruotasKodas.append(issZodis)

for eilute in issifruotasKodas:
    rasytiIByla('rez.txt', f'{str(eilute).replace(",", "")}')