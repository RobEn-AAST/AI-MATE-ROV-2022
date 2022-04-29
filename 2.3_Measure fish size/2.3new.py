import cv2
import math
import json
import pickle
import base64
import requests

# draw from left to right & up to bottom please
# من الشمال لليمين يا حيو***ن

RULER_POINT1 = 0, 0 # x, y
RULER_POINT2 = 0, 0 # x, y

ROBOT_POINT1 = 0, 0 # x, y
ROBOT_POINT2 = 0, 0 # x, y

ROBOT_POINT3 = 0, 0 # x, y
ROBOT_POINT4 = 0, 0 # x, y


N = 3
a = 1
b = 1
Length = 0
M = 0

CLICKS_COUNTER = 0

REFERENCE_LENGTH_IN_METERS = 1



def calculate_density():
    global N, a, b, Length, M, ROBOT_POINT4, RULER_POINT1
    cv2.destroyAllWindows()

    ruler_length_in_pixels = REFERENCE_LENGTH_IN_METERS/RULER_POINT1
    print(ruler_length_in_pixels)

    Length = ROBOT_POINT4*ruler_length_in_pixels
    
    print(">>>>" + str(Length))
    
    N = float(input('N = '))
    a = float(input('a = '))
    b = float(input('b = '))
    M = float(N * a * pow(Length, b))

    print("BIOMASS = " + str(M))

def click_event():
    global CLICKS_COUNTER, RULER_POINT1 , RULER_POINT2 , ROBOT_POINT1 ,ROBOT_POINT2 , ROBOT_POINT3, ROBOT_POINT4
    if CLICKS_COUNTER == 0:
        r = cv2.selectROI(img)
        RULER_POINT1 = int(r[3])
        print(RULER_POINT1)
    elif CLICKS_COUNTER == 1:
        r = cv2.selectROI(img)
        ROBOT_POINT2 = int(r[2])
    elif CLICKS_COUNTER == 2:
        r = cv2.selectROI(img)
        ROBOT_POINT3 = int(r[2])
        ROBOT_POINT4 = ROBOT_POINT3 + ROBOT_POINT2
        calculate_density()

    CLICKS_COUNTER+=1

    cv2.imshow('image', img)


def get_frame():
    img = cv2.imread("2.png")
    return img


if __name__=="__main__":
    img = None
    skip = False
    while True:
        if skip :
            break
        img = get_frame()
        img_copied = img.copy()
        cv2.destroyAllWindows()
        cv2.putText(img = img_copied, text = 'approve : a deny : x', org=(15,30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.2, color=(255,0,0), thickness=3)
        print("do u like this frame ? a / x")
        cv2.imshow("q", img_copied)
        while True:
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cv2.destroyAllWindows()
                skip = True
                break
            
            elif cv2.waitKey(1) & 0xFF == ord('x'):
                cv2.destroyAllWindows()
                break
        
    # displaying the image
    cv2.imshow('image', img)
    print("oy")
    # setting mouse handler for the image
    # and calling the click_event() function
    while (CLICKS_COUNTER <= 2):
        click_event()
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()