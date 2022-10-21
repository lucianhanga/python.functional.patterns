from itertools import cycle
from random import randrange
from typing import Any, Iterable

#rules definitions - generators
any = cycle(range(0))
every5th = cycle(range(5))
every7th = cycle(range(7))
def randseq(limit:int) -> int:
    while True:
        yield randrange(limit)
randrule = randseq(4) 
       
# choose generator
choose = lambda rule: ( x==0 for x in rule)

# generator which applies the choose rule for the collection
def choose_by_rule( data:Iterable[Any], rule:Iterable[int] ) -> Iterable[Any]:
    return (item for (choosen, item) in zip(choose(rule), data) if choosen)

# testing
print( tuple(choose_by_rule((1,2,3,4,5,6,7,8,9,0), randrule))  )


