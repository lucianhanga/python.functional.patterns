from typing import Callable

def enclosure_myfunction( param1: int, param2: int) -> Callable:
    __param1 = param1
    __param2 = param2
    def __myfunction():
        __param1 = __param1 - 1
        __param2 = __param2 - 1
        ret = f"{__param2} {__param1}"
        return ret

    return __myfunction

f1 = enclosure_myfunction(100, 1000)

print(f1())
print(f1())

