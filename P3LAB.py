# Get the amount of money from the user
money = float(input("Enter the amount of money (): "))

# Check if the amount is zero
if money == 0.00:
    print("No money entered.")
else:
    # Convert the money to cents
    cents = int(money * 100)

    # Initialize the number of each coin to zero
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

 # Calculate the number of dollars
    if cents >= 100:
        dollars = cents // 100
        cents = cents - (dollars * 100)

 # Calculate the number of quarters
    if cents >= 25:
        quarters = cents // 25
        cents = cents - (quarters * 25)

 # Calculate the number of dimes
    if cents >= 10:
        dimes = cents // 10
        cents = cents - (dimes * 10)

 # Calculate the number of nickels
    if cents >= 5:
        nickels = cents // 5
        cents = cents - (nickels * 5)

 # Calculate the number of pennies
    pennies = cents  # Whatever is left is pennies

  # Print the results
    if dollars > 0:
        print(dollars, "dollar" if dollars == 1 else "dollars")
    if quarters > 0:
        print(quarters, "quarter" if quarters == 1 else "quarters")
    if dimes > 0:
        print(dimes, "dime" if dimes == 1 else "dimes")
    if nickels > 0:
        print(nickels, "nickel" if nickels == 1 else "nickels")
    if pennies > 0:
        print(pennies, "penny" if pennies == 1 else "pennies")
