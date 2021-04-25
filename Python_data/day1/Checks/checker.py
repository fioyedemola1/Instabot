from functools import wraps


def checks(item=None):
    def inner(func):
        @wraps(func)
        def wrapper(value,*args, **kwargs):
            print('*' * 10)
            ans = func(value, *args, **kwargs)
            if item != type(ans):
                print('Your answer is  incorrect')
            else:
                print('Test passed')
            print('*' * 10)
        return wrapper
    return inner
