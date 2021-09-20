def get_shortest_word(astring):
    """ Work backwards! """
  
    result = None 
    for word in astring.split():
        op = word
        for ch in op:
            if ch in ['!', '?', ' ', '\n', '\t']:
                op = op.replace(ch, '')

        if result == None:
            result = op
        elif len(result) < len(op):
            result = op
        else:
            continue

    return result


print(get_shortest_word('Python is simple and effective!'))
print(get_shortest_word('Any pythonista like namespaces a lot.'))