p = int(input('Iveskite prekiu kieki...'))
d = int(input('Kiek telpa i didele deze...'))
m = int(input('Kiek telpa i maza deze...'))
dKiek = p // d
likutis = p % d
mKiek = likutis // m
liko = likutis % m
print(f'reikes {dKiek} dideliu deziu, {mKiek} mazu deziu ir liks {liko} prekiu ')
