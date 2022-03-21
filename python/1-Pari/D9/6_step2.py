from art import logo
from os import system
import math
print(logo)
print("Welcome to the secret auction program.")
# make dictionary and put key and vlaue there
dic_people_bid = {}
game_continue = True
while game_continue:

    user_name_key = input("what is your name?: ")
    user_bid_value = int(input("What's your bid?: $"))
    user_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    # adding to dictionary
    dic_people_bid[user_name_key] = user_bid_value

    if user_continue == "no":
        game_continue = False
    system('cls')
print(dic_people_bid)
# find max beween these dictionary
max_value = 0
person = ''
for element in dic_people_bid:
    print(element) # it prints all keys
    if dic_people_bid[element] > max_value:
        max = dic_people_bid[element]
        person = element
print(f"The winer is {person} with a bid of ${max}")
