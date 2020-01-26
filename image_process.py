import cv2
import numpy as np


def imageProcess(path,image_count):
    print("Processing Images...")
    for i in range(image_count):
        path1 = path+str(i+1)+".png"
        print("Processing",str(i+1)+".png")
        img = cv2.imread(path1,0)
        img = cv2.flip(img,1)
        size = np.size(img)
        skel = np.zeros(img.shape,np.uint8)
        ret,img = cv2.threshold(img,127,150,0)
        element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        done = False
    
        while( not done):
            eroded = cv2.erode(img,element)
            temp = cv2.dilate(eroded,element)
            temp = cv2.subtract(img,temp)
            skel = cv2.bitwise_or(skel,temp)
            img = eroded.copy()
            zeros = size - cv2.countNonZero(img)
            if zeros==size:
                done = True
    
        cv2.imwrite("processed/"+str(i+1)+".png",skel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    print("Images processed.")
