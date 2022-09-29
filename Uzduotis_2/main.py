import pprint

# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "get_user_average_age" - kaip argumentą priims "users" sąrašą ir
# duoto sąrašo atveju grąžins visų vartotojų amžiaus vidurkį kaip skaičių,
# suapvalintą iki artimiausio sveikojo skaičiaus.

# 2. funkcija "get_users_names" - kaip argumentą priims sąrašą ir duoto sąrašo
# atveju grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka,
# pvz. ['Alex John', 'Ann Smith', ...].

import pprint
from xml.etree.ElementTree import indent

users = [
  { 'id': '1', 'name': 'John Smith', 'age': 20 },
  { 'id': '2', 'name': 'Ann Smith', 'age': 24 },
  { 'id': '3', 'name': 'Tom Jones', 'age': 31 },
  { 'id': '4', 'name': 'Rose Peterson', 'age': 17 },
  { 'id': '5', 'name': 'Alex John', 'age': 25 },
  { 'id': '6', 'name': 'Ronald Jones', 'age': 63 },
  { 'id': '7', 'name': 'Elton Smith', 'age': 16 },
  { 'id': '8', 'name': 'Simon Peterson', 'age': 30 },
  { 'id': '9', 'name': 'Daniel Cane', 'age': 51 },
]

# ******************************************************************************
# 1.function
# ******************************************************************************
def get_user_average_age(usrs):
    '''Returns users age average'''

    sum = 0
    headcount = len(usrs)
    for usr in usrs:
        sum += usr['age']
    return round(sum / headcount)

# ******************************************************************************
# 2.function testing
# ******************************************************************************
def get_users_names(usrs):
    '''Returns sorted users names list'''

    users_names = []
    for usr in usrs:
        users_names.append(usr['name']) 
    return sorted(users_names)

# ******************************************************************************
# Testing
# ******************************************************************************
pp = pprint.PrettyPrinter(indent=4)
separator = 79 * '*'

# ******************************************************************************
# 1.function testing
# ******************************************************************************
user_average_age = get_user_average_age(users)

print(f'\n{separator}\n1.function printing. Users age average: {user_average_age}')
print(separator)

# ******************************************************************************
# 2.function testing
# ******************************************************************************
users_names_res = get_users_names(users)

print(f'{separator}\n2.function printing. Users names:\n')
pp.pprint(users_names_res)
print(separator)