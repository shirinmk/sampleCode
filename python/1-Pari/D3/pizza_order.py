print("Welcome to python Pizza Deliveries!")
size = input("what size pizza do you want? S, M, L")
print(size)
add_pepperoni = input("do you want pepperoni")
print(add_pepperoni)
extra_cheese = input("Do you want extra cheese? ")
print(extra_cheese)
price = 0
if size == "s" or size == "S":
    price += 15
    print(price)
    if add_pepperoni == "yes" or add_pepperoni == "y":
        price += 2
        print(price)
elif size == "m" or size == "M":
    price += 20
    print(price)
    if add_pepperoni == "yes" or add_pepperoni == "y":
        price += 3
        print(price)
elif size == "l" or size == "L":
    price += 25
    print(price)
    if add_pepperoni == "yes" or add_pepperoni == "y":
        price += 2
        print(price)
else:
    print(" you typed something else")


if extra_cheese == "yes" or extra_cheese == "y":
    price += 1
    print(price)
print(f"Your final bill is: ${price}")
