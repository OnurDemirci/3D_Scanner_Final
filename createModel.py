import cv2
import numpy as np
import math
import SavePLY # importing necessary libraries and scripts
import crop

#cropped = crop.crop("processed/1.jpg")

def create_model(output_name):
    print("Creating model...")
    centerLine = 750 # defining distance between object and camera
    X = []
    Y = []
    Z = []
    theta = 36 # defining laser angle
    step = .9 # defining step motor angle per step
    step_rad = math.radians(step) # we will use radians for calculation
    theta_rad = math.radians(theta)
    for i in range(400):
        path = "processed/"+str(i)+".jpg" # processed images' path
        image = cv2.imread(path)
        image = image[300:-105, 125:-15] # for get rid of white frames of processed images, I'll crop image a little bit
#        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#        cv2.resizeWindow("image", 600,600)
#        cv2.imshow("image",image)
        print("Generating model of",str(i)+".jpg")
        sensitivity = 250 #
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

