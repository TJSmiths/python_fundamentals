# #
# # Activity 1
# #

# This will create a list in memory and print hello world for every entry in the list
for i in range(13):
    print("hello world")

#
# Activity 2
#

# Create the variable num1 as a list with numbers from 1 to 12
num1 = range(1,13)
# Loop through the the num1 range
for x in num1:
    # Create the variable num2 as a list with numbers from 1 to 12
    num2 = range(1,13)
    # Loop through num2 range and for each, multiply by each entry in the num1 range
    for y in num2:
        math = x * y
        # The position of this print is important!! Moving it back will only return the last value in both ranges
        print(math)
    # The position of this print is also important, as underneath the num2 for loop will create a space between every number instead of each block of numbers
    print("")

#
# Activity 3
#

# Set variable for value of launch to count backwards from
launch = 10

# Create while loop - when launch variable is not 0, print launch and subtract one
while launch != 0:
    print(launch)
    launch -= 1
# Once launch variable is 0, print blastoff
else:
    print("Blastoff!")

#
# Activity 4
#

# Create variable for the list called imposters
imposters = ["cat","dog","dog","bird","elephant","Jim","dog"]
# Create empty list in order to append later
dogs = []

# Begin loop through imposters variable and if the item in the list is dog, append the empty dogs list
for i in imposters:
    if i == "dog":
        dogs.append("dog")

# f string has been used on this print for simplicity, but inside it is a check for the length of the list from the dogs variable
print(f"We have {len(dogs)} dogs at our shelter")

#
# Activity 5
#

# Create two lists with items in them
shopping_list = ["cheese", "beans", "crisps", "milk", "apples"]
at_the_shops = ["pears", "jam", "cheese", "apples", "bread", "tuna", "crisps"]

# Loop through the shopping list and for each item check if it is in the at_the_shops list
for item in shopping_list:
    # If the item is in both lists print the following
    if item in at_the_shops:
        print(f"{item}? Yay, they've got it!")
    # If the item is not in both lists print the following
    else:
        print(f"{item}? Oh no, they've not got it!")

#
# Activity 6
#

# Create variable with range of numbers 1-10
count1 = range(1,11)
# For loop through each number in the range, print the number
for i in count1:
    print(i)

# Create variable with value of 0
count2 = 0
# Create while loop to check if the number is less than 10 and if not, print the number and add one
while count2 < 10:
    count2 += 1
    print(count2)


# The while loop has more lines of code
# Both required variables as a start point of things to loop through
# In this instance, the for loop is more useful as we have a predefined number to work with and the code is shorter and cleaner