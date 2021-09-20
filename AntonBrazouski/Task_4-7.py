def xprod(alist, pos):
    result = 1
    for item in alist:
        if item != pos:
            result *= item
        else:
            continue

    return result        


def foo(alist):
    result = []

    for item in alist:
        result.append(xprod(alist, item))

    return result


test_list = [3, 2, 1]
print(test_list)
print(foo(test_list))

test_list = [1, 2, 3, 4, 5]
print(test_list)
print(foo(test_list))