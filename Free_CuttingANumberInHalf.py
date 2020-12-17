# Kyle Free
# ITSE 1302
# Cutting a Number in Half Minor Program
# Requirements:
#   Problem:
# Ask the user to input any positive integer.  Use a condition loop to
#   determine how many times the number can be cut in half before it is less than 1.
# Before starting your design, make sure you understand what steps have to be taken:
# •	What initial value might cause the while condition to fail the first time through the loop?
# •	Figure out how many times 24 can be cut in half before it is less than 1

# 0 - Initialize
# 1 - Input
num = int(input('Enter a positive integer: '))
while num <= 0:
    print('ERROR: Input is not a positive integer.')
    num = int(input('Try again: '))
# 2 - Process
total = num
for n in range(num):
    if total / 2 < 1:
        break
    print(f"{total} / 2 = ", end='')
    total /= 2
    print(total)
# 3 - Output
print(f"The number {num} can be halved {n} times before it is less than 1.")
