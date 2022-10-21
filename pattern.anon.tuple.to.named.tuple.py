#
# 
# The idea of Wrap-Unwrap design patterns that allow us to work with anonymous and named tuples. 
# The point of this kind of design is to use immutable objects that wrap other immutable objects 
# instead of mutable instance variables.
#
# 

from typing import Callable, Iterator, NamedTuple, Tuple

dta = ( (1,2), (3,4), (5,6), (7,8)) 


class Coordinates(NamedTuple):
    x:float
    y:float
#
# returns the whole collection 
#    
AnonCoordiantesIterator = Iterator[Tuple[float, float]]
toCoordinates:Callable[[AnonCoordiantesIterator], Tuple[Coordinates]] = lambda data: tuple( Coordinates(*item) for item in data)
# usage example
print(toCoordinates(dta))

#
# returns an iterator 
#
toCoordinatesIterator:Callable[[AnonCoordiantesIterator], Tuple[Coordinates]] = lambda data: ( Coordinates(*item) for item in data)
# usage example
print(tuple(toCoordinates(dta)))

