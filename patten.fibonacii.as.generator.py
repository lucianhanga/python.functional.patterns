
from typing import Iterable, Iterator, Optional
    
class FibGen:
    def __init__(self, end:Optional[int] = None) -> None:
        self.n_2 = None
        self.n_1 = None
        self.end = end
    def __iter__(self) -> Iterator[int]:
        return self
    def __next__(self) -> Iterator[int]:
        if not self.n_2: 
            self.n_2 = 1
            return self.n_2 
        if not self.n_1:
            self.n_1 = 1
            return self.n_1
        res = self.n_1 + self.n_2
        self.n_2 = self.n_1
        self.n_1 = res
        if self.end and res > self.end:
            raise StopIteration
        return res

# unlimited fibgen 
fibgen = FibGen()
print(tuple(  next(fibgen) for _ in range(0,100)))

# limited fibgen. stop when max value reached
fibgen = FibGen(1000)
print(tuple(fibgen))
