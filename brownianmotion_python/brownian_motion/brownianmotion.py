import numpy as np
import random

class BrownianMotion(object):
    def __init__(self, arena_size=[500, 500], robot_size=10, robot_color = (255, 0, 0), linear_speed=2, rotational_speed=1):
        self.arena_size = arena_size
        self.robot_size = robot_size
        self.linear_speed = linear_speed
        self.rotational_speed = rotational_speed

        self.robot_pos = np.array([arena_size[0] / 2, arena_size[1] / 2])
        self.robot_dir = np.array([-1, 0])
        self.robot_color = robot_color

    def simulate_robot(self):

        # simulate linear motion
        self.robot_pos = self.robot_pos + self.linear_speed * self.robot_dir

        collided = False
        # check if collided with walls
        if self.robot_pos[0] <= self.robot_size or self.robot_pos[0] >= self.arena_size[0] - self.robot_size:
            
            # change direction
            self.robot_dir[0] = -self.robot_dir[0]
            collided = True
            
        if self.robot_pos[1] <= self.robot_size or self.robot_pos[1] >= self.arena_size[1] - self.robot_size:
                
            # change direction
            self.robot_dir[1] = -self.robot_dir[1]
            collided = True

        if collided:
            random_duration = random.randint(50, 80)

            for i in range(random_duration):
                self.robot_dir = np.dot(self.robot_dir, np.array([[np.cos(self.rotational_speed), np.sin(self.rotational_speed)], [-np.sin(self.rotational_speed), np.cos(self.rotational_speed)]]))

        return collided