def replacer(str):
    result = ''

    op = ''
    for ch in str:
        if ch == '\"':
            op = '\''
        elif ch == '\'':
            op = '\"'
        else:
            op = ch
        result += op

    return result 
           
test_str = "The \'correct\' \"method\"."       

print(test_str)
print(replacer(test_str))