
from email.generator import Generator
from typing import Iterable, Iterator, Optional

#
# FibGen - First Class Function Generator
#
#    
class FibGen:
    def __init__(self, elements:Optional[int] = None) -> None:
        self.n_2 = 1
        self.n_1 = 1
        self.counter = 0 # need it to know when to return 1,1
        self.elements = elements
    def __iter__(self) -> Iterator[int]:
        return self
    def __next__(self) -> Iterator[int]:
        if self.elements and self.counter >= self.elements:
            raise StopIteration
        self.counter += 1
        if self.counter <= 2:
            return 1
        res = self.n_1 + self.n_2
        self.n_2 = self.n_1
        self.n_1 = res
        return res

# unlimited fibgen 
fibgen = FibGen()
print(tuple(  next(fibgen) for _ in range(0,10)))

# limited fibgen. stop when max value reached
fibgen = FibGen(10)
print(tuple(fibgen)) 


#
# fibonacii_gen - generator
#
def fibonacii_gen(elements:Optional[int]=None) -> Iterator[int]:
    yield 1
    if elements is not None : elements -= 1
    if elements is not None and elements <= 0: return 
    yield 1
    if elements is not None : elements -= 1
    if elements is not None and elements <= 0: return 
    n_2 = 1
    n_1 = 1
    while True:
        res = n_2 + n_1
        yield res
        if elements is not None: elements -= 1
        if elements is not None and elements <= 0: return
        n_2 = n_1
        n_1 = res
    return 

# unlimited fibonacii_gen
fibgen2 = fibonacii_gen()
print(tuple( next(fibgen2) for _ in range(0,10)))

# limited fibgen. stop when max value reached
fibgen2 = fibonacii_gen(10)
print(tuple(fibgen2)) 

