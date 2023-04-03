from GUI import GUI
from HAL import HAL
import cv2
import numpy as np
# Enter sequential code!

kp = -1/500
kd = -1/200

error = 0.0
prev_error = 0.0

while True:
    # Enter iterative code!
    img = HAL.getImage()

    # filter red color
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # lower red
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0= cv2.inRange(img_hsv, lower_red, upper_red)
    
    # upper red
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    mask = mask0 + mask1
    
    output = img.copy()
    output = cv2.bitwise_and(output, output, mask=mask)
    

    h,w,c = img.shape
    
    # find center of mask
    moment = cv2.moments(mask)
    
    if moment['m00'] != 0:
        setpt_x = int(moment['m10'] / moment['m00'])
        setpt_y = int(moment['m01'] / moment['m00'])
        cv2.circle(output, (setpt_x, setpt_y), 20, (0,0,255), 5)
        print("predicted x: {} w/2: {} ".format(setpt_x, w/2))
        error = setpt_x - float(w/2)
        p_error = kp*float(error)
        d_error = kd*(float(error) - float(prev_error))
        prev_error = float(error)
        
        print("error", float(error))
        print("p_error {} d_Error {}".format(p_error, d_error))
        
        if abs(error) > 10:
            HAL.setV(1)
        else:
            HAL.setV(5)
        HAL.setW(p_error + d_error)
        
        GUI.showImage(output)

    