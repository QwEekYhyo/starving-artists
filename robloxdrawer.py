import keyboard
import time
import clipboard
from PIL import ImageGrab
import random

import mousemovements
import colormatrix
import utils

############# Global variables #############

# Position on screen of relevant buttons in game
top_left = (654, 168)
middle_tl = (662, 176)
bottom_right = (1266, 780)
color_button = (1083, 829)
color_input = (1080, 740)
close_color = (1322, 458)

# Size of cells to create the drawing grid
width = bottom_right[0] - top_left[0]
height = bottom_right[1] - top_left[1]
delta_width = width / 32
delta_height = height / 32

# Color of the close button
close_button_color = (109, 42, 40)


# Take a screenshot and check that the selected color matches the given one
def is_right_color_selected(color):
    screenshot = ImageGrab.grab()
    return screenshot.getpixel(color_button) == color


# Take a screenshot and check that the close button is not visible through its color
def is_color_menu_closed():
    screenshot = ImageGrab.grab()
    return screenshot.getpixel(close_color) != close_button_color


# Move the mouse to the given coordinates with a randomness of a few pixels
def move_to(coordinates):
    mousemovements.move(
        coordinates[0] + random.randint(0, 2), coordinates[1] + random.randint(0, 2)
    )
    time.sleep(0.05)


# Move mouse and click on the given coordinates
#   Only used to draw on the grid
def pixel_click(coordinates):
    for _ in range(3):
        mousemovements.move(
            coordinates[0] + random.randint(0, 2), coordinates[1] + random.randint(0, 2)
        )
        mousemovements.click()
        time.sleep(0.03)


# Select the given color
def pick_color(color):
    sleep_time = 0.05
    # Ensure that the color picker menu is opened
    time.sleep(0.1)
    while True:
        if not is_color_menu_closed():
            break
        move_to(color_button)
        mousemovements.click()
        time.sleep(0.2)
        if not is_color_menu_closed():
            break

    # Ensure the right color is selected
    while True:
        # If the color picker menu is not opened, call the function recursively
        if is_color_menu_closed():
            pick_color(color)
            return
        move_to(color_input)
        mousemovements.click()
        time.sleep(sleep_time)
        clipboard.copy(utils.rgb_to_hex(color))
        keyboard.send("ctrl+v")
        time.sleep(0.1)
        keyboard.press_and_release("enter")
        time.sleep(sleep_time)

        if is_right_color_selected(color):
            break

    # Ensure that the color picked menu is closed
    while True:
        move_to(close_color)
        time.sleep(sleep_time)
        mousemovements.click()
        time.sleep(sleep_time)
        if is_color_menu_closed():
            break


def main(image_path, starting_delay, quality_loss_factor):
    matrix = colormatrix.get_matrix(image_path, quality_loss_factor)
    unique_colors = colormatrix.get_unique_colors(matrix)

    time.sleep(starting_delay)
    current_selection = None
    for color in unique_colors:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                current = matrix[i][j]
                if current == color:
                    if current_selection != current:
                        current_selection = current
                        pick_color(current)
                    coord = (
                        (j * delta_width) + middle_tl[0],
                        (i * delta_height) + middle_tl[1],
                    )
                    pixel_click(coord)


if __name__ == "__main__":
    image_path = input("Which image would you like to draw ? ")
    quality_loss_factor = int(input("Quality loss factor ? (1 = no quality loss) "))
    delay = 2
    print(f"Starting to draw in {delay} seconds")
    execution_time = utils.time_function(lambda: main(image_path, delay, quality_loss_factor))
    execution_time -= delay
    print(f"Took {utils.time_format(execution_time)} to draw {image_path}")
