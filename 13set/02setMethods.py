aibeA = {1, 2, 3, 4, 5}
aibeB = {1, 2, 3, 4, 5, 7, 8, 11}

#ar poaibis
print(aibeA.issubset(aibeB))
print(aibeB.issubset(aibeA))

#virsaibis
print(aibeA.issuperset(aibeB))
print(aibeB.issuperset(aibeA))

aibeC = {12, 13, 14, 15}
#ar visi skirtingi
print(aibeC.isdisjoint(aibeB))

#aibiu sajunga
aibeD = aibeA.union(aibeB)
print(aibeD)

#aibiu sankirta
aibeE = aibeA.intersection(aibeB)
print(aibeE)

#skirtumas
aibeF = aibeA.difference(aibeB)
aibeG = aibeB.difference(aibeA)
print(aibeF)
print(aibeG)