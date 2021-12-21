# Implementation of classic arcade game Pong
import math
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
move_paddle1_down = False
move_paddle1_up = False
move_paddle2_down = False
move_paddle2_up = False



def reset():
    new_game()


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel = [ -1, 0 ]
    if direction == True:
        ball_vel[0] = random.randrange( 120, 240 ) // 60
        ball_vel[1] = random.randrange( 60, 180) // 60
    else:
        ball_vel[0] = -1 * random.randrange( 120, 240 ) // 60
        ball_vel[1] = -1 * random.randrange( 60, 180) // 60
       

        


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [[0, HEIGHT // 2],[PAD_WIDTH, HEIGHT // 2]]
    paddle2_pos = [[WIDTH - PAD_WIDTH, HEIGHT // 2],[WIDTH, HEIGHT // 2]]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    score1 = 0
    score2 = 0
    spawn_ball('')


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, move_paddle1_up
    global move_paddle1_down, move_paddle2_down, move_paddle2_up
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
        
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
        
            
    # draw ball
    canvas.draw_circle((ball_pos), 20, 10, "green", "green")
    
    # update paddle's vertical position, keep paddle on the screen
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] *= -1
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] *= -1
        
# Movement for first paddle
########################################
        
    if paddle1_pos[0][1] <= HALF_PAD_HEIGHT:
        move_paddle1_up = False
    elif paddle1_pos[0][1] >= HEIGHT - HALF_PAD_HEIGHT:
        move_paddle1_down = False
    
    
    if move_paddle1_down:
        paddle1_pos[0][1] += paddle1_vel[1]
        paddle1_pos[1][1] += paddle1_vel[1]
    elif move_paddle1_up:
        paddle1_pos[0][1] += paddle1_vel[1]
        paddle1_pos[1][1] += paddle1_vel[1]
    else:
        paddle1_vel[1] = 0
        

# Movement for second paddle    
########################################   
        
    if paddle2_pos[0][1] <= HALF_PAD_HEIGHT:
        move_paddle2_up = False
    elif paddle2_pos[0][1] >= HEIGHT - HALF_PAD_HEIGHT:
        move_paddle2_down = False
    

 
    if move_paddle2_down:
        paddle2_pos[0][1] += paddle2_vel[1]
        paddle2_pos[1][1] += paddle2_vel[1]
    elif move_paddle2_up:
        paddle2_pos[0][1] += paddle2_vel[1]
        paddle2_pos[1][1] += paddle2_vel[1]
    else:
        paddle2_vel[1] = 0
        
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos, PAD_HEIGHT, 'Yellow', 'Orange')
    canvas.draw_polygon(paddle2_pos, PAD_HEIGHT, 'Yellow', 'Orange')

    
    # determine whether paddle and ball collide
    
    paddle1_distance = math.sqrt((ball_pos[0] - paddle1_pos[1][0]) ** 2 + (ball_pos[1] - paddle1_pos[1][1]) ** 2)
    paddle2_distance = math.sqrt((ball_pos[0] - paddle2_pos[0][0]) ** 2 + (ball_pos[1] - paddle2_pos[0][1]) ** 2)
    
        
    if ball_pos[0] <= 0 + PAD_WIDTH + BALL_RADIUS:
        if paddle1_distance + BALL_RADIUS + PAD_WIDTH < 75:
            ball_vel[0] *= -1.1
        else:
            spawn_ball(RIGHT)
            score1 += 1
            
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if paddle2_distance + BALL_RADIUS < 75:            
            ball_vel[0] *= -1.1
        else:
            spawn_ball(LEFT)
            score2 += 1
    
    
    
        
    
    # draw scores
    
    canvas.draw_text("Player 1: " + str(score2) + " -- " + "Player 2: " + str(score1), (WIDTH // 3.28, 50), 25, 'Green', 'serif')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, move_paddle1_down, move_paddle1_up
    global move_paddle2_down, move_paddle2_up
    
    # Paddle 1 controls
    
    if key == simplegui.KEY_MAP['w']:
        move_paddle1_up = True
        paddle1_vel[1] = paddle1_vel[1] - 5
    elif key == simplegui.KEY_MAP['s']:
        move_paddle1_down = True
        paddle1_vel[1] = paddle1_vel[1] + 5
        
    # Paddle 2 controls
        
    if key == simplegui.KEY_MAP['up']:
        move_paddle2_up = True
        paddle2_vel[1] = paddle2_vel[1] - 5
    elif key == simplegui.KEY_MAP['down']:
        move_paddle2_down = True
        paddle2_vel[1] = paddle2_vel[1] + 5


def keyup(key):
    global paddle1_vel, paddle2_vel, move_paddle1_down, move_paddle1_up, move_paddle2_up
    global move_paddle2_down
    
    # Paddle 1 controls
    
    if key == simplegui.KEY_MAP['w']:
        move_paddle1_up = False
    elif key == simplegui.KEY_MAP['s']:
        move_paddle1_down = False
   
    # Paddle 2 controls
        
    if key == simplegui.KEY_MAP['up']:
        move_paddle2_up = False
    elif key == simplegui.KEY_MAP['down']:
        move_paddle2_down = False
        


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', reset)


# start frame
new_game()
frame.start()
