# Program 1-B: Classify a tornado by windspeed
# 0 - Initialization
fujita = int(0)
windspeed = float(0.0)
# 1 - Input
windspeed = float(input('Enter the windspeed of the tornado: '))
# 2 - Process
if 40 <= windspeed <= 72:
    fujita = 0
elif 72 <= windspeed <= 112:
    fujita = 1
elif 112 <= windspeed <= 157:
    fujita = 2
elif 157 <= windspeed <= 205:
    fujita = 3
elif 205 <= windspeed <= 260:
    fujita = 4
elif windspeed > 260:
    fujita = 5
# 3 - Output
if windspeed < 40:
    print(f"Windspeed: {windspeed} mph\n"
          f"Fujita Scale: Does not qualify.")
else:
    print(f"Windspeed: {windspeed} mph\n"
          f"Fujita Scale: F-{fujita}")

# Program 2-A
# 0 - Initialization
factorBool = False
sqrt = False
number = int(0)
factorInput = int(0)
# 1 - Input
number = int(input('Enter a number: '))
while number < 100 or number > 1000:
    print('ERROR: Number is not between 100 and 1000. Please try again.\n')
    number = int(input('Enter a number: '))
factorInput = int(input('Enter a possible factor for that number: '))
# 2 - Process
if number % factorInput == 0:
    factorBool = True
    if (number / factorInput) == factorInput:
        sqrt = True
# 3 - Output
print(f"\nNumber: {number}\n"
      f"Possible Factor: {factorInput}")
if factorBool:
    print(f"{factorInput} is a factor of {number}.")
    if sqrt:
        print(f"{factorInput} is the square root of {number}.")
    else:
        print(f"{factorInput} is NOT the square root of {number}.")
else:
    print(f"{factorInput} is NOT a factor of {number}.")
