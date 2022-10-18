from typing import Any, Callable, Iterable

#
# define the function as a "fist-class" function
#
# First-class functions means that the language treats functions as values
# that you can assign a function into a variable, pass it around etc. 
# It's seldom used when referring to a function, such as “a first-class function”.
#
#



# the sum-filter-transform from "high order reduction pattern" rewritten as 
# a "first-class" function
#
#  
class SumFilterTransform:
    # don't allow to add new members to the class other then the ones listed below
    __slots__ = [
        "transform",
        "filterf" ]

    def __init__(   self,
                    filterf:Callable[[Any], bool],
                    transform:Callable[[Any], Any]) -> None:
        self.filterf = filterf
        self.transform = transform

    def __call__(self, data:Iterable[Any]) -> float:
        return sum( self.transform(x) for x in data if self.filterf(x))


tpl = (1,2,3,4,5,6,None,7,8,9)

mySumFilterTransform = SumFilterTransform( lambda x: x != None, lambda x: 1)
print(mySumFilterTransform(tpl))




