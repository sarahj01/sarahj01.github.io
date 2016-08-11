"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PURPLE = (208, 14, 250)





pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
x_pos = 350
y_pos = 250
x_direction = 1
y_direction = -1
colors = [BLUE, BLACK, PURPLE, GREY, WHITE]
picked_color = colors[random.randint(0,len(colors)-1)]








# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here
    picked_color = colors[random.randint(0,len(colors)-1)]
    pygame.draw.circle(screen,picked_color,(x_pos, y_pos),30,0)
    x_pos += 10 * x_direction
    y_pos += -10 * y_direction
    if x_pos >= 670:
        x_direction = -1
        #x_pos += 15 * direction
    if x_pos <= 30:
        x_direction = 1
    if y_pos <= 30:
        y_direction = -1
    if y_pos >= 470:
        y_direction = 1




    #y_pos += 15

    #pygame.time.delay(200)


    






    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
