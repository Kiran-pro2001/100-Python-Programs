# Python 100 Programs  

# 1. Write a program to print Hello World.
print("Hello World")

# 2. Simple Calculator 
def calculator(num1,num2):
  add = num1 + num2
  subtract = num1 - num2 
  multiply = num1 * num2
  divide = num1 / num2
  return add,subtract,multiply,divide

print(calculator(10,5))