import time


def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("== start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func


def sleep_for_a_while():
    print("眠る")
    time.sleep(5)
    print("done sleeping")


sleep_for_a_while()
