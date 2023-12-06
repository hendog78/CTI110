# This program calculates and displays travel expenses

# 10 OCT 2023

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

print(f"{'Location: ' : <20}", f"{destination : <20}")

print(f"{'Budget: ' : <20}", f"{'$' + str(float(budget)) : <20}")

print(f"{'Fuel: ' : <20}", f"{'$'+str(float(gas)) : <20}")

print(f"{'Accommodation: ' :<20}", f"{'$'+str(float(hotel)) : <20}")

print(f"{'Food: ' :<20}", f"{'$'+str(float(food)) : <20}")

print("---------------------------------------")

total_expense = gas + hotel + food
remaining = budget - total_expense

print("Remaining Balance: ", remaining)
