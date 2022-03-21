import random, math
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card
print(deal_card())

user_card = []
computer = []
for _ in range(0,2):
    user_card.append(deal_card())
    computer.append(deal_card())
print(user_card)
print(computer)

def calculate_score(user_card,computer):
    pass
    sum_user = sum(user_card)
    sum_computer = sum(computer)
    if sum_user >= 21 or sum_computer >= 21 :
        # check 11 is in the list
        if 11 in user_card:
            user_card.remove(11)
            user_card.append(1)
            sum_user = sum(user_card)
            print("new ")
            return sum_user
        elif 11 in computer:
            computer.remove(11)
            computer.append(1)
            sum_computer = sum(computer)
            print("new")
            return sum_computer
        else:
            return 0
    else:
        return sum_user, sum_computer


print(calculate_score(user_card, computer))
# hint 8 don't know '
#how to seperate two return value from function


