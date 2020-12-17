# Kyle Free
# ITSE 1302
# Calorie Counter Minor Program
# Requirements:
# Create a loop that will execute 7 times: the number of days the user has been tracking their calories.
# In the loop,
# 	The prompt for the user should include the value of the loop counter + 1
# 	User should enter the number of calories consumed for each day
# 	Computer should total the calories as they are entered
# When all 7 days have been entered, calculate the average number of calories consumed per day
# Display the total number of calories and the average

# 0 - Initialization
total = float(0.0)
cal = float(0.0)
day = int(1)
# 1 - Input
cal = float(input(f"Enter your calories for day {day}: "))
# 2 - Process
total += cal
for day in range(2, 8):
    cal = float(input(f"Day {day}: "))
    total += cal
calorieAvg = total / day
# 3 - Output
print(f"\nTotal calories consumed during the week: {format(total,',.2f')}\n"
      f"Average calories consumed per day: {format(calorieAvg,',.2f')}")
