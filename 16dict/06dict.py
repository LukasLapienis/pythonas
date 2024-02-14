draugai ={
    'Žygis': 37,
    'Petras': 29,
    'Rimas' : 18,
    'Ona': 25,
    'Greta': 29,
    'Aidas':28
}

print(draugai)
print(sorted(draugai))
pagalVarda = dict(sorted(draugai.items()))
print(pagalVarda)

pagalAmziu = dict(sorted(draugai.items(), key=lambda kv: kv[1]))
print(pagalAmziu)

pagalAmziuVarda = dict(sorted(draugai.items(), key = lambda kv:(kv[1], kv[0])))
print(pagalAmziu)