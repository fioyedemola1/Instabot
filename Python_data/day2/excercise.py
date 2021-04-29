from Checks.checker import checks
from typing import Optional,Any


@checks(list)
def List_checker(value: Optional[Any]=None ,*args):
    ans = value
    return ans


@checks(dict)
def dictionary_checker(value: Optional[Any]= None,*args):
    ans = value
    return ans


@checks(tuple)
def tuple_checker(value: Optional[Any],*args):
    ans = value
    return ans


@checks(set)
def set_checker(value: Optional[Any] = None,*args):
    ans = value
    return ans




    


if __name__ == '__main__':
    List_checker()               #list
    dictionary_checker()          # Dictionary
    tuple_checker()               #tuple
    set_checker()                 #set
