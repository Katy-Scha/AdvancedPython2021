import time

def timeit(n=1): #timeit==decorator_maker
    def dec(f):
        def new_f(*args, **kwargs):
            sum_time = 0
            sum_time_sqrt = 0
            for i in range(n):
                time_start = time.time()
                t = f(*args, **kwargs)
                time_end = time.time()
                sum_time += (time_end-time_start)
                sum_time_sqrt += (time_end - time_start)**2
            print('Execution time: %.6f s +- %.6f s, from %d runs' % (sum_time/n, (sum_time_sqrt)/n - (sum_time/n)**2, n))
            return t
        return new_f
    return dec

if __name__ == '__main__':
    @timeit(3)
    def f(a):
        time.sleep(1.0)
        return 5 * a

    print('in main:', f(3))