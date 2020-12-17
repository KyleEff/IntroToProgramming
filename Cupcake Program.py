# The Cupcake Program
# 0 - Initialization
BUTTER=int(1) # stick
FLAVORING=int(1) # teaspoon
CREAM_CHEESE=int(1) # cup
SUGAR=int(4) # powdered, cups
# 1 - Input
pansNeeded=int(input('Please enter the number of pans of cupcakes you need to frost:  '))
# 2 - Process
finalButter=float(BUTTER*pansNeeded) # final number needed
finalFlavoring=float(FLAVORING*pansNeeded)
finalCreamCheese=float(CREAM_CHEESE*pansNeeded)
finalSugar=float(SUGAR*pansNeeded)
# 3 - Output
print(f"CUPCAKE FROSTING RECIPE CONVERTER\n"
      f"Number of pans to frost: {format(pansNeeded,'8.1f')}\n"
      f"Sticks of butter: {format(finalButter,'15.1f')}\n"
      f"Cups of cream cheese: {format(finalCreamCheese,'11.1f')}\n"
      f"Teaspoons of flavoring: {format(finalFlavoring,'9.1f')}\n"
      f"Cups of powdered sugar: {format(finalSugar,'9.1f')}")
