# Input, Processing, Output for Leia and her friend Han

# Algorithm with Code Section

# getting original_price and surcharge_rate INPUT... converting to a floating number
original_price = float(input("Original price: $"))
surcharge_rate = float(input("Surcharge % (e.g 0.20 is 20%): "))

# Using the extra_charge variable to assign the original_price * surcharge_rate PROCESSING...
extra_charge = original_price * surcharge_rate

# Assigning the total_price variable to original_price + extra_charge to get the surcharge PROCESSING...
total_price = original_price + extra_charge

# display total_price OUTPUT...
print("The total meal price is $", total_price, sep="")

