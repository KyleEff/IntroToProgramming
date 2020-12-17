# Kyle Free
# ITSE 1302
# Car Sales with Functions Minor Program
# Requirements:
# Original Problem: (This completed program is available as part of the assignment files.)
# The owner of a car dealership would like a program where he can
#   enter the price of each car sold during a day and the program
#   will calculate the total revenue taken in from the sales as well
#   as display the number of cars sold, and the average price of the sales.

# Additional Requests:
# The owner of a car dealership would like the program
#   to calculate the total sales tax due for the car sales
#   at a rate of 8.5%.  Please display the result along with
#   the profit by subtracting the tax due from the total sales.

# Technical Requirements:
# •	Use a sentinel value to indicate that the list of car sales is finished.
# •	Use a while loop to process the sales
# •	Use a function with a parameter of totalSales to calculate and return the amount of sales tax owed
# •	Use a function with a parameter of totalSales and amount of sales tax owed to return the total profit.

# My IDE is throwing all sorts of suggestions at me about
#   camelCase versus lowercase so I ended up going
#   back and forth between the two

SALES_TAX = 0.085


def main():
    total, numCarsPurchased = get_total()
    profit(total, get_sales_tax(total))
    sales_avg(total, numCarsPurchased)


def get_total():
    # 0 - Initialization
    total = float(0.0)
    numCarsPurchased = int(0)
    # 1 - Input
    carPrice = float(input('Enter "0" when there are no more sales.\nEnter sale: $'))
    # 2 - Process
    while carPrice > 0:
        total += carPrice
        numCarsPurchased += 1
        carPrice = float(input("Enter sale: $"))
    # 3 - Output
    print(f"\nNumber of cars sold: {numCarsPurchased}\n"
          f"Total amount of revenue from sales: ${format(total,',.2f')}")
    return total, numCarsPurchased


def get_sales_tax(totalSales):
    tax_amt = totalSales * SALES_TAX
    print(f"Total amount of sales tax due from revenue: ${format(tax_amt,',.2f')}")
    return tax_amt


def profit(totalSales, tax_amt):
    profit_made = totalSales - tax_amt
    print(f"Total profit from revenue: ${format(profit_made,',.2f')}")


def sales_avg(total, numCarsPurchased):
    avg = total / numCarsPurchased
    print(f"Average sale price: ${format(avg,',.2f')}")


main()
