def is_palindrome(astring):
    if len(astring) <= 1:
        return True
    else:
        if astring[0] == astring[-1]:
            return is_palindrome(astring[1:-1])
        else:
            return False


print(is_palindrome('racecar'))
print(is_palindrome('nope'))
print(is_palindrome('madam'))