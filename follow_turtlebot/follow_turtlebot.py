from GUI import GUI
from HAL import HAL
import cv2
# Enter sequential code!

height = 1

# take off and go to origin
yaw_angle = 0
HAL.takeoff(height)

# move towards turtle bot
HAL.set_cmd_pos(-3, -1, height, yaw_angle)

# PID params
kp = 0.1
kd = 0.1

# error in individual directions x and y
error_x = 0.0
prev_error_x = 0.0
error_y = 0.0
prev_error_y = 0.0

while True:
    # Enter iterative code!
    img = HAL.get_ventral_image()
    # print(HAL.get_position())
    GUI.showImage(img)

    # filter green color
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, (36, 25, 25), (70, 255,255))

    output = img.copy()
    output = cv2.bitwise_and(output, output, mask=mask)
    h,w,c = img.shape

    # find center of mask
    moment = cv2.moments(mask)
    if moment['m00'] != 0:
        setpt_x = int(moment['m10'] / moment['m00'])
        setpt_y = int(moment['m01'] / moment['m00'])
        cv2.circle(output, (setpt_x, setpt_y), 20, (0,0,255), 5)

        # Calculate vel in x direction
        error_x = setpt_x - float(w/2)
        v_x = kp*float(error_x) + kd*(float(error_x) - float(prev_error_x))

        # Calculate vel in y direction
        error_y = setpt_y - float(h/2)
        v_y = kp*float(error_y) + kd*(float(error_y) - float(prev_error_y))

        # set velocities using mixed mode
        print("v_X: {} v_Y: {}".format(v_x, v_y))
        HAL.set_cmd_mix(v_x, v_y, height, yaw_angle)

        prev_error_x = float(error_x)
        prev_error_y = float(error_y)

    