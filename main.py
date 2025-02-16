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