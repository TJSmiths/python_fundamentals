#
# Activity 1
#

# Create variable of password from user input
password = input("Enter Password: ")

# Check password length and return results
if len(password) >= 8:
    print(password)
else:
    print("Password is too short.")

#
# Activity 2
#

# Create variable as integer based off user input
num = int(input("Pick a number: "))

# Check if the number is divisible by 3 or 5
if num % 3 == int() or num % 5 == int():
    print("The number is divisible by 3 or 5.")
else:
    print("The number is not divisible by 3 or 5.")

#
# Activity 3
#

# Create variable as integer based off user input
num = int(input("Enter a number: "))

# Check if num is divisible by 3 and 7
if num % 3 == int() and num % 7 == int():
    print("fizzbuzz")
# Check if num is divisible by 3
elif num % 3 == int():
    print("fizz")
# Check if num is divisible by 7
elif num % 7 == int():
    print("buzz")
# If not divisible by 3 or 7, return num
else:
    print("Your number is " + str(num))

#
# Activity 4
#

print("What is the capital of England")

answer = input("Type your answer here >> ").lower()

if answer == "london":
    print("Correct! The answer is " + answer)
else:
    print("Incorrect, the answer is 'London', not " + answer)

#
# Activity 5
#

# Create variable value as string based off user input
word = input("Enter a word: ").lower()

# Error check to ensure an input has been recorded
if len(word) > 0:
    # Check if the word is a palindrome
    if word == word[::-1]:
        print("This word is a palindrome! Of course it has the same first and last letter!")
    # Compare first and last indexed letters
    elif word[0] == word[-1]:
        print("True")
    else:
        print("False")
else:
    print("No word was entered!")