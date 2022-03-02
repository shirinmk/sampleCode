# check the number entered is odd or ever
# Write a program that works out whether if a given number is an odd or even number.

number = int(input("enter the number? "))
if number % 2 == 0:
    print(f"{number} is evern")
else:
    print(f"{number} is odd")
