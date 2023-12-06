# CTI-110
# P3HW2 - Salary
# Rashid Hendricks
# 20 October 2023
#

'''
name = ask user to enter employee name
hours = ask user to enter employee's hours worked
payrate = ask user to enter pay rate

set overtime pay = 0.0
set over_time = 0.0

if hours greater than 40
evaluate overtime pay and regular pay
	over_time = hours_worked - 40
	ot_payRate = pay_rate + (pay_rate * 0.5)
	overTime_pay = over_time * ot_payRate
	reg_pay = 40 * pay_rate

else
do the evalution of the regular pay
reg_pay = hours_worked * pay_rate


And then calculate the gross pay = regular pay + overtime pay

print output
'''

# Read data from user

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Evaluate total pay(overtime pay and regular pay)

overTime_pay = 0.0

over_time = 0.0

if hours_worked > 40:
	over_time = hours_worked - 40
	ot_payRate = pay_rate + (pay_rate * 0.5)
	overTime_pay = over_time * ot_payRate
	reg_pay = 40 * pay_rate
else:
	reg_pay = hours_worked * pay_rate

# Calculate gross pay

gross_pay = reg_pay + overTime_pay

# Print output
print("-----------------------------------")
print("Employee name: ", employee_name)
print()
print(f'{"Hours Worked":<15}{"Pay Rate":10}{"OverTime":10}{"OverTime Pay":14}{"RegHour Pay":14}{"Gross Pay"}')
print("------------------------------------------------------------------------")
print(f'{hours_worked:<15}{pay_rate:<10}{over_time:<10}{overTime_pay:<14}${reg_pay:<13.2f}${gross_pay:<.2f}')
 
