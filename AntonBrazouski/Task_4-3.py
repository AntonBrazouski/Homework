def str_split_sep(astr,sep=' '):
    result = []

    ops = ''
    for ch in astr:
        if ch == sep:
            result.append(ops)
            ops = ''
        else:
            ops += ch
    result.append(ops)

    return result


test_str = 'Split clone is ready!'
test_str_comma = 'Comma separated, as well'

print(str_split_sep(test_str))
print(str_split_sep(test_str_comma, ','))




