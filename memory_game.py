# implementation of card game - Memory

import simplegui
import random

card  = [50, 100]  
turns = 0


def turns_setter(add_turn):
    global turns
    if add_turn:
        turns += 1
    else:
        return turns
    label.set_text("Turns = " + str(turns))


def clicked():
    if exposed[0] != exposed[1]:
        return True
    else:
        return False


def good_guess(guess):
    if guess:
        solved.extend(list(exposed))
        pick[0], pick[1] = False, True

def new_list():
    global card_list
    card_list = range(1,9)
    card_list.extend(range(1,9))
    random.shuffle(card_list)

# helper function to initialize globals
def new_game():
    global counter, click_pos, exposed, pick, solved, turns
    new_list()
    counter = 0
    turns = 0
    click_pos = [0, 0]
    exposed = [False, False]
    pick = [False, True]
    solved = []
    pass  

     
# define event handlers
def mouseclick(pos):
    global click_pos, counter, clicked, turns
    if counter < 2:
        counter += 1
    else:
        counter = 1
        turns_setter(True)
    click_pos = list(pos)
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global guessed_right
    def draw_squares(i):
        if card[0] * i < click_pos[0] < card[0] * i + 50:
            if counter == 1:
                exposed[0] = i
                pick[0] = card_list[exposed[0]]
                if clicked():
                    if pick[0] == pick[1]:
                        good_guess(True)
                good_guess(False)
                exposed[1] = False
            else:
                exposed[1] = i
                pick[1] = card_list[exposed[1]]
                if clicked():
                    if pick[0] == pick[1]:
                        good_guess(True)
                good_guess(False)
        else:
            if isinstance(exposed[0], int):
                canvas.draw_polygon([[card[0] * exposed[0], 0],[card[0] * exposed[0],card[1]],[(card[0] * exposed[0]) + 50,card[1]],[(card[0] * exposed[0]) + 50,0]],1, "green", "black")
                canvas.draw_text(str(card_list[exposed[0]]),((card[0] * exposed[0]) + 15,card[1]/1.5), 45, "white")
            if isinstance(exposed[1], int):
                canvas.draw_polygon([[card[0] * exposed[1], 0],[card[0] * exposed[1],card[1]],[(card[0] * exposed[1]) + 50,card[1]],[(card[0] * exposed[1]) + 50,0]],1, "green", "black")
                canvas.draw_text(str(card_list[exposed[1]]),((card[0] * exposed[1]) + 15,card[1]/1.5), 45, "white")
            canvas.draw_polygon([[card[0] * i, 0],[card[0] * i,card[1]],[(card[0] * i) + 50,card[1]],[(card[0] * i) + 50,0]],1, "black", "green")
            if solved != []:
                for item in range(len(solved)):
                    canvas.draw_polygon([[card[0] * solved[item], 0],[card[0] * solved[item],card[1]],[(card[0] * solved[item]) + 50,card[1]],[(card[0] * solved[item]) + 50,0]],1, "green", "black")
                    canvas.draw_text(str(card_list[solved[item]]),((card[0] * solved[item]) + 15,card[1]/1.5), 45, "white")
        
    map(draw_squares, range(len(card_list)))
    pass




# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label.get_text()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric