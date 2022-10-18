#
# high order function - reduction patterns
#


from typing import Callable, Iterable, Any, Iterator, TypeVar


# sum_tranform
#
#
# apply to each element of the collection/iterable the function f() and sum the results
#  
#   input parameters:
#     tranformation - a function which is applied to each element of the collection/iterable 
#                     and generates a value. All the generated values are added using sum() 
#                     reduction function.
#     data - the iterable collection which could be list, tuple, or an interator  
#
def sum_transform( 
            transformation:Callable[[Any], float], 
            data:Iterable[Any]) -> float:
     return sum( transformation(x) for x in data)

#
# usage on diferent cathegories of iteratables
#
lst = [1,2,3,4,5,6,7,8,9]
tpl = (0,2,4,6,8,10)
myGenerator = (x for x in range(0,100))
def myGenerator2(begin:int, end:int) -> Iterator[int]:
    i = begin
    while( i<end):
        yield i
        i+=1

print("sum_transform() usage: ")
lstCount = sum_transform( lambda x: 1, lst)
print(lstCount)
tplCount = sum_transform( lambda x: 1, tpl)
print(tplCount)
myGeneratorCount = sum_transform(lambda x: 1, myGenerator)
print(myGeneratorCount)
myGenerator2Count = sum_transform(lambda x: 1, myGenerator2(1,5))
print(myGenerator2Count)


# sum_filter_transform
#
#
# apply the filter function to collection/iterable the function, then to the remaining iterables
# the transformation function and apply sum
#  
#   input parameters:
#
#     filterf    - the filter function which is applied to the collection/iterable befor the transformation
#     transform - a function which is applied to each element of the collection/iterable and generates a value.
#                 all the generated values are added using sum() reduction function
#     data      - the iterable collection which could be list, tuple, or an interator  
#
def sum_filter_transform( 
                            filterf: Callable[[Any], Any], 
                            transform:Callable[[Any], bool], 
                            data:Iterable[Any]) -> float:
    return sum (transform(x) for x in data if filterf(x) )


print("sum_filter_transform() usage: ")
lstCount = sum_filter_transform( lambda x: x%2 == 0, lambda x: 1, lst)
print(lstCount)
tplCount = sum_filter_transform( lambda x: x%2 == 0, lambda x: 1, tpl)
print(tplCount)
myGenerator = (x for x in range(0,100)) # this one has to be redefined because an iterator can be used only ONCE
myGeneratorCount = sum_filter_transform(lambda x: x%2 == 0, lambda x: 1, myGenerator)
print(myGeneratorCount)
myGenerator2Count = sum_filter_transform(lambda x: x%2 == 0, lambda x: 1, myGenerator2(1,5))
print(myGenerator2Count)

#
# this function can be also replaced by
#
print("sum_filter_transform() replacement: ")
lstCount =  sum(
            map( lambda x: 1,
            filter( lambda x: x%2 ==0,
            lst ) ) )
print(lstCount)