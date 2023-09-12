"""General library for tests"""
from typing import List, Callable, Any


def postfunc(func) -> Callable:
    """Return func for call func"""

    def wrapper(*args, **kwargs) -> Callable:
        return lambda: func(*args, **kwargs)

    return wrapper


def reverted(rev_func: Callable | None) -> Callable:
    """Castomize test function for add to revers list reversed fuction"""

    def wrapper(func: Callable):
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)

        if rev_func is not None:
            setattr(wrap, "revers_func", postfunc(rev_func))
        return wrap

    return wrapper


def callr(rev_list: List[Callable], func: Callable, *args, **kwargs) -> Any:
    """Call function and add to list it's reverted func"""
    rev = getattr(func, "revers_func", None)
    result = func(*args, **kwargs)
    if rev is not None:
        rev_list.append(rev(*args, **kwargs))
    return result


def revert(rev_list: List[Callable]):
    """Call all revert functions from list"""
    for r in rev_list:
        r()
