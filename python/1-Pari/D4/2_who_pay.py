# Instructions
#
# You are going to write a program which will select a random name from a list of names. The person selected will
# have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to
# work, you must enter all the names as name followed by comma then space. e.g. name, name, name Example Input
#
# Angela, Ben, Jenny, Michael, Chloe
# Angela, Ben, Jenny, Michael, Chloe
#
# Note: notice that there is a space between the comma and the next name.
# Example Output
#
# Michael is going to buy the meal today!
import random

str_of_people = input("please enter list of all people seperated with comma: ")

#put string in array
list_of_people = str_of_people.split(',')
print(list_of_people)
# choose random index and then print array[index]
len_of_array_list = len(list_of_people)
print(len_of_array_list)
index_random = random.randint(0, len_of_array_list-1)
print(f"{list_of_people[index_random]} is going to buy the meal today!hahaha")