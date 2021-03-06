
import time

class Decorator():
    """
        Класс используется как декоратор

        count - кол-во испытаний для определения среднего времени работы алоритма
    """
    def __init__(self, count):
        self.count = count


    def __call__(self, func):
        def wrap(*args, **kwargs):
            avg_time = 0
            for i in range(self.count):
                t0 = time.time()
                func(*args)
                t1 = time.time()
                avg_time += t1 - t0
            print("Время выполнения - %.5f" % avg_time)
        return wrap

@Decorator(count = 100)
def square(n):
    """
        Функция прсото считает сумму квадратов в заданном диапозоне
    """
    sum = 0
    for i in range(n):
        sum += i ** 2

square(10000)
