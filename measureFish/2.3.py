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
    global N, a, b, Length, M
    cv2.destroyAllWindows()
    ruler_length_in_pixels = math.sqrt(pow(abs(RULER_POINT2[0] - RULER_POINT1[0]), 2) + pow(abs(RULER_POINT2[1] - RULER_POINT1[1]), 2)) # 1 meter in real life
    fish_length_in_pixels = math.sqrt(pow(abs(ROBOT_POINT2[0] - ROBOT_POINT1[0]), 2) + pow(abs(ROBOT_POINT2[1] - ROBOT_POINT1[1]), 2))

    length = REFERENCE_LENGTH_IN_METERS * fish_length_in_pixels / float(ruler_length_in_pixels)
    # Length = length
    print(">>>>" + str(length))
    
    N = float(input('N = '))
    a = float(input('a = '))
    b = float(input('b = '))
    M = float(N * a * pow(length, b))

    print("BIOMASS = " + str(M))



def click_event(event, x, y, flags, params):

    global CLICKS_COUNTER, RULER_POINT1 , RULER_POINT2 , ROBOT_POINT1 ,ROBOT_POINT2 , ROBOT_POINT3, ROBOT_POINT4

 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        if CLICKS_COUNTER == 0:
            RULER_POINT1 = x, y
        elif CLICKS_COUNTER == 1:
            RULER_POINT2 = x, y
            
        elif CLICKS_COUNTER == 2:
            ROBOT_POINT1 = x, y
        elif CLICKS_COUNTER == 3:
            ROBOT_POINT2 = x, y
            
        elif CLICKS_COUNTER == 4:
            ROBOT_POINT3 = x, y
        elif CLICKS_COUNTER == 5:
            ROBOT_POINT4 = x, y
            
            # point 2 updated
            ROBOT_POINT2 = ROBOT_POINT2[0] + abs(ROBOT_POINT4[0] - ROBOT_POINT3[0]), ROBOT_POINT2[1] + abs(ROBOT_POINT4[1] - ROBOT_POINT3[1]) 
            
            calculate_density()
            
        CLICKS_COUNTER += 1
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
 

# def containerdocker(URL):
#     stream = requests.get(URL)
#     load = json.loads(stream.content)
#     imdata = base64.b64decode(load['image'])
#     im = pickle.loads(imdata)
#     dd = cv2.imdecode(im, cv2.IMREAD_COLOR)
#     real = cv2.resize(dd, (640,480))
#     return real


# def get_frame():
    
#     while True:
#         frame = containerdocker('http://127.0.0.1/AI')
#         # Display the resulting frame
#         cv2.imshow('frame', frame)
#         # the 'q' button is set as the
#         # quitting button you may use any
#         # desired button of your choice
#         if cv2.waitKey(1) & 0xFF == ord('y'):
#             return frame
# driver function


def get_frame():
    img = cv2.imread("2.png", 0)
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
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()