# 
# JOIN ON WHERE  SQL pattern  
#
#

from math import fabs
from operator import truediv
from typing import Callable, Iterable, TypeVar, Tuple, NamedTuple
from itertools import product

JT1_ = TypeVar("JT1_")
JT2_ = TypeVar("JT2_")


class Table1(NamedTuple):
    Id:int
    Name:str
    Adress:str

class Table2(NamedTuple):
    TransactionId:int
    SenderId:int
    ReceiverId:int
    Amount:float
    
dataTable1 = (
    Table1(1, "James", "Downingstr.10, 80831, London"),
    Table1(2, "Thomas", "Bayerbrunnerstr. 12, 82332, Munich"),
    Table1(3, "Ann", "Rowostr. 2233, Los Angeles"),
    Table1(4, "Jana", "Toledo, 12345, Spain"),
)    

dataTable2 = (
   Table2( 1, 1, 2, 123.00),
   Table2( 2, 1, 3, 99.00),
   Table2( 3, 1, 4, 21.00), 
   Table2( 4, 1, 2, 44.00),
   Table2( 5, 1, 2, 12.00), 
   Table2( 6, 1, 4, 20.00), 
   Table2( 7, 1, 4, 16.00), 
   Table2( 8, 2, 3, 32.00), 
   Table2( 9, 2, 4, 40.00), 
   Table2(10, 2, 4, 22.00), 
   Table2(11, 3, 1, 32.00), 
   Table2(12, 3, 2, 42.00), 
   Table2(13, 3, 4, 52.00) 
)

def join( table1: Iterable[JT1_], table2: Iterable[JT2_], on: Callable[[ Tuple[JT1_, JT2_]], bool]) -> Iterable[ Tuple[JT1_, JT2_]]:
    return filter(  on, product( table1, table2 ) )


def on_idt1_equal_senderidt2( joinpair:Tuple[JT1_, JT2_] ) -> bool:
    (itemt1, itemt2) = joinpair
    return itemt1.Id == itemt2.SenderId


where_name_is = lambda name, data : filter( lambda pair: pair[0].Name == name , data)
amount_send = lambda data : (x[1].Amount for x in data )

print ( sum(
        amount_send(
        where_name_is( "James",
        join( dataTable1, dataTable2, on_idt1_equal_senderidt2)))) )
