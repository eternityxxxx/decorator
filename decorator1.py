
import time

def timer(num = 10):
    def decorator(func):
        def wrap(*args, **kwargs):
            avg_time = 0
            for i in range(num):
                t0 = time.time()
                func(*args)
                t1 = time.time()
                avg_time += (t1 - t0)
            print("Среднее время выполнения функции -  %.5f " % avg_time)

        return wrap
    return decorator

@timer(num = 150)
def square(n):
    sum = 0
    for i in range(n):
        sum += i ** 2
square(10000)
