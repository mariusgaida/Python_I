# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
# sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
# naminių gyvūnų visiškai, arba turi ir šunį, ir katę.

# 2. funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
# ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
# bet jau turi bent vieną naminį gyvūną.

import pprint
from xml.etree.ElementTree import indent

users = [
    { 'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True },
    { 'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False },
    { 'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True },
    { 'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False },
    { 'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False },
    { 'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True },
    { 'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False },
    { 'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True },
    { 'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False },
]
# ******************************************************************************
# 1.function
# ******************************************************************************
def filter_all_or_nothing_people(usrs):
    '''Returns owners having both or none pets'''

    all_or_nothing_people = []
    for usr in usrs:
        if usr['hasDog'] == usr['hasCat']:
            all_or_nothing_people.append(usr)
    return all_or_nothing_people

# ******************************************************************************
# 2.function
# ******************************************************************************
def filter_underaged_owners(usrs):
    '''Return underaged owners of pets'''
    
    underaged_owners = []
    for usr in usrs:
        if usr['age'] < 18 and (usr['hasDog'] or usr['hasCat']):
            underaged_owners.append(usr)
    return underaged_owners

# ******************************************************************************
# Testing
# ******************************************************************************
pp = pprint.PrettyPrinter(indent=0)
separator = 79 * '*'

# ******************************************************************************
# 1.function testing
# ******************************************************************************
all_nothing_usrs = filter_all_or_nothing_people(users)

print(f'\n{separator}\n1.function printing. Users having both or none pets:\n')
pp.pprint(all_nothing_usrs)
print(separator)

# ******************************************************************************
# 2.function testing
# ******************************************************************************
underaged_own = filter_underaged_owners(users)

print(f'{separator}\n2.function printing. Underaged owners of pets:\n')
pp.pprint(underaged_own)
print(separator)