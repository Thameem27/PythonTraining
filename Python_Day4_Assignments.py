# Day 4
# Task 1
class TravClass:
    """Class to implement an iterator
    """

    def __init__(self, string):
        self.string = string
        print('input is ', self.string)
        self.start = 0
        self.index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.index:
            nextitrval = self.string[self.start]
            self.start += 2
            return nextitrval
        else:
            raise StopIteration


# create an object
strings = TravClass('hello')

# create an iterable from the object
i = iter(strings)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# ====================================================
# Task 2
# Create a CSV File with names and experience
import csv
path = input("Enter the path where you want the file to be created ")+"\\"
with open(path+"Day4_Data_File.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Employee Name', 'Years of Experience'])
    writer.writerow(['Bob', 10])
    writer.writerow(['Michelle', 5])
    writer.writerow(['Bobby', 12])
    writer.writerow(['Bebo', 2])
# ====================================================
# Task 3
# Print all py file names recursively in current and subdirectories
import glob
path = input("Enter the path where you want the files to be picked ")
files = [f for f in glob.glob(path+ "**/*.py", recursive=True)]

for f in files:
    print('Files are ', f)
# ====================================================

# Task 4
# Print all the command line arguments passed on to the file
import sys

if __name__ == "__main__":
    print(f"Arguments Passed Totally are: {len(sys.argv)}")
    for i, argument in enumerate(sys.argv):
        print(f"Argument {i:>8}: {argument}")
# ====================================================
# Task 5
import random
print("Welcome, To Guess The Number Game")
attempt = int(input("Choose the number of attempts between 1-10 in which you can guess the Number => "))
constant = random.randint(1, 100)
i = 1
while i <= attempt:
    try:
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
            print("Yay !! You Guessed it right. The Number is ", constant)
            break
        i += 1
    except ValueError:
        print('error')
    if i > attempt:
        raise ValueError("Alas !! Your attempts are exhausted. The Number is ", constant)

# ====================================================

# Task 6
try:
    inputValue1 = int(input("Enter a number : "))
    inputValue2 = input("Enter a string : ")
    print("Square root of Your number input is ", inputValue1*inputValue1)
    print("Upper case of your string is ", inputValue2.upper())
    print("Square root of Your number input is "+ inputValue1)
except ValueError:
    print("Your input was faulty")
except TypeError:
    print("Your Data Type was faulty")
