# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi = weight(kg)/ height(m) * height(m)
# convert string to number
height = float(height)
# print(height)
weight = int(weight)
# print(weight)

bmi = weight / height ** 2
bmi = round(bmi)
print(f" your bmi is {bmi} ")
if bmi <= 18.5:
    print(f" your bmi is {bmi} and your are underwieght ")
elif 18.5 < bmi < 25:
    print(f" your bmi is {bmi}  and you are normal wieght")
elif 25 < bmi < 30:
    print(f" your bmi is {bmi} , and you are overweigth")
elif 30 < bmi < 35:
    print(f" your bmi is {bmi} , and you are obese")
else:
    print(f" your bmi is {bmi} , and you are clinically obese")


