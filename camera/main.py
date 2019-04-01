import cv2
import serial
import numpy as np
import time
from curveTrace import curveTrace, curve_follow
from objDetect import getCenter, getTrashCan

def print_history(pos_history):
    print('xxxxxxxxxx')
    for pos in pos_history:
        print(pos[0])
    print('yyyyyyyyyy')
    for pos in pos_history:
        print(pos[1])

def main():
    pos_history = []
    ser = serial.Serial('/dev/tty.HC-05-DevB', 9600)
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    t0 = cap.read()[1]
    t1 = cap.read()[1]
    pos_t0 = [0,0]
    pos_t1 = [0,0]
    pos_t2 = [0,0]
    count = 0
    
    trash_y = 0;
    
    try:
        while True:
            count += 1
            TrashCenter = getTrashCan(t0[trash_y:,:,:], count)
            TrashCenter = ( TrashCenter[0], trash_y+TrashCenter[1]) 
            if count == 1:
                trash_y = TrashCenter[1]
            t0 = t1
            #print(t0.shape)
            pos_t0 = pos_t1
            pos_t1 = pos_t2
            t1 = cap.read()[1]
            #cv2.imwrite(str(count)+'.jpg', t1)
            pos_t2 = getCenter(t0[:trash_y,:,:], t1[:trash_y,:,:], count)
            #print(pos_t2)
            pos_history.append(pos_t2)
            if count > 2:
                #msg = curveTrace(pos_t0, pos_t1, pos_t2, TrashCenter)
                print('pos :', pos_t2)
                print('trash :', TrashCenter)
                msg = curve_follow(pos_t2, TrashCenter)
                ser.write((msg+'\r\n').encode('ascii'))
                #print(msg)
            else:
                #pass
                ser.write(b'stop\r\n')

    except KeyboardInterrupt:
        #print_history(pos_history)
        ser.write(b'stop\r\n')
        ser.close()
        cap.release()

if __name__=="__main__":
    main()
