#CTI-110
#P4HW2 - Salary Calculator
#Rashid Hendricks
#November 14, 2023
#

# variables
numOfEmp = 0  
totalOverTimePay = 0
totalRegPay = 0  
totalGrossPay = 0  

# run loop until user terminates
while True:

    # enter employee's name, hours worked, and pay rate
    name = input("Enter employee's name or \"Done\" to terminate: ")

    # enter Done to break the loop without any further user input
    if name == "Done":
        break
    
    else:# if continuing, increase employee count by increments of 1
        numOfEmp += 1

    hours_worked = float(input("How many hours did " + name + " work? "))
    rate = float(input("What is " + name + "\'s pay rate? "))

    # set variables to calculate values
    overtime = 0
    overtimePay = 0
    regularPay = 0
    grossPay = 0

    # evaluate overtime, if number of worked hours are greater than 40
    if hours_worked > 40:

        # calculate overtime
        overtime = hours_worked - 40

        # calculate over time Pay(50% more)
        overtimePay = overtime * rate * 1.5

        # calculate regular pay
        regularPay = 40 * rate

        # calculate gross Pay
        grossPay = regularPay + overtimePay
        
    else:
        # otherwise, calculate regular Pay and gross pay
        regularPay = hours * rate
        grossPay = regularPay

    # add over time pay to total over time pay
    totalOverTimePay += overtimePay

    # add regular pay to total regular pay
    totalRegPay += regularPay

    # add gross pay to total gross pay
    totalGrossPay += grossPay

    # print employee name
    print("\nEmployee name: " + name + "\n")

    # print values in tabular format
    print(f'{"Hours Worked":<15}{"Pay Rate":<10}{"OverTime":<10}{"OverTime Pay":<15}{"RegHour Pay":<14}{"Gross Pay":<14}')
    print("-" * 74)
    print(f'{hours_worked:<15}{rate:<10}{overtime:<10}${overtimePay:<14.2f}${regularPay:<13.2f}${grossPay:.2f}')
    print()

# print number of employees entered, total over time pay, total regular pay, and total gross pay
print()
print("Number of employees entered:", numOfEmp)
print("Total amount payed for over time: ${totalOverTimePay:.2f}")
print("Total amount payed for regular hours: ${totalRegPay:.2f}")
print("Total amount payed in gross: ${totalGrossPay:.2f}")


