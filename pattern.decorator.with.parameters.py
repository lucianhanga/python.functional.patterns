#
# the decorators with parameters are high-order functions which generate
# high-order functions and it has two internal function definitions
#
#
# this example contains an decorator with parameters which try to remove
# some bad characters from the strings which contain currency definitions
# defore applying other functions to them which might fail if they
# would not be integer values 
#

from typing import Callable, Optional, Any, TypeVar, Union, cast, Tuple
from functools import wraps



F_ = TypeVar("F_", bound = Callable[..., Any])

def clean_string_parameter( *character_list: str ) -> Callable[[F_], F_]:
    def create_decorator( func:F_ ) -> F_:
        @wraps(func)
        def wrap_clean_str(text:str) -> float:
            for ch in character_list:
                text = text.replace(ch,"")
            return func(text)
        return cast(F_, wrap_clean_str)
    return create_decorator



@clean_string_parameter(",", "$")
def currency(text:str) -> float:
    return float(text)


print(currency("1210.00"))
print(currency("1210.00$"))
print(currency("1,211.00"))
print(currency("1,210.00$"))
print(currency("$1210.00"))

