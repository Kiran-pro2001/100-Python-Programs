# Python 100 Programs  

# 1. Write a program to print Hello World.
print("Hello World")

# 2. Simple Calculator 
def calculator(num1,num2):
  add = num1 + num2
  subtract = num1 - num2 
  multiply = num1 * num2
  divide = num1 / num2
  return "Sum : ",add, "Subtract :", subtract, "Multiply :", multiply, "Division :",divide

print(calculator(10,5))


# 3. Factorial of a Number 

def factorial(num):
  if num == 0:
    return 1
  else: 
    return num * factorial(num-1)

number = int(input("Enter a Number : "))
print("Factorial :", factorial(number))



# 4. Fibonacci Sequence 



# 5. Check for Prime Number 

# 6. Simple Interest Calculator 
def si_calculator(p,r,t):
  return (p*r*t)/100
print("Simple Interest : ", si_calculator(1000,5,5))
  

# 7. Check for Even or Odd   
def check_odd_even(num):
  if num%2 == 0:
    return "Even" 
  else:
    return "Odd" 
print(check_odd_even(10)) 


# 8. Area of a Circle 
import math 
def area_of_circle(radius): 
  return math.pi * radius ** 2 
print("Area of Circle : ", area_of_circle(5))


# 9. List Comprehension - Squares of a Number 
squares = [num**2 for num in range(1,11)]
print(squares)

# 10. File Handling - Write a File
with open("sample.txt", "a") as file: 
  file.write("Hello World")
  
with open("sample.txt","r") as file: 
  print(file.read())


# 11. Check Palindrome 
def check_palindrome(my_string):
  if my_string == my_string[::-1]:
    print("Palindrome")
  else: 
    print("Not a Palindrome")
check_palindrome("ii")
    
    
# 12. Find the largest amont three numbers 
def largest_of_three(num1,num2,num3):
  my_list = []
  my_list.append(num1)
  my_list.append(num2)
  my_list.append(num3)
  return max(my_list)
print(largest_of_three(10,20,15))


# 13. Print Multiplication Number 
def multiplication_table(num):
  for value in range(1,11):
    print(num * value)
multiplication_table(5)

# 14. Convert Celsius to Fahrenheit 
def celsius_to_farhen(celsius_value):
  return (celsius_value * (9/5)) + 32 
print(celsius_to_farhen(10))


# 15. String Operations 
my_string = "Kiran Kumar"
print("Length :", len(my_string))
print("Uppercase : ", my_string.upper())
print("Lowercase:", my_string.lower())
print("Reverse :",my_string[::-1])