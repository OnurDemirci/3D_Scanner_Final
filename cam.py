import cv2

cap = cv2.VideoCapture('http://192.168.1.108:8080/video')


ret, frame = cap.read()
cv2.imwrite("onur.jpg",frame)
#img = cv2.imread("onur.jpg")
#rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#cv2.imwrite("onur.jpg",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()