import cv2
import numpy as np
import math
import SavePLY # importing necessary libraries and scripts

def create_model(output_name):
    print("Creating model...")
    centerLine = 656 # defining distance between object and camera
    X = []
    Y = []
    Z = []
    theta = 35 # defining laser angle
    step = 5.806 # defining step motor angle per step
    step_rad = math.radians(step) # we will use radians for calculation
    theta_rad = math.radians(theta)
    for i in range(62):
        path = "processed/"+str(i+1)+".png" # processed images' path
        image = cv2.imread(path)
        image = image[15:-15, 125:-15] # for get rid of white frames of processed images, I'll crop image a little bit
        print("Generating model of",str(i+1)+".png")
        sensitivity = 110 #
        lower_white = np.array([0,0,255-sensitivity]) #
        upper_white = np.array([255,sensitivity,255]) # defining white color
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        white_mask = cv2.inRange(hsv_frame, lower_white, upper_white) # defining mask
        coord = cv2.findNonZero(white_mask) # finding coordinates of mask
        x_c = coord[0:,0,0]
        y_c = coord[0:,0,1] # getting x and y coordinates from coord variable
        for d in range(len(x_c)):
            X.append(((x_c[d]/math.sin(theta_rad)-centerLine)*math.cos(step_rad*i+1))) # calculating x coordinate
            Y.append(-y_c[d]) # calculating y coordinate
            Z.append(((x_c[d]/math.sin(theta_rad)-centerLine)*math.sin(step_rad*i+1))) # calculating z coordinate

        cv2.waitKey(0)
        cv2.destroyAllWindows()


    print("Generated",len(X),"vertices")
    SavePLY.SavePLY(X,Y,Z,output_name) # saving output as a .ply file
