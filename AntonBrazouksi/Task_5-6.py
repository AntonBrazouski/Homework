cache = None


def call_once(func):
    
    def inner(*args):
        global cache
        if cache == None: cache = func(*args)
        
        return cache

    return inner


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))