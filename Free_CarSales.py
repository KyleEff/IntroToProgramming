# Kyle Free
# ITSE 1302
# Car Sales Minor Program
# Requirements:
# The owner of a car dealership would like a program where he can enter the
#   price of each car sold during a day and the program will calculate the
#   total revenue taken in from the sales as well as display the number
#   of cars sold, and the average price of the sales.
# Technical Requirements:
# •	Use a sentinel value to indicate that the list of car sales is finished.
# •	Use a while loop to process the sales
# Before starting your design, make sure you understand what steps have to be taken:
# •	What initial value might cause the while condition to fail the first time through the loop?
# •	Given the following sale prices, calculate the total, the number of sales and the average sale on paper.

# 0 - Initialize
revenue = float(0.0)
numSales = int(0)
avgSale = float(0.0)
# 1 - Input
sale = float(input('Enter 0 to finish sale input.\nEnter sale amount: $'))
# 2 - Process
while sale > 0:
    numSales += 1
    revenue += sale
    sale = float(input('$'))
avgSale = revenue / numSales
# 3 - Output
print(f"Number of cars sold: {numSales}\n"
      f"Total Amount of Revenue from Sales: ${format(revenue,',.2f')}\n"
      f"Average sale price: ${format(avgSale,',.2f')}")
