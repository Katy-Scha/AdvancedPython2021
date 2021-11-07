# среднее, дисперсию, количество элементов
def counter():
    summ = 0
    count = 0
    sq_sum = 0
    while True:
        a = yield
        count += 1
        summ += a
        sq_sum += a*a
        mean = summ/count
        sq_mean = sq_sum/count
        print(f'mean = {mean}, dispersion = {sq_mean - mean**2} of {count} numbers')

if __name__=='__main__':
    coroutine = counter()
    next(coroutine)
    for i in range(5):
        a = float(input())
        coroutine.send(a)