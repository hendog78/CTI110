# Ask the user to enter an integer
print("Enter integer:")
user_num = int(input())

# Print the integer that the user entered
print("You entered:", user_num)

# Square the integer
square = user_num ** 2

# Print square
print(f'{user_num} squared is {square}')

# Cube the integer
cube = user_num ** 3

# Print cube
print(f'And {user_num} cubed is {cube} !!')

# Ask the user to enter another integer
print("Enter another integer:")
another_num = int(input())

# Add the two integers
sum = user_num + another_num

# Multiply the two integers
product = user_num * another_num

# Print the results
print(f"{user_num} + {another_num} is {sum}")
print(f"{user_num} * {another_num} is {product}")
