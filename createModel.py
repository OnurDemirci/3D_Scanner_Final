import cv2
import numpy as np
import math
import SavePLY

def create_model(output_name):
    print("Creating model...")
    centerLine = 656
    X = []
    Y = []
    Z = []
    theta = 35
    step = 5.806
    step_rad = math.radians(step)
    theta_rad = math.radians(theta)
    for i in range(62):
        path = "processed/"+str(i+1)+".png"
        image = cv2.imread(path)
        image = image[15:-15, 125:-15]
    #    cv2.imshow("c",image)
    #    image = cv2.flip(img, 1)
        print("Generating model of",str(i+1)+".png")
        sensitivity = 110
        lower_white = np.array([0,0,255-sensitivity])
        upper_white = np.array([255,sensitivity,255])
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsv_frame, lower_white, upper_white)
        coord = cv2.findNonZero(red_mask)
        x_c = coord[0:,0,0]
        y_c = coord[0:,0,1]
        for d in range(len(x_c)):
            X.append(((x_c[d]/math.sin(theta_rad)-centerLine)*math.cos(step_rad*i+1)))
            Y.append(-y_c[d])
            Z.append(((x_c[d]/math.sin(theta_rad)-centerLine)*math.sin(step_rad*i+1)))
            
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    print("Generated",len(X),"vertices")
    SavePLY.SavePLY(X,Y,Z,output_name)
    
