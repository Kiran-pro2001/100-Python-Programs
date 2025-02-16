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
print(factorial(number))
  