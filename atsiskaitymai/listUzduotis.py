#--------------------------------3 1. uzduotis--------------------------------------------
# input int elements and convert it to a list
while True:
    try:
        listInput = list(map(int, input("iveskite masyvo skaicius atskirtus tarpais: ").split()))
        break
    except:
        print("blogai ivesti duomenys, bandykite dar karta")

print(listInput)

# get all positive and even integers from list input
sum = [x for x in listInput if x > 0 and x % 2 == 0]

print(sum)

result = 1
for a in sum:
    result = result * a
print(result)


# !!ar suspaustas geriau?!!
# result = 1
# for a in [x for x in listInput if x > 0 and x % 2 == 0]:
#     result = result * a
# print(result)

#-----------------------------------------------------------------------------------------
#-------------------------------2. uzduotis-----------------------------------------------

# input int elements and convert it to a list
while True:
    try:
        A = list(map(int, input("iveskite pirmo masyvo skaicius atskirtus tarpais: ").split()))
        break
    except:
        print("blogai ivesti duomenys, bandykite dar karta")

while True:
    try:
        B = list(map(int, input("iveskite antro masyvo skaicius atskirtus tarpais: ").split()))
        break
    except:
        print("blogai ivesti duomenys, bandykite dar karta")

print(A)
print(B)

#find positives and make a new list out of them
positiveA = [elementA for elementA in A if elementA >= 0]
positiveB = [elementB for elementB in B if elementB >= 0]
C = positiveA + positiveB

print(C)

#-----------------------------------------------------------------------------------------  