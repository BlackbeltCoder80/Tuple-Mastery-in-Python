#Mastering Tuple Packing and Unpacking in Python
#Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

#Problem Statement: You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

#Sample Order Data:
from tabulate import tabulate
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
#- Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.

#NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

#The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

print(tabulate(orders, headers=["Customer", "Item", "Amount"], tablefmt="grid"))