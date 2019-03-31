import numpy as np

def curveTrace(p1, p2, p3, trashCan):
    if trashCan==(0, 0) or p1==(0,0) or p2==(0,0) or p3==(0,0):
        return "stop"
    
    # y = ax^2 + bx + c
    x1_x2 = p1[0]-p2[0]
    x12_x22 = p1[0]*p1[0]-p2[0]*p2[0]
    y1_y2 = p1[1]-p2[1]
    x2_x3 = p2[0]-p3[0]
    y2_y3 = p2[1]-p3[1]
    x3_x1 = p3[0]-p1[0]
    trashCan_x = trashCan[0]
    trashCan_y = trashCan[1]

    if x2_x3==0 or x1_x2==0 or x3_x1==0:
        return "stop"

    a = ((x1_x2*y2_y3/x2_x3)-y1_y2)/x1_x2/x3_x1
    b = (y1_y2 - a*x12_x22)/(x1_x2)
    c = p2[1] - a*p2[0]*p2[0] - b*p2[0]

    if a == 0 :
        return "stop"

    # trashcan movement
    if b*b-4*a*(c-trashCan_y) <= 0:
        return "stop"
    
    end_x = -b/2/a+np.sqrt(b*b-4*a*(c-trashCan_y))/2/a
    
    
    ################################
    max_thres = 160
    if abs(end_x - trashCan_x) > max_thres:
        return "stop"

    min_thres = 10
    if abs(end_x - trashCan_x) > max_thres:
        print('gotcha')
        return "stop"

    if end_x < trashCan_x:
        if trashCan_x < 200:
            print("Out of bounding")
            return "stop"
        return "front" #move front
    elif end_x > trashCan_x:
        if trashCan_x > 600: 
            print("Out of bounding")
            return "stop"
        return "back" #move back
    else:
        return "stop"

if __name__ == "__main__":
    print(curveTrace([0,0], [2,-5], [6,-6], [6,-5]))
