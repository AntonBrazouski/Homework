def fib(n):
    result = 0
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    
    return result


def endless_fib_gen():
    i = 0
    while True:
        yield fib(i)
        i = i+1


gen = endless_fib_gen()
while True:
    print(next(gen))


    