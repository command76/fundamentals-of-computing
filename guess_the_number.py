 # template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = random.randrange(0, 100)
guess_range = [{min: 0, max: 100},{min: 0, max: 1000}]
guess_limit = 0
attempts_counter = 0

def restart():
    return new_game()


def attempts():
    global guess_limit
    global attempts_counter
#    if attempts_counter < guess_limit:
#        attempts_counter = attempts_counter + 1    
    print guess_limit, attempts_counter
    if attempts_counter < guess_limit:
        attempts_counter = attempts_counter + 1   
        return True
    elif attempts_counter == guess_limit:
        return True
    else:
        return False
    
    
    

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print
    global secret_number
    global guess_limit
    global attempts_counter
    secret_number = random.randrange(0, 100)
    guess_limit = 0
    attempts_counter = 0

    
    # remove this when you add your code  
    range100()


    # start the program
    f.start()
#    pass

def convert_to_int(guess):
    exclude = ['a','b','c','d','e','f','g','h','i','j','k',
               'l','m','n','o','p','q','r','s','t','u','v',
               'w','x','y','z','A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N','O','P','Q','R',
               'S','T','U','V','W','X','Y','Z']
    # main game logic goes here
    for item in exclude:
        if guess.isdigit():
            guess_number = int(guess)
            return guess_number
        elif guess.find(item) >= 0:
            return
        else:
            guess_number = float(guess)
            guess_number = int(guess_number)
            return guess_number
            
            
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print
    print "New game. Range is [0,100)"
    global guess_limit
    global attempts_counter
    attempts_counter = 0
    guess_limit = 0
#    guess_limit = int(math.ceil(math.log(guess_range[0].get(max)))) + 1
    while 2 ** guess_limit <= guess_range[0].get(max) - guess_range[0].get(min) + 1:
        guess_limit += 1
    print "The number of remaining guesses is " + str(guess_limit)
    return guess_limit
    
    # remove this when you add your code    
#    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print
    print "New game. Range is [0,1000)"
    global guess_limit
    global attempts_counter
    attempts_counter = 0
    guess_limit = 0
#    guess_limit = int(math.ceil(math.log(guess_range[1].get(max)))) + 1
    while 2 ** guess_limit <= guess_range[1].get(max) - guess_range[1].get(min) + 1:
        guess_limit += 1
    print "The number of remaining guesses is " + str(guess_limit)
    return guess_limit

#    pass
    
def input_guess(guess):
    print
    print "Guess was " + guess
    global secret_number
    global attempts_counter
    global guess_limit
    attempts_notifier = "Number of remaining guesses is " + str(guess_limit - attempts_counter)
    if isinstance(convert_to_int(guess), int):
        user_guess = convert_to_int(guess)
        if user_guess != secret_number and attempts_counter == guess_limit:
            print attempts_notifier
            print "You ran out of guesses. The number was " + str(secret_number)
            return new_game()
        elif user_guess - secret_number > 0:
            attempts()
            print attempts_notifier
            print "Lower!"
        elif user_guess - secret_number < 0:
            attempts()
            print attempts_notifier
            print "Higher!"
        elif attempts_counter <= guess_limit and user_guess == secret_number:
            attempts()
            print attempts_notifier
            print "Correct"
            return new_game()
    else:
        if attempts_counter == guess_limit:
            print attempts_notifier
            print "You ran out of guesses. The number was " + str(secret_number)
            return new_game()
        print attempts_counter, guess_limit
        print "Please enter an valid integer"
        print attempts_notifier
        attempts()
        
    
    

   
    
    # remove this when you add your code
#    pass

    
# create frame
f = simplegui.create_frame("Guess the Number", 200, 200, 200)

# register event handlers for control elements and start frame
f.add_input("Input Guess", input_guess, 100)
f.add_button("Range 100", range100, 50)
f.add_button("Range1000", range1000, 50)
f.add_button("Restart", restart, 50)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric



