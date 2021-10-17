def endless_generator():
    i = 0
    while True:
        i += 1
        if i % 2 == 0:
            continue
        else:
            yield i 


gen = endless_generator()


while True:
    print(next(gen))