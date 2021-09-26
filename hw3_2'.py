def pluz(a, b):
    try:
        return a+b
    except TypeError:
        try:
            return float(a)+float(b)
        except:
            print('cannot add number and unnumber')

print(pluz('1.5', 2))