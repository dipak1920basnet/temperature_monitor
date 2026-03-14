# store temperature for 3 days 
day1 = 28
day2 = 35
day3 = 31

# 2️⃣ Print each temperature

print(day1)
print(day2)
print(day3)

# 3️⃣ Calculate average temperature
total_days = 3
average_temperature = (day1 + day2 + day3)/total_days

# 4️⃣ Print warning if any temperature > 32
if average_temperature > 32:
    print(f"Warning the the temprature is: {average_temperature}")
