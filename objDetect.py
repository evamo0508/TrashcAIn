import numpy as np
import cv2

def getCenter(t0, t1):
    grey0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)
    grey1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
    blur0 = cv2.GaussianBlur(grey0,(7,7),0)
    blur1 = cv2.GaussianBlur(grey1,(5,5),0)
    d = cv2.absdiff(blur0, blur1)
    ret, th = cv2.threshold( d, 10, 255, cv2.THRESH_BINARY )
    dilated = cv2.dilate(th, None, iterations=1)
    _,contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    if len(areas) == 0:
        return (0,0)
    max_index = np.argmax(areas)
    cnt = contours[max_index]
    x,y,w,h = cv2.boundingRect(cnt)
    #markColor = (0,255,0)
    #cv2.drawContours(t0, cnt, -1, markColor, 2)
    #cv2.rectangle(t0,(x,y),(x+w,y+h), markColor,2)
    #cv2.imwrite('pic_new{}.jpg'.format(i), t0)
    return (x+0.5*w, y+0.5*h)

def getCenter_write(t0, t1):
    grey0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)
    grey1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
    blur0 = cv2.GaussianBlur(grey0,(7,7),0)
    blur1 = cv2.GaussianBlur(grey1,(5,5),0)
    d = cv2.absdiff(blur0, blur1)
    ret, th = cv2.threshold( d, 10, 255, cv2.THRESH_BINARY )
    dilated = cv2.dilate(th, None, iterations=1)
    _,contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    if len(areas) == 0:
        return (0,0)
    max_index = np.argmax(areas)
    cnt = contours[max_index]
    x,y,w,h = cv2.boundingRect(cnt)
    markColor = (0,255,0)
    cv2.drawContours(t0, cnt, -1, markColor, 2)
    cv2.rectangle(t0,(x,y),(x+w,y+h), markColor,2)
    cv2.imwrite('pic_new{}.jpg'.format(i), t0)
    return (x+0.5*w, y+0.5*h)


def getTrashCan(t0):
    t1 = t0;
    # cv2.imwrite("green.png", t0)
    hsv = cv2.cvtColor(t1, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (40,40,40), (70,255,255))
    imask = mask>0
    green = np.zeros_like(t1, np.uint8)
    green[imask] = t1[imask]

    greengray = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
    dilated = cv2.dilate(greengray, None, iterations=1)
    ret, th = cv2.threshold(dilated, 10, 255, cv2.THRESH_BINARY )
    _, contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    if len(areas) == 0:
        print('No green objects!')
        return (0,0)

    max_index = np.argmax(areas)
    cnt = contours[max_index]
    x,y,w,h = cv2.boundingRect(cnt)
    # markColor = (0,255,0)
    # cv2.drawContours(t1, cnt, -1, markColor, 2)
    # cv2.rectangle(t1,(x,y),(x+w,y+h), markColor,2)

    # cv2.imwrite("green.png", t0)
    return (x+0.5*w, y)

