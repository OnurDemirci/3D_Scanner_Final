import cv2
from time import sleep
import RPi.GPIO as GPIO

def capture():
    cap = cv2.VideoCapture('http://192.168.1.26:8080/video')
    DIR = 20
    STEP = 21 
    CW = 1    
    CCW = 0    
    SPR = 400

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, CW)
    step_count = SPR
    delay = .1
    
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        ret, frame = cap.read()
        cv2.imwrite("photos/"+str(int(x))+".jpg",frame)
        print("angle",str(int(x)),"scanned")
      
    GPIO.cleanup()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
