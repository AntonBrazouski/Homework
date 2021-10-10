from contextlib import contextmanager
import time


@contextmanager
def log_exec():
    resourse = open('log.txt', 'a')
    start = time.time()
    try:
        yield resourse

    finally:
        finish = time.time()
        duration  = finish - start
        print(duration)
        resourse.write(str(duration)+'\n') 
        resourse.close()


with log_exec() as log:
    # do something
    calc = 0
    for i in range(100):
        for j in range(100):
            calc = (i**(i - j+101))

