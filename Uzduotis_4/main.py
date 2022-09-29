# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

# ******************************************************************************
# Class
# ******************************************************************************
class Movie:
    '''A class to represent a movie'''

    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        '''Returns either True if budget is over 100_000_000 or False if under'''

        return bool(self.budget > 100_000_000)
    
    def __str__(self):
        '''Helps to print class instances'''

        return f'Title: {self.title},\
                director: {self.director},\
                budget: {self.budget}'

# ******************************************************************************
# Class instances
# ******************************************************************************
Movie1 = Movie('First Movie', 'First Movie Director', 10_000_000)
Movie2 = Movie('Second Movie', 'Second Movie Director', 101_000_000)

# ******************************************************************************
# Testing
# ******************************************************************************
separator = 79 * '*'

# ******************************************************************************
# Instances testing
# ******************************************************************************
print(f'\n{separator}\nInstances: \n\n{Movie1}\n{Movie2}')

# ******************************************************************************
# Method testing
# ******************************************************************************
print(f'{separator}\nTesting Movie method:\n')
print(f'Movie budget: {Movie1.budget}\nMovie method responce: {Movie1.was_expensive()}\n')
print(f'Movie budget: {Movie2.budget}\nMovie method responce: {Movie2.was_expensive()}\n')
print(separator)