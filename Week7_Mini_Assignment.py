# Basic infrastructure for Bubble Shooter

import simplegui
import random
import math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = 0
bubble_stuck = True
key_pressed = {"state": "up", "button": "left"}


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# class defintion for Bubbles
class Bubble:
    
    def __init__(self):
        pass
    
    def update(self):
        pass
        
    def fire_bubble(self, vel):
        pass
        
    def is_stuck(self): 
        pass

    def collide(self, bubble):
        pass
            
    def draw(self, canvas):
        pass

# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck, key_pressed
    if simplegui.KEY_MAP["left"] == key:
        key_pressed["state"], key_pressed["button"] = "down", "left"
    elif simplegui.KEY_MAP["right"] == key:
        key_pressed["state"], key_pressed["button"] = "down", "right"
    

def keyup(key):
    global firing_angle_vel, key_pressed
    if simplegui.KEY_MAP["left"] == key:
        key_pressed["state"], key_pressed["button"] = "up", "left"
    elif simplegui.KEY_MAP["right"] == key:
        key_pressed["state"], key_pressed["button"] = "up", "right"
    
# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck, key_pressed
    
    # update firing angle
    
    
    
    if key_pressed.get("state") == "down" and key_pressed.get("button") == "left":
        firing_angle += FIRING_ANGLE_VEL_INC
        print key_pressed
    elif key_pressed.get("state") == "down" and key_pressed.get("button") == "right":
        firing_angle -= FIRING_ANGLE_VEL_INC
        print key_pressed
        
        
        
    #draw firing line
    orient = angle_to_vector(firing_angle)
    upper_endpoint = [FIRING_POSITION[0] + FIRING_LINE_LENGTH * orient[0], 
                      FIRING_POSITION[1] - FIRING_LINE_LENGTH * orient[1]]
    canvas.draw_line(FIRING_POSITION, upper_endpoint, 4, "White")
    
    # update a_bubble and check for sticking
    
    # draw a bubble and stuck bubbles
 
# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
frame.start()