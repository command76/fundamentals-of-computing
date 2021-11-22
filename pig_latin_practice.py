# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def is_consonant(first_letter):
    vowels = ['a','e','i','o','u']
    if not(first_letter in vowels):
        return True


    
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
        
    if is_consonant(first_letter):
        return rest_of_word + first_letter + "ay"
    else:
        return word + "way"

# Handler for input field
def get_input(word):
    print pig_latin(word)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input('Translate', get_input, 100)

# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


