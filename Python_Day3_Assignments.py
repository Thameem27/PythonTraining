# Day 3 of Python Training
# Task 1.1
intDict = {x: x**2 for x in list(range(1, 10))}
print(intDict)

# Task 1.2
intDict = {x: x**2 for x in list(range(1, 10))}
print(list(intDict.values()))

# Task 2.1
intSet = {x: x**2 for x in set(list([1, 2, 3, 2, 5, 7, 3, 5, 9]))}
print(set(intSet.values()))

# 3.1
tup = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
output = [item for t in tup if t[1] >= t[2] for item in t[0:2]]
# First way of converting a list to dict
itr = iter(output)
propBalDict = dict(zip(itr, itr))
print(f"Question 3.1 ", propBalDict)
# 3.2 Convert to set
print(f"Question 3.2 ", set([item for t in tup for item in t[1:2]]))

# 3.3 Print List 
print(f"Question 3.3 ", list([item for t in tup for item in t[0:1]]))

# 3.4 => Alternate way of handling Dictionary
balNeeded = {t[0]: t[2]-t[1] for t in tup if t[1] < t[2] for item in t[0:2]}
print(f"Question 3.4 ", balNeeded)

# 3.5
print(f"Question 3.5 ", [item[0:2] for item in tup if item[1] >= 0])
# print(output)

# Task 4
class Developer:



     def __init__(self, devlang):

         self.devlang = ["C","SQL","ReactJS","GoLang","Python","PostgreSQL"]
 
     def code(self,language): 

            if(language in list(map(lambda x: x, self.devlang ))): 

                  print(f"code {language} is present in the list ")

            else:

                 print(f"Code {language} is not in the list")          



     def resume(self):

        print(self.devlang) 

        

language = input("Please enter the coding language: ")

s = Developer("")

s.code(language)

# Task 5
import math as m


class FactorialClass:
    def __init__(self):
        self.finalres = []

    def factfunc(self, numbers):
        for num in numbers:
            if num >= 0:
                self.finalres.append(m.factorial(num))
            else:
                self.finalres.append('No factorial for Negative numbers')
        return self.finalres


factObject = FactorialClass()
print(factObject.factfunc([-1, 0, 1, 2, 3, 4, 5, 6]))


# Task 6
from math import ceil as c
from math import floor as f
num = float(input("Enter a decimal value : "))
print("Its Ceil value is ", c(num))
print("Its Floor value is ", f(num))

# Task 7

# Module Name : moduleThameem
# Function : sayhi
# File saved as moduleThameem.py
def sayhi(name):
    print("Hey There "+name)


import moduleThameem as mT


print(mT.sayhi('Bob'))

# Below tasks couldnt be completed due to lack of time. I'll get them done and resubmit.
# create a module that prints "I'm running" only when it's ran as a script (not as a module using import)
# use python to open another python source file and print the contents