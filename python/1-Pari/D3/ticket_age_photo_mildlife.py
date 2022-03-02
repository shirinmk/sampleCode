# this program check the height of kids, so they can ride or not

print("welcome to the rollercoaster!")
height = int(input("please enter the height? "))
total = 0
price = 0
if height > 120:
    print("you can ride")
    age = int(input("how old are you? "))
    if age >= 18:
        # check mildlife
        if 45 < age < 55:
            price = 0
        # print("please pay $12")
        else:
            price = 12
    elif 12 <= age & age < 18:
        # print("please pay $7")
        price = 7
    else:
        # print("please pay $5")
        price = 5
else:
    print("sorry, you need to be over 120 centimeters")
photo_answer = input("do you want photo? yes/no ")
if photo_answer == "yes":
    total = price + 3
else:
    total = price

print(f"you need to pay {total}")