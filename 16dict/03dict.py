auto_geras ={
    'Marke': 'Opel',
    'Kaina':2500,
    'Turis':1.4,
    'Dauztas':False
}

auto_blogas ={
    'Dauztas':False,
    'Turis':1.4,
    'Kaina':2500,
    'Marke': 'Opel'
}

print(id(auto_geras))
print(id(auto_blogas))
print(auto_blogas == auto_geras)

daugiau_info={
    'Rida' :254872,
    'Spalva': 'Kibiras',
    'Kaina' : 3500
}

# auto_geras.update(daugiau_info)
# print(auto_geras)
# daugiau_info.update(auto_geras)
# print(daugiau_info)

kitas_auto = auto_blogas|daugiau_info
print(kitas_auto)