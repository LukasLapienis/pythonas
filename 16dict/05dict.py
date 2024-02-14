users = {
    'Tomuxx':{'psw':'524*/Fds', 'Admin':False, 'id':1451},
    'Kestuxxs':{'psw':'14*/524*/Fds', 'Admin':False, 'id':1450},
    'Dievss':{'psw':'/*-+*/Fds', 'Admin':True, 'id':1}


}
print(users['Tomuxx'])
print(users['Tomuxx']['psw'])

# Noriu visu slaptazodziu
print(users.items())
for user, data in users.items():
    print(f'Vartotojas {user} slaptazodis {data["psw"]}')