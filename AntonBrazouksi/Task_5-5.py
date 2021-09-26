last_result = None


def remember_result(func):

    def inner(*args):
        global last_result 
        print(f"Last result = {last_result}")
        last_result = func(*args)

    return inner


@remember_result
def sum_list(*args):  
    result = ""
    if isinstance(args[0], int):
        result = 0

    for item in args:
        result += item
    
    print(f"Current result = '{result}'")

    return result

sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)