# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS

print WIDTH // 10, HEIGHT // 10
# define draw
def draw(canvas):
    for row_item in range(0,10):
#        canvas.draw_circle([40 * row_item, 20], BALL_RADIUS, 10, 'Yellow', 'Orange')
        for col_item in range(0, 10):
            canvas.draw_circle([45 * row_item, 45 * col_item], BALL_RADIUS, 10, 'Yellow', 'Orange')

                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()
