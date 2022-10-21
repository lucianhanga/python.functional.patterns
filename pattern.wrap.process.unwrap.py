
#
# wrap-process-unrwrap pattern
#
#


from typing import Iterable, Any

#
# the wrap will add aditional informations to the items which are used for processing
#
def wrap (data:Iterable) -> Iterable:
    return map(lambda x: (x[1], x), data)

#
# the unwrap remves the aditional data and returns the original item
#
def unwrap(item:Any) -> Any:
    return item[1]

#
# the process function
#
def process (data:Iterable) -> Any:
    return max(data)

# example of usage
dta = [("james",2), ("thomas", 4), ("andrei", 1), ("jason", 0)]

maxDta =    unwrap(
            process(
            wrap(dta)
            )
)

print(maxDta)

# this was a simpler case which could be implemented easier
# how to implement easier ?
print(  max(dta , key=lambda x: x[1]  ))

