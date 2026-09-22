# annotations 

from __future__ import annotations
from typing import Iterable
# def add(a: int, b: int) -> int:
#     return a + b

# name: str = "Enoch"
# count: int = 5
# prices: Iterable[float] = [0.4, 1.2, 3.5]

# def find_even(numbers: Iterable[int]) -> optional[int]:
#     for n in numbers:
#         if n%2 == 0:
#             return n
#         return None
    
#     print(find_even([1, 3, 5]))
#     print(find_even([1, 4, 7]))


#dataclass

from dataclasses import dataclass

# class User:
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight
        
# @dataclass

# class User:
#     height: float
#     weight: float
    
# Mike = User(6.2, 90.5)
# print(Mike)
# print(Mike.height)
        
        
from collections import Counter

ips = ['1.1.1.1', '2.2.2.2', '1.1.1.1']
count = Counter(ips)
print(count)
print(count.most_common)
