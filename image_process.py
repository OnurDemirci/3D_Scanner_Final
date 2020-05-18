import cv2
import numpy as np # importing necessary libraries and scripts


def imageProcess(path):
    print("Processing Images...")
    for i in range(400):
        path1 = path+str(i)+".jpg" # image path
        print("Processing",str(i)+".jpg")
        img = cv2.imread(path1,0)
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#       img = cv2.flip(img,1) # flipping image in x axis
        size = np.size(img) # getting size of image
        skel = np.zeros(img.shape,np.uint8) # defining empty list for processed image
        ret,img = cv2.threshold(img,190,130,0) #defining red color for thresholding
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
                done = True  #(between line 15 and 26) skeletonization of images

        cv2.imwrite("processed/"+str(i)+".jpg",skel)# generating new processed images
#        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#        cv2.resizeWindow("image", 600,600)
#        cv2.imshow("image",skel) # color test
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    print("Images processed.")

