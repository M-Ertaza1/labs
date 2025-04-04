
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 

# start = int (input("enetr the starter number : "))
# end = int (input("enetr the end number : "))

# for i in range(start, end + 1):
#   if i % 7 == 0 and i % 5 == 0:
#       print(i)


# # Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [Formula: c/5f-32/9 [where c = temperature in Celsius and f = temperature in Fahrenheit]Expected Output:60°C is 140 in Fahrenheit 45°F is 7 in Celsius
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# # Get temperature input from the user
# print("Temperature Conversion Program")
# print("1. Convert Celsius to Fahrenheit")
# print("2. Convert Fahrenheit to Celsius")
# choice = input("Enter your choice (1 or 2): ")

# if choice == '1':
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     print(f"{celsius}°C is {fahrenheit:.1f}°F")
# elif choice == '2':
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = fahrenheit_to_celsius(fahrenheit)
#     print(f"{fahrenheit}°F is {celsius:.1f}°C")
# else:
#     print("Invalid choice. Please enter 1 or 2.")


#3 Write a Python program to guess a number between 1 to 9. 
# Note: User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.


# import random
# secret_number = random.randint(1, 9)

# while True:
#     guess = int(input("Guess a number between 1 and 9: "))
#     if guess == secret_number:
#         print("Well guessed!")
#         break
#     else:
#         print("Wrong guess. Try again!")


# 4 Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(1,6):
#  for j in range(i):
#   print("*",end=" ")
#  print()  

# for i in range(4,0,-1):
#  for j in range(i):
#   print("*",end=" ")
#  print() 

# 5. Write a simple Python program that accepts a word from the user and reverse it.

# word = input("Enter a word: ")
# reversed_word = word[::-1]
# print("Reversed word:", reversed_word)



# 6 Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers :                                                                                                                                          numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output:
# Number of even numbers: 5 Number of odd numbers: 4


# input_str = input("Enter numbers separated by spaces: ")
# numbers = [int(num) for num in input_str.split()]

# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print(f"Number of even numbers: {even_count}")
# print(f"Number of odd numbers: {odd_count}")


# 7 Write a simple Python program that prints each item and its corresponding type from the following list.
# Sample List: datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
# ("class":"V", "section":"A']]


# datalist = [1452,11.23,1+2j,True,'w3resource',(0, -1),[5, 12],{"class": "V", "section": "A"} ]
# for item in datalist:
#  print(f"Item: {item}, Type: {type(item)}")



# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note: Use 'continue' statement.
# Expected Output: 01245

# for num in range(7):
#     if num == 3 or num == 6:
#         continue 
#     print(num, end='')  
 
# 9 Write a Python program to get the Fibonacci series between 0 to 50. Note: The
# Fibonacci Sequence is the series of numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, .....
# Every next number is found by adding up the two numbers before it.
# Expected Output: 112358 13 21 34

# a, b = 0, 1
# while a <= 50:
#     print(a, end=' ')  
#     a, b = b, a + b    


# 10 Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three
# and five print "FizzBuzz".
# Sample Output: 
# fizzbuzz
# 1
# 2
# fizz 4
# buzz

# for num in range(1, 51):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)



# 10 Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th
# column of the array should be i*j.
# Note:
# i = 0,1.., m-1
# Test Data: Rows = 3, Columns = 4
# j=0,1, n-1.
# Expected Result: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

# m = int(input("Enter number of rows (m): ")) 
# n = int(input("Enter number of columns (n): "))  
# array_2d = [[i * j for j in range(n)] for i in range(m)]
# print("Generated 2D Array:")
# print(array_2d)



# Write a simple  Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).


# print("Enter your lines (press Enter twice to finish):")
# lines = []
# while True:
#     line = input()
#     if line.strip() == "":  # Check for blank line to terminate
#         break
#     lines.append(line.lower())  # Convert to lowercase and store

# print("\nOutput (in lowercase):")
# for line in lines:
#     print(line)


# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.

# Sample Data: 0100,0011,1010,1001,1100,1001

# Expected Output: 1010


# binary_input = input("Enter comma-separated 4-digit binary numbers: ")
# binary_list = [num.strip() for num in binary_input.split(',')]

# result = [bin_num for bin_num in binary_list 
#           if len(bin_num) == 4 and int(bin_num, 2) % 5 == 0]

# print(','.join(result))



# Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data: Python 3.2 Expected Output:
# Letters 6
# Digits 2


# string = input("Enter a string: ")
# letters = 0
# digits = 0

# for char in string:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1

# print(f"Letters {letters}")
# print(f"Digits {digits}")


# Write a Python program to check the validity of password input by users. Validation
# At least 1 letter between [a-z] and 1 letter between (A-Z)
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False, "Password must be 6-16 characters long"
    
    if not re.search("[a-z]", password):
        return False, "Password needs at least 1 lowercase letter"
    
    if not re.search("[A-Z]", password):
        return False, "Password needs at least 1 uppercase letter"
    
    if not re.search("[0-9]", password):
        return False, "Password needs at least 1 number"
    
    if not re.search("[$#@]", password):
        return False, "Password needs at least 1 special character ($, #, or @)"
    
    return True, "Password is valid"

# Get user input
password = input("Enter your password: ")

# Validate and show result
is_valid, message = validate_password(password)
print(message)