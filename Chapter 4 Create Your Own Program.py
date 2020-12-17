# Kyle Free
# ITSE 1302
# Chapter 4 Create Your Own Program
# Technical Requirements:
# Include a counter loop.  You may choose whether it is
#   a while counter loop or a for counter loop.
# In the loop,
#    Some processing should occur.  You can decide what
#       processing it will be whether it is math, an input
#       statement, or something I haven't thought of …
#    A print statement should also be included in the loop
#       body so that one can see what occurred in the loop
# At the end of the program, after the loop is complete,
#   you should include some kind of summary information.
'''
This program calculates the amount of money a person would earn
over a period of time if the salary is one penny for the first day,
two pennies for the second day, and doubling for every day after that.
The program will ask for a number of days, then display a table showing
the daily pay and total pay up to the number of days input by the user.
'''
# 0 - Initialization
def heading():
    header = str('Day \t Daily Pay \t Total Pay')
    print(header)
    for c in range(len(header)+7):
        print('-', end='')
    print()


pay = float(0.0)
total = float(0.0)
# 1 - Input
days = int(input('Enter a number of days to collect salary: '))
# 2 - Process
heading()
for d in range(1, days+1):
    if d == 1:
        pay = 0.01
    else:
        pay *= 2
    total += pay
# 3 - Output
    print(f"{format(d,'^3')} \t${format(pay,'^9,.2f')} \t${format(total,'^9,.2f')}")


