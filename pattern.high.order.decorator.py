#
# define a high-order function which behaves like a decorator
#
# this example checks the paramter. if the parameter is None it returns
# imediatelly None. If the parameter is not None call the original function
#
#

from typing import Callable, Optional, TypeVar, Any, cast
from functools import wraps
import logging

F = TypeVar('F' , bound=Callable[..., Any])

def nullsafe ( func: F ) -> F:    
    @wraps(func) # get the __name__ and __doc__ from the func
    def nullsafe_wrapper( arg: Optional[Any] ) -> Optional[Any]:
        return None if arg is None else func(arg)
    return cast(F, nullsafe_wrapper)


# usage example
# if the decorator is not used the following error will aper:
#
#  TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
#
@nullsafe 
def pow2( arg:Any ) -> Any:
    return arg*arg

# using the decorator on a lambda function
div2 = nullsafe(lambda x: x//2)

print(tuple(map(pow2, (1,2,None,3,4,None,5))))
print(tuple(map(div2, (1,2,None,3,4,None,5))))



