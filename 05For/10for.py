# Anukas turi x euru ir y centu. Senelis visa menesi (30 dienu) dave anukui po a centu. Parasyti programa
# kuri parodytu kiekvienos dienos anuko turimu pinigu kieki.
# pav Anukas turi 20eur. 30ct. Senelis duoda po 50ct.
# rezultatas :
# 1 diena anukas tures 20eur 80ct
# 2 diena anukas tures 21eur 30ct
# 3 diena anukas tures 21eur 80ct
#................................
# 30 diena anukas tures 
prEurai = int(input('Kiek turi euru '))
prCentai = int(input('Kiek turi centu '))
senCentai = int(input('Kiek centu duoda senelis '))
sumaCentais = prEurai*100 + prCentai
for i in range(1, 31):
    sumaCentais = sumaCentais + senCentai
    print(f'{i} diena tures {sumaCentais // 100}euru ir {sumaCentais % 100}centu')