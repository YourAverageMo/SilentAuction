'''
an important note after i finished the exercise is that the teacher found the highest bidder and bid using
a sepereate function and accessed the dictionary itself rather than what i did.
which was to set variables inside the new_bidder functin that would update if the new_bidder was greater than the previous highest
bidder.
i guess i should have done that to get some experience using dictionaries and accessing them.
but that technique made the code very convoluded and i didnt like it as much. 
'''

import os

from art import logo


def clear():
    os.system("clear")


# using another as a loop var
another = 'y'
bids = {}
highest_bidder = ''
highest_bid = 0

print(logo)


def new_bidder():
    global another
    global highest_bidder
    global highest_bid

    name = input("who is bidding?\n")
    bid = int(input("how much do you bid?\n"))
    bids[name] = bid

    if bid > highest_bid:
        highest_bidder = name
        highest_bid = bid

    another = input("is there another else that wants to bid? y/n?\n").lower()
    clear()


while another == 'y':
    new_bidder()

print(highest_bidder)
print(highest_bid)
