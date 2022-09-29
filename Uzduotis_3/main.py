# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

import pprint
from xml.etree.ElementTree import indent

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

# ******************************************************************************
# function
# ******************************************************************************

def get_dict_values(vehicle):
  '''Return dict's values list'''
  values = []
  for v in vehicle.values():
    values.append(v)
  return values

# ******************************************************************************
# Testing
# ******************************************************************************
pp = pprint.PrettyPrinter(indent=4)
separator = 79 * '*'

# ******************************************************************************
# function testing
# ******************************************************************************
val = get_dict_values(audi)

print(f'\n{separator}\nfunction printing. All values:\n')
pp.pprint(val)
print(separator)