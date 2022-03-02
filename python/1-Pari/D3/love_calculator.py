print("welcome to the love calculator! ")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()
right_side = 0
left_side = 0
right_side += name1.count('t')
right_side += name1.count('r')
right_side += name1.count('u')
right_side += name1.count('e')
right_side += name2.count('t')
right_side += name2.count('r')
right_side += name2.count('u')
right_side += name2.count('e')
left_side += name1.count('l')
left_side += name1.count('o')
left_side += name1.count('v')
left_side += name1.count('e')
left_side += name2.count('l')
left_side += name2.count('o')
left_side += name2.count('v')
left_side += name2.count('e')
number = right_side * 10 + left_side
if number < 10 or number > 90:
    print(f"Your score is {number}%, you go together like coke and mentos")
elif 40 <= number <= 50:
    print(f"Your score is {number}%, you are alright together")
else:
    print(f"Your score is {number}%")