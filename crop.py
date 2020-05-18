import cv2

def crop(image_path):
    global selection
    selection = False
    global roi
    roi = []
    def roi_selection(event, x, y, flags, param):
        global selection, roi
        if event == cv2.EVENT_LBUTTONDOWN:
            selection = True
            roi = [x, y, x, y]
        elif event == cv2.EVENT_MOUSEMOVE:
            if selection == True:
                roi[2] = x
                roi[3] = y          

        elif event == cv2.EVENT_LBUTTONUP:
            selection = False
            roi[2] = x
            roi[3] = y
                
    image_read_path=image_path
    window_name='Input Image'
    window_crop_name='Cropped Image'
    esc_keycode=27

    wait_time=1

    input_img = cv2.imread(image_read_path,cv2.IMREAD_UNCHANGED)
    if input_img is not None:
        clone = input_img.copy()
        cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name,500,500)
        cv2.setMouseCallback(window_name, roi_selection)
        while True:
            cv2.imshow(window_name,input_img)
        
            if len(roi) == 4:
                input_img = clone.copy()
                roi = [0 if i < 0 else i for i in roi]
                cv2.rectangle(input_img, (roi[0],roi[1]), (roi[2],roi[3]), (0, 255, 0), 2)  
                if roi[0] > roi[2]:
                    x1 = roi[2]
                    x2 = roi[0] 
                else:
                    x1 = roi[0]
                    x2 = roi[2]
                if roi[1] > roi[3]:
                    y1 = roi[3]
                    y2 = roi[1] 
                else:
                    y1 = roi[1]
                    y2 = roi[3] 
                    
                crop_img = clone[y1 : y2 , x1 : x2]
                if len(crop_img):
                    cv2.namedWindow(window_crop_name,cv2.WINDOW_NORMAL)
                    cv2.resizeWindow(window_crop_name,400,400)
                    cv2.imshow(window_crop_name,crop_img)

            k = cv2.waitKey(wait_time)
            if k == esc_keycode:  
                cv2.destroyAllWindows()
                break
            elif k== 115:
                def gfc():
                    print("y coordinates:",y1,y2,", x coordinates:",x1,x2)
                    return x1,x2,y1,y2
                cv2.destroyAllWindows()
                break
    else:
        print('Please Check The Path of Input File')
    return gfc()
