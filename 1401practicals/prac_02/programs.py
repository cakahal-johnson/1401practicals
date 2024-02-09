# 1. DISCOUNT PRICE

# Algorithm and code using pseudocode IPO with MAGIC NUMBER
#  Getting the INPUT... of the original price converting to float number INPUT...
original_price = float(input("Original price for magic number: $"))

# PROCESSING the discount
discount_rate = original_price * 0.2

# PROCESSING the new price
new_price = original_price - discount_rate

# displaying the result OUTPUT
print("The total Discount rate 20%, of your money $", original_price, " is $", new_price, sep="")


# Algorithm and code using pseudocode IPO with CONSTANT NUMBER
#  Getting the INPUT... of the original price converting to float number INPUT...
# Input
original_price = float(input("Original price for Constant Number: $"))

# Constants
DISCOUNT_RATE_PERCENTAGE = 20 / 100  # 20% discount

# Processing
discount_rate = original_price * DISCOUNT_RATE_PERCENTAGE
new_price = original_price - discount_rate

# Output
# display_result
print("The total Discount rate 20%, of your money $", original_price, " is $", new_price, sep="")
# ============================================ 1 DISCOUNT PRICE ENDS ===============================================

# 2. KILOMETERS TO MILES USING IPO CONSTANTS CONVENTION
# Constants
KILOMETER_TO_MILE = 0.621371
MILE_TO_KILOMETER = 1.60935

# Input
distance_in_kilometers = float(input("Enter distance in kilometers: "))

# Processing
distance_in_miles = distance_in_kilometers * KILOMETER_TO_MILE

# Output
print(f"{distance_in_kilometers} kilometers is equal to {distance_in_miles:.2f} miles")

# ============================================ 2 KILOMETERS TO MILES ENDS ==============================================

# 3. HOLIDAY COST
# Input
daily_food_cost_price = float(input("Enter daily food cost: $"))
daily_activity_cost_price = float(input("Enter daily activities cost: $"))
number_of_days_to_spend = float(input("Enter number of days: "))

# Constants
HOTEL_COST_PER_DAY_RATE = 75

# Processing
total_hotel_cost = HOTEL_COST_PER_DAY_RATE * number_of_days_to_spend
total_food_cost = daily_food_cost_price * number_of_days_to_spend
total_activity_cost = daily_activity_cost_price * number_of_days_to_spend

total_trip_cost = total_hotel_cost + total_food_cost + total_activity_cost

# Output
print("Daily food cost: $", daily_food_cost_price, sep="")
print("Daily activities cost: $", daily_activity_cost_price, sep="")
print("Number of days: ", number_of_days_to_spend, sep="")
print("The trip will cost $", total_trip_cost, sep="")

# ========================================= 3. HOLIDAY COST ENDS ================================

# 4. DEEP SLEEP CALCULATE(PERCENTAGE)
# Step 1: Get input from the user
total_sleep_seconds = int(input("Enter total sleep time in seconds: "))
deep_sleep_seconds = int(input("Enter deep sleep time in seconds: "))

# Step 2: Calculate the percentage of deep sleep
percentage = (deep_sleep_seconds / total_sleep_seconds) * 100

# Step 3: Display the results in decimal format
print(f"Percentage: {percentage}", sep="")

# Step 4: Enhance the program to display time in minutes and seconds
minutes = total_sleep_seconds // 60
seconds = total_sleep_seconds % 60

# Display the results in the desired format
print(f"Total sleep: {minutes}m {seconds}s", sep="")
print(f"Deep sleep: {deep_sleep_seconds // 60}m {deep_sleep_seconds % 60}s", sep="")
print(f"Percentage: {percentage:.2f}%", sep="")





