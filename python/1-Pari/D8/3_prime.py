# Prime numbers are numbers that can only be cleanly divided by itself and 1.
#
# https://en.wikipedia.org/wiki/Prime_number
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
#
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
#
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
#
# https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H
#
# Here are the numbers up to 100, prime numbers are highlighted in yellow:
#
# https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw

# Write your code below this line 👇
import math
def prime_checker(number):
    # new_num = math.ceil(number/2)
    # print(f"new_num is {new_num}")
    # print(number)
    prime = True
    for _ in range(2, number):
        # print(f"inside loop {_}_")
        if number % _ == 0:
            # print(f"not prime")
            prime = False
    if prime:
        print("it is a prime")
    else:
        print("it is not a prime")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


