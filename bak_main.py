import cv2
import bluetooth
import numpy as np
import time
import RPi.GPIO as GPIO
from curveTrace import curveTrace
from objDetect import getCenter, getTrashCan

def print_history(pos_history):
    print('xxxxxxxxx')
    for pos in pos_history:
        print(pos[0])
    print('yyyyyyyyy')
    for pos in pos_history:
        print(pos[1])

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #GPIO.add_event_detect(10, GPIO.FALLING, callback=fall_cb,bouncetime=300)
    #GPIO.add_event_detect(10, GPIO.RISING, callback=rise_cb,bouncetime=300)
    
    
    bd_addr = "98:D3:91:FD:49:ED"
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    t0 = cap.read()[1]
    t1 = cap.read()[1]
    pos_t0 = [0,0]
    pos_t1 = [0,0]
    pos_t2 = [0,0]
    count = 0
    pos_history = []
    try:
        while True:
            count += 1
            TrashCenter = getTrashCan(t0)
            t0 = t1
            pos_t0 = pos_t1
            pos_t1 = pos_t2
            t1 = cap.read()[1]
            #cv2.imwrite(str(count)+'.jpg', t1)
            pos_t2 = getCenter(t0, t1)
            pos_history.append(pos_t2)
            if GPIO.input(10) == GPIO.HIGH:
                if count > 2:
                    msg = curveTrace(pos_t0, pos_t1, pos_t2, TrashCenter)
                    sock.send(msg+'\r\n')
                    print(msg)
            else:
                #pass
                sock.send("stop")

    except KeyboardInterrupt:
        print_history(pos_history)
        sock.close()
        cap.release()
        GPIO.cleanup()

if __name__=="__main__":
    main()
