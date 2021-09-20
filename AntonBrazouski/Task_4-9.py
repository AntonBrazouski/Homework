from string import ascii_lowercase

test_strings = ["hello", "world", "python", ]


def test_1_1(*strings):
    result = []
    for ch in strings[0]:
        find = True
        for s in strings:
            if not ch in s:
                find = False
                break
            else:
                continue
        if find:
            result.append(ch)
        
    return sorted(set(result))  


def test_1_2(*strings):
    result = []
    for ch in ascii_lowercase:
        find = False
        for s in strings:
            if ch in s:
                find = True
                break
            else:
                continue
        if find:
            result.append(ch)
        
    return sorted(set(result))


def test_1_3(*strings):
    result = []

    for ch in ascii_lowercase:
        find = 0
        for s in strings:
            if ch in s:
                find += 1
            else:
                continue
        if find > 1:
            result.append(ch)
        
    return sorted(set(result))


def test_1_4(*strings):
    result = []

    for ch in ascii_lowercase:
        find = True
        for s in strings:
            if ch in s:
                find = False
                break
            else:
                continue
        if find:
            result.append(ch)
        
    return sorted(set(result))


print(test_1_1(*test_strings))    
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))
print(test_1_4(*test_strings))
