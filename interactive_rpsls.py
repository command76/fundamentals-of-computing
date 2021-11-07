# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random



# Functions that compute RPSLS
choice = ['rock','Spock','paper','lizard','scissors']

def results(guess, comp_guess):
    if guess in choice:
        print "Player chose " + guess
    else:
        print "Error: Bad input \"" + guess + "\" to rpsls" 
    if comp_guess in choice and guess in choice:
        print "Computer chose " + comp_guess
#    if not(guess in choice):
        
        
def guess_to_number(guess):
    for x in choice:
        if x == guess:
            x = choice.index(guess)
            return x

     
    
# Handler for input field
def get_guess(guess): 
    print
    comp_num = random.randrange(0 - 4)
    comp_guess = choice[comp_num]
    results(guess, comp_guess)
    if guess_to_number(guess) <= 4 and guess_to_number(guess) != None:
        if (guess_to_number(guess) - comp_num) % 5 == 0:
            print "There is a tie!"
        elif (guess_to_number(guess) - comp_num) % 5 > 2:
            print "Computer Wins!"
        else:
            print "Player Wins!"
        
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#