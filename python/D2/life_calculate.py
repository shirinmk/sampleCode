# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until
# 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x days, y weeks, and z months left.
#
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age = int(age)
remain_year = 90 - age
print(remain_year)
# break remain_year to days and week and months
remain_week = remain_year * 52
remain_days = remain_year * 365
remain_month = remain_year * 12
print(f"You have {remain_year} years, {remain_days} days, {remain_week} weeks, and {remain_month} months left.")