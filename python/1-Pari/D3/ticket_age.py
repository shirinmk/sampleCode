# this program check the height of kids, so they can ride or not

print("welcome to the rollercoaster!")
height = int(input("please enter the height? "))
if height > 120:
    print("you can ride")
    age = int(input("how old are you? "))
    if age >= 18:
        print("please pay $12")
    else:
        print("please pay $8")
else:
    print("sorry, you need to be over 120 centimeters")