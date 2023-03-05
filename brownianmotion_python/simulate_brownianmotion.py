import numpy as np
import random
import pygame
import time
from brownian_motion import BrownianMotion

def main():

    # create brownian motion obj
    brownian_motion = BrownianMotion()

    # pygame module init
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode(brownian_motion.arena_size)
    running = True
    
    while running:

        # If the user clicks the close button, stop the loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # simulate robot
        brownian_motion.simulate_robot()

        # clear screen
        screen.fill((255, 255, 255))

        # draw robot
        pygame.draw.circle(screen, brownian_motion.robot_color, brownian_motion.robot_pos.astype(int), brownian_motion.robot_size)
        # draw robot direction
        pygame.draw.line(screen, (0, 0, 255), brownian_motion.robot_pos.astype(int), brownian_motion.robot_pos.astype(int) + brownian_motion.robot_dir*50, 2)
        
        # update screen
        pygame.display.update()

        # wait
        time.sleep(0.01)

    pygame.quit()


if __name__ == "__main__":
    main()