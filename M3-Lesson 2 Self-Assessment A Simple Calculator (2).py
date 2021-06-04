#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Spencer Good     6/4/21

# Simple Calculator

class SimpleCalculator:
    
    #This function adds the numbers
    def add(x, y):
        return x + y
    
    #This functions subtracts the numbers
    def subtract(x, y):
        return x - y
    
    #This function multiples the numbers
    def multiply(x, y):
        return x * y
    
    #This function divides the numbers
    def divide(x, y):
        return x / y
    
print("Select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    choice = choice.lower()
    
    if choice != "quit":
        
        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", (num1 + num2))

            elif choice == '2':
                print(num1, "-", num2, "=", (num1 - num2))

            elif choice == '3':
                print(num1, "*", num2, "=", (num1 * num2))

            elif choice == '4':
                print(num1, "/", num2, "=", (num1 / num2))
        else:
            print("Invaild number")
    else:
        print("Thank you for using this calculator")


# In[ ]:




