# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

numbers = range(5)
random.shuffle(numbers)
#print numbers

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        a = 0
    elif name == "Spock":
        a = 1
    elif name == "paper":
        a = 2
    elif name == "lizard":
        a = 3
    elif name == "scissors":
        a = 4
    else: print "name not valid"
    return a
        

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
   
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else : print "invalid number"
    
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
   
    
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    playernum = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    #compnum = random.randrange(0,5,1)
    #print compnum
    
    compnum = numbers.pop()
    #print compnum
 
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(compnum)
    # print out the message for computer's choice
    print "Computer chooses" , comp_choice
    # compute difference of comp_number and player_number modulo five
    diffnum = playernum - compnum
    # use if/elif/else to determine winner, print winner message
    if (diffnum % 5 == 1) or (diffnum % 5 == 2):
     print "Player wins!"
    elif (diffnum % 5 == 3) or (diffnum % 5 == 4):
     print "Computer wins!"
    elif (diffnum % 5 == 0):
     print "Player and computer tie!"
    print "\n"
            
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

