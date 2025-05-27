while True:
    try:
        change = float(input("Change owed: "))
        if change > 0:
            break
        else:
            print("Amount must be positive")
    except ValueError:
        print("Please enter a valid number")

# Convert dollars to cents and round to avoid floating point issues
cents = round(change * 100)

# Initialize coin counter
coins = 0

# Calculate coins (quarters, dimes, nickels, pennies)
while cents >= 25:
    cents -= 25
    coins += 1

while cents >= 10:
    cents -= 10
    coins += 1

while cents >= 5:
    cents -= 5
    coins += 1

while cents >= 1:
    cents -= 1
    coins += 1

print(coins) 