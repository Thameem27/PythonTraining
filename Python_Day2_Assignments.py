#First task, Nineth Task with While Loop with & without getting invoked
import random
print("Welcome, To the Guess The Number Game")
attempt = int(input("Choose the number of attempts between 1-10 in which you can guess the Number => "))
constant = random.randint(1, 100)
i = 1
while i <= attempt:
    random_num = int(input('Guess the Number : '))
    if random_num < constant and (random_num > constant-10):
        print("Your number Was close to, but Less than the generated Number ")
    elif random_num < constant:
        print("Your number Was less than the generated Number ")
    elif random_num > constant and (random_num < constant+10):
        print("Your number Was close to, but Greater than the generated Number ")
    elif random_num > constant:
        print("Your number Was Greater than the generated Number ")
    else:
        print("Yay !! You Guessed it right. The Number is "+str(constant))
        break
    i += 1
else:
    print("Alas !! You could not guess the number. The Number is " + str(constant))

# Task 2

"""
Print list elements along with their position
"""
charList = ['Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Mumbai', 'Noida', 'Kochi', 'Hyderabad']

for index, City in enumerate(charList):
    print(f"{index} : {City}")

# Task 3
"""
Loop over a Dictionary and print the value and key in a readable format
"""
empDict = {'Company': 'Apple', 'Designation': 'Senior Consultant', 'Department': 'Delivery Operations'}
for key, value in empDict.items():
    print("Value " + value, " Belongs to " + key)

# Task 4
"""
Code of Else clause being invoked in a while loop and the opposite too.
"""
# Else clause invoked
num = int(input("Enter your number: "))
while num < 6:
    print("Number : " + num)
    num += 1
else:
    print("Please enter a number less than 6")

# Else clause not invoked
num = int(input("Enter your number: "))
while num < 8:
    print("Num : " + num)
    num += 1
    if num == 8:
      break
else:
    print("Enter a number less than 8")
    
    
# Task 5
# """
# Build a function that accepts two numbers and returns their addition
# """


# type hints
def add_num(num1: int, num2: int):
    """Adding 2 numbers based on user i/o"""  # docstring
    return num1 + num2


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Sum of the two numbers is "+str(add_num(n1, n2)))

# Task 6

"""

A function that accepts any number of args and prints them one per line

"""


def national_anthem(*args):
    for word_list in args:
        print(word_list)


national_anthem("Jana", "Gana", "Mana", "Adhinayaka", "Jayahe")

# Task 7
"""

A function that accepts any number of kwargs and prints the number of args & its content

"""


def keywordargs(**kwargs):
    print(len(kwargs))
    for key, value in kwargs.items():
        print(f"Key is {key} => Value is {value}")


keywordargs(Movie="Robo", Hero="Rajinikanth", Heroine="Aishwarya Rai")

# Task 8

"""

A function that accepts any number of args/kwargs and prints the count of both

"""


def argsandkeywordargs(*args, **kwargs):
    print("Count of Args/Keyword Args is "+str(len(args) + len(kwargs)))
    print("Count of Args is " + str(len(args)))
    print("Count of Keyword Args is " + str(len(kwargs)))


argsandkeywordargs("January", "February", "March", "April", Nation="USA", Capital="Washington", President="Joe Biden")


# Task 10

"""

List comprehension to get square values of odd number from the list provided

"""

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

numbersquare = [number**2 for number in numList if number % 2 == 1]

for oddnumbersq in numbersquare:
    print("Odd Square Value is "+str(oddnumbersq))


# PEP 20 Favourite Line
# If the implementation is hard to explain, it's a bad idea.

# Task 11
""" Lambda Expression Demo """
total = int(input("Enter a Total : "))
count = int(input("Enter a Count : "))

print(" Below is the average of these ")

average = lambda total, count : total/count

print(average(total, count))
