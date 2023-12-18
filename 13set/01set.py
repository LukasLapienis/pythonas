aibeA = set()
print(type(aibeA))
aibeB = {}
print(type(aibeB))
aibeC = {1, 8, 9, 7}
print(type(aibeC))

# print(aibeC[0]) #nepavyks, aibe neturi indekso
for i in aibeC:
    print(i)

aibeC.add(11)
print(aibeC)
aibeC.add(11)
print(aibeC)
sar = [1, 1, 8, 9, 7, 8, 6, 1, 1, 7, 5, 3, 3]
aibeD = set(sar)
print(aibeD)

print(1 in aibeD)