# Task 1 
# Make a generator to perform the same functionality of the iterator

import sys

print('Generator to replicate the Iterator')

def genTest(value):

    for x in value:

        yield(x*2)

result= genTest([1,3,5,7,9,11])

try:

    for x in result:

        print(x)

except StopIteration:

    sys.exit()

# Task 2 
# Overwrite default dunder methods & manipulate their default behavior
class DunderDemo:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return "Hi, "+ self.string
    def __add__(self, other):
        sum = self.string+self.string
        return sum

DundObj = DunderDemo(4)
# print(DundObj)
DundObj2 = DunderDemo(5)

print("Sum is ",DundObj2 + DundObj)

DundObj3 = DunderDemo("Welcome Thameem, This is Dunder Modified print")

print(DundObj3)


# Task 3
# A Decorator which times a function call using timeit start, a timer before function call, end the timer after function call print the time difference

from functools import wraps
import time

def TimeIT(func):

    @wraps(func)

    def timefuncwrap(*args, **kwargs):

        start_time = time.perf_counter()

        print(f"Start time is {start_time}")

        func(*args, **kwargs)

        end_time = time.perf_counter()

        print(f"end time is {end_time}")

        print(f"Total Time is {end_time-start_time}")

    return timefuncwrap

@TimeIT

def Hello():

    print('Hey.. There !!')

@TimeIT

def Hello_Question(name,question):

    print(f"Hello {name} , {question}")

Hello()

Hello_Question("Kate","Will you come with me for a Date?")