import cv2
import serial
import numpy as np
import time
from curveTrace import curveTrace
from objDetect import getCenter, getTrashCan

def main():
    ser = serial.Serial('/dev/tty.HC-05-DevB', 9600)
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    t0 = cap.read()[1]
    t1 = cap.read()[1]
    pos_t0 = [0,0]
    pos_t1 = [0,0]
    pos_t2 = [0,0]
    count = 0

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
            if count > 2:
                msg = curveTrace(pos_t0, pos_t1, pos_t2, TrashCenter)
                ser.write((msg+'\r\n').encode('ascii'))
                print(msg)
            else:
                #pass
                ser.write('stop')

    except KeyboardInterrupt:
        ser.close()
        cap.release()

if __name__=="__main__":
    main()
