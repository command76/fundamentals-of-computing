import simplegui
number = 217

def collatz_conjecture():
    global number
    if number % 2 == 0:
        number //= 2
        print number
    elif number > 2:
        number = (number * 3) + 1
        print number
    else:
        timer.stop()
    
def tick():
    collatz_conjecture()
    
    
timer = simplegui.create_timer(100, tick)

print timer.start()