from functools import wraps


def checks(item):
    def inner(func):
        @wraps(func)
        def wrapper(value=None,*args):
            if value == None:
                print(func.__name__, 'has no value')
                return 
            print('*' * 10)
            ans = func(value)
            if item != type(ans):
                print(ans, type(ans))
                print('Your answer is  incorrect')
            else:
                print('Test passed')
            print('*' * 10)
        return wrapper
    return inner
