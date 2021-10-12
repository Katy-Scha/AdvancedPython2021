class Book:
    def __init__(self, name, author=None, year=None):
        self.name = name
        #self.author = author
        self.author = frozenset(author.split(', ')) #чтобы порядок авторов менять можно было, a frozen - чтоб хешировалось
        self.year = year
    def __repr__(self):
        return (f'{self.author}, {self.name}, год изд.{self.year}')
    def __eq__(self, other):
        if self.author==other.author and self.name==other.name:
            return True
        return False
    def __ne__(self, other):
        return not (self == other)
    def __hash__(self):    #иначе на dict-полку не поставишь
        return hash((self.name, self.author))

class Library:
    def __init__(self, name):
        self.name = name
        self.shelf = dict()
    def __repr__(self):
        return (f'{self.name} (число книг: {sum(self.shelf.values())})')
    def __add__(self, book):
        if type(book)!=Book:
            raise TypeError
        new_lib = Library(self.name)
        new_lib.shelf = self.shelf
        try:
            new_lib.shelf[book] += 1
        except:
            new_lib.shelf[book] = 1
        return new_lib
    def __radd__(self, book):
        if type(book)!=Book:
            raise TypeError
        new_lib = Library(self.name)
        new_lib.shelf = self.shelf
        try:
            new_lib.shelf[book] += 1
        except:
            new_lib.shelf[book] = 1
        return new_lib
    def __eq__(self, other):
        return True if self.shelf==other.shelf else False
    def __gt__(self, other):
        return True if sum(self.shelf.values())>sum(other.shelf.values()) else False

if __name__ == '__main__':
    biblio1 = Library(name="Библиотека МФТИ")
    biblio2 = Library(name="Ленинка")
    print(f'0: {biblio1} > {biblio2}:', biblio1 > biblio2)
    print(f'0: {biblio1} = {biblio2}:', biblio1 == biblio2)
    book = Book(
        name="Теоретическая физика. Том 1. Механика",
        author="Ландау Л.Д., Лифшиц Е.М.",
        year=2004
    )
    book2 = Book(
        name="Теоретическая физика. Том 1. Механика",
        author="Лифшиц Е.М., Ландау Л.Д."
    )
    #print(book2==book)
    biblio1 = book +biblio1
    biblio2 = biblio2 + book
    print(f'lib: {biblio1}, with books: {biblio1.shelf}')
    print(f'only Landavsh: {biblio1} > {biblio2}:', biblio1 > biblio2)
    print(f'only Landavsh: {biblio1} = {biblio2}:', biblio1 == biblio2)
    biblio1 += book
    print(f'2 and 1: {biblio1} > {biblio2}:', biblio1 > biblio2)
    print(f'2 and 1: {biblio1} = {biblio2}:', biblio1 == biblio2)
    print('repr:', repr(biblio1), '\n str:', str(biblio1))