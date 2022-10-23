from itertools import accumulate, count, cycle, chain, groupby, zip_longest, compress
from typing import Callable, Iterator

################################################################################################################
#
# chooser pattern using the itertools.cycle
# 
#   creates a generator which returnes an infinite number of booleans determined by 
#   the argument n with true/false determined by the predicate parameter
#   
#   
#
def chooser(n:int, predicate:Callable[[int], bool]) -> Iterator[bool] : return ( predicate(x) for x in cycle(range(n)) )
chooser3 = chooser(3, lambda x: x==0 ) # choose every 3rd element

# example of usage
process = lambda data: ( item for (choosen, item) in zip(chooser3, data) if choosen)
lst1 = (1,2,3,4,5,6,7,8,9,10,11,12)
print( tuple(  process( lst1 )  ) )


################################################################################################################
#
#  itertools.accumulate and itertools.count
#
#  calculate the factorial
#
#
# infinite factorial generator
#
factorialgen = accumulate( count(2), func = lambda x,a : x*a, initial = 1)
#
# finite factorial generator
#
def factorial(n:int) -> Iterator[int]:
    return accumulate(range(2,n+1), func=lambda x,a : x*a, initial = 1)

#
# example of usage of infinite
#
iterations = 100
while iterations >= 1:
    print(next(factorialgen))
    iterations -= 1
 
#   
# example of usage of finite
#
print(tuple(factorial(10))) 



######################################################################################################
#
# chain
# zip
# zip_longest    
# count
# enumerate
#
#
print(tuple(chain(       (1,2,3,4), (5,6,7)  )))
print(tuple(zip(         (1,2,3,4), (5,6,7)  )))
print(tuple(zip_longest( (1,2,3,4), (5,6,7)  )))
print(tuple(enumerate(  (10,20,30,40), start=1)))

