def split_by_index(str, idxs):
    result = []
    op = ''
    for idx, ch in enumerate(str):
        if idx in idxs:
            result.append(op)
            op = ch
        else:
            op += ch
    result.append(op)  
                     
    return result 


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))