from ast import And
from typing import Callable, Any, Iterator, Optional

#
# very generic definition of the pattern 
#
class NullAware:
    def __init__(self, function:Callable[[Any], Any]) -> None:
        self.function = function
        
    def __call__(self, item:Optional[Any]) -> Optional[Any]:
        return self.function(item) if item else None
        # the return can be written also like
        # return None if item is None else function(item)


# usage example
#
safeSquareF = NullAware(lambda x: x*x)
print(tuple(map(safeSquareF, (1,2,None,4,None,6))))
