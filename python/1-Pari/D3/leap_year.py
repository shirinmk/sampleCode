year = int(input("please enter the year? "))

if year % 4 != 0:
    print("not leap year")
elif year % 100 != 0:
    print("it is leap year")
elif year % 400 != 0:
    print("not leap year")
else:
    print("it is leap year")
