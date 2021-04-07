# Deep problem run through for students

# Defining problem:
# total bill amount (from the user)
# levels (from the user): "good" (20%), "fair" (15%), or "bad" (10%)



# declare some variable that stores the user's bill
# request that number from the user
userBill = int(input("Total bill amount? "))

# declare some variable that stores the level of service 
# request that value from the user
serviceLevel = input("Level of service? ")

# declare a variable that will store the tip
userTip = 0
endingBill = 0


# total * 0.20 "good"
if serviceLevel == "good":
    userTip = userBill * 0.2
# total * 0.15 "fair"
elif serviceLevel == "fair":
    userTip = userBill * 0.15
# total * 0.10 "bad"
elif serviceLevel == "bad":
    userTip = userBill * 0.1
else:
    print("Invalid input.")

# Final total = the user's tip + initial amount
# example: $100 (userBill) + $10 (userTip) = $110 (final)
endingBill = userTip + userBill

# Output to user
print(f'Tip amount: {userTip}')
print(f'Total amount: {endingBill}')