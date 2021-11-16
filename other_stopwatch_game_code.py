# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
x = y = 0
flag = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    mins = t / 600
    s_tenths = t % 600 / 10.0
    if s_tenths < 10:
        return str(mins) + ":" + "0" + str(s_tenths)
    else:
        return str(mins) + ":" + str(s_tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    timer.start()
    global flag
    flag = True
    
def stop_button():
    timer.stop()
    global x, y, flag
    if flag:
        y += 1
        if t % 600 % 10 == 0:
            x += 1
    flag = False
    
def reset_button():
    global t, x, y, flag
    t = 0
    x = y = 0
    flag = False
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), [70, 85], 30, "white")
    canvas.draw_text(str(x) + "/" + str(y), [160, 20], 26, "green") 

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_button, 95)
frame.add_button("Stop", stop_button, 95)
frame.add_button("Reset", reset_button, 95)
# start frame
frame.start()

