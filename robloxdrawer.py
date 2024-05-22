import keyboard
import time
import clipboard
from PIL import ImageGrab
import random

import mousemovements
import getmatrix

matrix = getmatrix.get_matrix("images/skin.png")
top_left = (654, 168)
middle_tl = (662, 176)
bottom_right = (1266, 780)
color_button = (1083, 829)
color_input = (1080, 740)
close_color = (1322, 458)

width = bottom_right[0] - top_left[0]
height = bottom_right[1] - top_left[1]
delta_width = width / 32
delta_height = height / 32

close_button_color = (109, 42, 40)

def rgb_to_hex(rgb):
    temp = ["", "", ""]
    for i in range(3):
        temp[i] = hex(rgb[i])[2:]

    result = ""
    for v in temp:
        if len(v) < 2:
            result += "0" + v
        elif len(v) == 2:
            result += v
            
    return result

def is_right_color_selected(color):
    screenshot = ImageGrab.grab()
    return screenshot.getpixel(color_button) == color

def is_color_menu_closed():
    screenshot = ImageGrab.grab()
    is_closed = screenshot.getpixel(close_color) != close_button_color
    return is_closed

def click_to(coordinates): 
    mousemovements.move(coordinates[0] + random.randint(0, 2), coordinates[1] + random.randint(0, 2))
    time.sleep(0.1)

def pixel_click(coordinates):
    for _ in range(3):
        mousemovements.move(coordinates[0] + random.randint(0, 2), coordinates[1] + random.randint(0, 2))
        mousemovements.click()
        time.sleep(0.05)
    

sleeptime = 0.1
def pick_color(color):
    while True:
        click_to(color_button)
        mousemovements.click()
        time.sleep(sleeptime)
        if not is_color_menu_closed():
            break
 
    while True:
        if is_color_menu_closed():
            pick_color(color)
            return
        click_to(color_input)
        #click_to(color_input)
        mousemovements.click()
        time.sleep(sleeptime)
        #mouse.double_click()
        clipboard.copy(rgb_to_hex(color))
        keyboard.send("ctrl+v")
        time.sleep(0.1)
        keyboard.press_and_release("enter")
        time.sleep(sleeptime)

        if is_right_color_selected(color):
            break

    while True:
        click_to(close_color)
        time.sleep(sleeptime)
        mousemovements.click()
        time.sleep(sleeptime)
        if is_color_menu_closed():
            break

    
# get unique colors
unique_colors = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        current_color = matrix[i][j]
        if current_color != "void" and current_color not in unique_colors:
            unique_colors.append(current_color)
#

# main
time.sleep(4)
current_selection = None
for color in unique_colors:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            if current == color:
                if current_selection != current:
                    current_selection = current
                    pick_color(current)
                coord = ((j * delta_width) + middle_tl[0], (i * delta_height) + middle_tl[1])
                pixel_click(coord)

