import numpy as np
import random
import pygame
import time

# arena
arena_size = [500, 500]

# robot specifications
robot_size = 10
robot_color = (255, 0, 0)
robot_pos = np.array([arena_size[0] / 2, arena_size[1] / 2])

# initial dir
robot_dir = np.array([-1, 0])

# motion params
linear_speed = 2
rotational_speed = 1


def simulate_robot():
    global robot_pos, robot_dir

    # simulate linear motion
    robot_pos = robot_pos + linear_speed * robot_dir

    collided = False
    # check if collided with walls
    if robot_pos[0] <= robot_size or robot_pos[0] >= arena_size[0] - robot_size:
        
        # change direction
        robot_dir[0] = -robot_dir[0]
        collided = True
        
    if robot_pos[1] <= robot_size or robot_pos[1] >= arena_size[1] - robot_size:
            
        # change direction
        robot_dir[1] = -robot_dir[1]
        collided = True

    if collided:
        random_duration = random.randint(50, 80)

        for i in range(random_duration):
            robot_dir = np.dot(robot_dir, np.array([[np.cos(rotational_speed), np.sin(rotational_speed)], [-np.sin(rotational_speed), np.cos(rotational_speed)]]))

    return collided

if __name__ == "__main__":
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode(arena_size)

    running = True
    while running:

        # If the user clicks the close button, stop the loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # simulate robot
        simulate_robot()

        # clear screen
        screen.fill((255, 255, 255))

        # print("robot_pos: ", robot_pos)
        print("robot_dir: ", robot_dir)
        # draw robot
        pygame.draw.circle(screen, robot_color, robot_pos.astype(int), robot_size)
        # draw robot direction
        pygame.draw.line(screen, (0, 0, 255), robot_pos.astype(int), robot_pos.astype(int) + robot_dir*50, 2)
        
        # update screen
        pygame.display.update()

        # wait
        time.sleep(0.01)

    pygame.quit()



