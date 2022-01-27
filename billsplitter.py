import random

# This is my first official python project. 
# It consists of a simple bill splitter, for going out with friends.
# Fair warning: it's not the most efficient.

print('Enter the number of friends joining (including you):')
number_friends = int(input())
if (number_friends <= 0):  
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    friends = {}
    for _ in range(number_friends):
        friends[input()] = 0
    print('Enter the total bill value:')
    bill_value = int(input())
    split_amount = bill_value // number_friends
    if bill_value % number_friends != 0:
        split_amount = round(bill_value / number_friends, 2)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    if choice == "Yes":
        random_choice = random.randint(1, number_friends)
        index = 1
        lucky_amount = bill_value // (number_friends - 1)
        if bill_value % number_friends != 0:
            new_amount = round(bill_value / (number_friends - 1), 2)
        for key in friends:
            if index == random_choice:
                print(key, 'is the lucky one!')
                friends[key] = 0
            else:
                friends[key] = lucky_amount
            index += 1
    else:
        print('No one is going to be lucky')
        friends = {key: split_amount for key in friends}
    print(friends)