# template for "Stopwatch: The Game"
import simplegui

# define global variables
WIDTH = 500
HEIGHT = 300
total_ticks = 0
is_running = False
Score = 0
A = 0
B = 0
C = 0
D = 0
E = 0
output = ''
total_stops = 0
scoring_stops = 0
score_board = str(scoring_stops) + '/' + str(total_stops)
scored = False
stopped = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global D, C, B, A, E, output, scoring_stops, scored
    if D < 10:
        D += 1
        scored = False
        if D == 10:
            C += 1
            scored = True
            D = 0
    if C == 10:
        B += 1
        C = 0
    if B == 6:
        A += 1
        B = 0
    if A == 10:
        E += 1
        A = 0
    output = str(E) + str(A) + ':' + str(B) + str(C) + '.' + str(D)
    return output
    
    
''' Another way to calculate is to divide total_ticks by milliseconds
and to use modular arithmatic to get the tenths of a second 
I  used a different and simpler approach '''
        
        
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    timer.start()
    stopped = False
    print stopped
    pass

def stop():
    global total_stops, scoring_stops, score_board, stopped
    timer.stop()
    if stopped == False:
        stopped = True
        print stopped
        total_stops += 1
        score_board = str(scoring_stops) + '/' + str(total_stops)
        if scored:
            scoring_stops += 1
            score_board = str(scoring_stops) + '/' + str(total_stops)
            return score_board
        else:
            return score_board  
    pass

def reset():
    global A, B, C, D, E, output, total_stops, scoring_stops, score_board
    timer.stop()
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    output = str(E) + str(A) + ':' + str(B) + str(C) + '.' + str(D)
    total_stops = 0
    scoring_stops = 0
    score_board = str(scoring_stops) + '/' + str(total_stops)
    pass




# define event handler for timer with 0.1 sec interval
def tick():
    global total_ticks
    total_ticks += 1
    format(total_ticks)


# define draw handler
def draw(canvas):
    canvas.draw_text(output, (WIDTH / 3, HEIGHT / 2), 18, 'red', 'sans-serif')
    canvas.draw_text(score_board, (int(WIDTH * .9), int(HEIGHT * .1)), 18, 'white', 'sans-serif')

    
# create frame
frame = simplegui.create_frame("Stopwatch", WIDTH, HEIGHT)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# register event handlers
frame.set_draw_handler(draw)
timer.start()



# start frame
frame.start()

# Please remember to review the grading rubric
