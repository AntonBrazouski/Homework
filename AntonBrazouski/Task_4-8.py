def get_pairs(alist):
    if len(alist) <= 1:
        return None
    
    result = []

    pre = None
    for item in alist:
        if pre == None:
            pre = item
        else:
            result.append((pre, item))
            pre = item

    return result


test_list = [1, 2, 3, 8, 9]
print(test_list)
print(get_pairs(test_list))

test_list = ['need', 'to', 'sleep', 'more']
print(test_list)
print(get_pairs(test_list))

test_list = [1]
print(test_list)
print(get_pairs(test_list))
