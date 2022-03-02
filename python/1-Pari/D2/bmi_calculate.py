# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi = weight(kg)/ height(m) * height(m)
# convert string to number
height = float(height)
print(height)
weight = int(weight)
print(weight)
bmi = (weight / (height * height))
bmi2 = weight / height ** 2
print(round(bmi, 2))
print(int(bmi2))

