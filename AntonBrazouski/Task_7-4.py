import logging


def suppressor(func):
    def inner():
        try:
            func()
            logging.warning('\tNo exception this time!')
        except Exception:
            pass
    return inner


@suppressor
def bad_func():
    return 1 / 0


@suppressor
def good_func():
    return 1 / 1


bad_func()
good_func()
