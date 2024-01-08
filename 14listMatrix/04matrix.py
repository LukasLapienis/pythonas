grupe = [['Jonas', 5, 8, 9, 7, 8], ['Tadas', 5, 8, 7, 7, 7, 8, 7], ['Antanas', 9, 8, 9, 9, 10, 8, 10], ['Rimas', 5, 8, 7, 9, 7, 10, 10], ['Vyc', 4, 4, 3]]
gerStudNr = None
gerVid = 0

for stud in range(len(grupe)):
    sumPaz = 0
    for nrPaz in range(1, len(grupe[stud])):
        sumPaz += grupe[stud][nrPaz]
        # sum()
    vid = sumPaz / (len(grupe[stud])-1)
    grupe[stud].append(round(vid, 2))
    if vid >= gerVid:
        gerVid = round(vid, 2)
        gerStudNr = stud

print(f'Vardas {grupe[gerStudNr][0]}')
print(f'Viskas apie geriausia {grupe[gerStudNr]}')
print(f'Visa grupe: {grupe}')