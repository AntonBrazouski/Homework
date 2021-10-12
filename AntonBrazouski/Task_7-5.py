class Error(Exception):
    """ Base """
    pass


class ValueNotEvenError(Error):
    pass


class ValueLessThanTwo(Error):
    pass


def func(num):
    """ check for even and >2  """
    try:
        if num % 2 != 0:
            raise ValueNotEvenError
        elif num <= 2:
            raise ValueLessThanTwo
    except ValueNotEvenError:
        print(f'{num} is odd')
    except ValueLessThanTwo:
        print(f'{num} is less than two')


func(100)
func(11)
func(0)
