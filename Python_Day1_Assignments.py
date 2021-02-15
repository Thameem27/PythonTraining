# First Task
names = ["john", "jake", "jack", "george", "jenny", "jason", "john"]
temp_name = []
for i in names:
    if i not in temp_name:
        temp_name.append(i)

for j in temp_name:
    if len(j) < 5 and 'e' not in j:
        print("Unique Strings whose length is less than 5 and doesnt contain letter e " + j)

# First Task with Set
names = {"john", "jake", "jack", "george", "jenny", "jason", "john"} 
for j in names:
    if len(j) < 5 and 'e' not in j:
        print("Unique Strings whose length is less than 5 and doesnt contain letter e " + j)

# Second Task
character = 'python'
print('c'+character[1:])



# Third task
random_num = int(input('Enter a number of your choice : '))
constant = 50
if random_num < constant:
    print("Your number is less than "+str(constant))
elif random_num > constant:
    print("Your number is greater than "+str(constant))
else:
    print("Your number is equal to "+str(constant))

# Fourth Task
Total_list = {"name": "python", "ext": "py", "creator": "guido"}
key_list = list(Total_list.keys())
for key_val in key_list:
    print("Key is "+key_val+". Value is "+Total_list[key_val])

# FizzBuzz Program
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
