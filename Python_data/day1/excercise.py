from Checks.checker import checks

# insert a string



@checks(str)
def string_checker(value,*args):
    ans = value
    return ans

@checks(int)
def integer_checker(value,*args):
    ans = value
    return ans


@checks(bool)
def boolean_checker(value,*args):
    ans = value
    return ans


@checks(list)
def List_checker(value,*args):
    ans = value
    return ans


@checks(dict)
def dictionary_checker(value,*args):
    ans = value
    return ans


@checks(tuple)
def tuple_checker(value,*args):
    ans = value
    return ans


@checks(set)
def set_checker(value,*args):
    ans = value
    return ans



set_checker(12,3,4)