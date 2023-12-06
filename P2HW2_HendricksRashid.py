# enter grade for six modules
# get input as float numbers
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# create list with all modules
grades = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]

# get min, max and sum grades list
low = min(grades)
high = max(grades)
sum = sum(grades)

# find average = total sum of grades
avg = sum/len(grades)

# print format
print("-----------Results------------")
print("Lowest Grade:      %.2f"%low)
print("Highest Grade:     %.2f"%high)
print("Sum of Grades:    %.2f"%sum)
print("Average:           %.2f"%low)
print("---------------------------------")


