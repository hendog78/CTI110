# This program calculates and displays travel expenses

# 27 Sept 2023

# CTI-110 P1HW2 - Travel Expense

# Rashid Hendricks

#

print("This program calculates and displays travel expenses")

budget = float(input("Enter the budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you think will spend on gas? "))

hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))

food = float(input("Last, how much do you need for food? "))

print("------------Travel Expenses------------")

print("location: ", destination)

print("Initial Budget: ", budget)

print("\n")

print("Fuel: ", gas)

print("Accommodation: ", hotel)

total_expense = gas + hotel + food

remaining = budget - total_expense

print("\n")

print("Remaining Balance: ", remaining)
