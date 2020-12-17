# Kyle Free
# ITSE 1302
# Pay Check Program
# Complex Extension
# Requirements:
# •	Program will calculate a person's gross pay based on number of hours worked,
#       pay rate and overtime (if earned)
# •	Standard pay is calculated as pay rate * number of hours worked up to 40
# •	Overtime pay is calculated as pay rate * 1.5 * number of hours over 40
# •	Determine the amount of tax withheld for:
# o	Social Security: 6.2%
# o	Medicare: 1.45%
# •	Calculate the net pay based on gross pay – tax withheld
#
# •	Display the value of each of the variables with appropriate labels (See input and output example)
#
# •	Input Example:
#
# Enter Company Name: Programs R Us
# Enter Employee Name:  Cal Q. Later
# Enter Hourly Pay Rate:  22.50
# Enter Hours Worked:  45
#
# Output Example:
#
# Employee: Cal Q. Later
#
#
# Programs R Us Weekly Pay Check
# Hourly Pay Rate:         22.50
# Hours Worked:            40.00
# Gross Pay:              900.00
#
# OT Pay Rate:             33.75
# OT Hours Worked:          5.00
# OT Gross Pay:           168.75
#
# Ttl Gross Pay:        1,068.75
#
# SSI Tax:                 66.26
# Medicare Tax:            15.50
# Net Pay:                986.99
# 0 - Initialization
otHours = float(0.0)
otPay = float(0.0)
OT = False
# 1 - Input
companyName = input('Enter Company Name: ')
name = input('Enter Employee Name: ')
payRate = float(input('Enter Hourly Pay Rate: $'))
hoursWorked = float(input('Enter Hours Worked: '))
# 2 - Process
standardPay = hoursWorked * payRate # no overtime
if hoursWorked > 40:
    OT = True
    otHours = hoursWorked - 40
    otPay = otHours * (payRate * 1.5)
    standardPay = (hoursWorked - otHours) * payRate
    grossPay = standardPay + otPay
else:
    grossPay = standardPay
SS = grossPay * 0.062 # amount paid TO Social Security
MEDICARE = grossPay * 0.0145 # amount paid TO Medicare
# 3 - Output
# len('Programs R Us Weekly Pay Check') # 30
print(f"\nEmployee: {format(name,'20')}\n\n\n"
      f"{companyName} Weekly Pay Check\n"
      f"Hourly Pay Rate: ${format(payRate,'12.2f')}\n"
      f"Hours Worked: {format(hoursWorked-otHours,'16.2f')}\n"
      f"Gross Pay: ${format(grossPay-otPay,'18,.2f')}\n"
      )
if OT:
    print(f"OT Pay Rate: ${format(payRate * 1.5, '16.2f')}\n"
          f"OT Hours Worked: {format(otHours, '13.2f')}\n"
          f"OT Gross Pay: ${format(otPay, '15,.2f')}\n\n"
          f"Ttl Gross Pay: ${format(grossPay, '14,.2f')}\n")
else:
    print(f"Ttl Gross Pay:${format(grossPay,'15,.2f')}\n")
print(f"SSI Tax: ${format(SS,'20.2f')}\n"
      f"Medicare Tax: ${format(MEDICARE,'15.2f')}\n"
      f"Net Pay: ${format(grossPay - (SS + MEDICARE),'20,.2f')}")