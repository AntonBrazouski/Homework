def get_digits(inum):
    alist = []
    istr = str(inum)
    for ch in istr:
        alist.append(int(ch))

    result = tuple(alist)

    return result



print(get_digits(87178291199))