def author(name): #author==decorator_maker
    def dec(f):
        def new_f(*args, **kwargs):
            new_f._author = name
            return f(*args, **kwargs)
        return new_f
    return dec

if __name__ == '__main__':
    @author('me')
    def x5(a):
        return 5*a

    x5(3)
    print('in main:', x5._author)
