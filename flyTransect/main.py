import cv2
import numpy as np
from rovlib.cameras import RovCam
from rovlib.control import RovMavlink, JoyStickControl

THROTTLE = 0.7
rov = RovMavlink(connection_type = 'udpin', connection_ip = '0.0.0.0', connection_port = '14550', silent_mode = True)
# Binds to the port in the given address
rov.establish_connection()

rov.arm_vehicle() # you only need to arm the vehicle once, there is no need to arm it every time you want to stablize it

# rov.set_vehicle_mode(rov.Mode.STABILIZE)
rov.set_vehicle_mode(rov.Mode.ALT_HOLD)


class RedLineFollowing:
    def __init__(self):
        self.lastDirection = ["left", "up"]  # [0]-> left&right, [1]-> up&down

    # Select ROI
    # return (X, Y, W, H)
    def cameraViewRectangle(self, image) -> tuple:
        bounding_box = cv2.selectROI("Select starting point", image, False)
        cv2.destroyAllWindows()
        # return int(bounding_box[0] + bounding_box[2] / 2), int(bounding_box[1] + bounding_box[3] / 2)
        return bounding_box

    def checkDirection(self, mask, boundings):
        x = boundings[0]
        y = boundings[1]
        w = boundings[2]
        h = boundings[3]

        list_down = mask[y + h, x:x + w]
        list_up = mask[y, x:x + w]
        list_left = mask[y:y + h, x]
        list_right = mask[y:y + h, x + w]

        print(f"left: {cv2.countNonZero(list_left)}")
        print(f"right: {cv2.countNonZero(list_right)}")
        print(f"up: {cv2.countNonZero(list_up)}")
        print(f"down: {cv2.countNonZero(list_down)}")
        print("=====================================================================================")

        if cv2.countNonZero(list_up) > 0 and self.lastDirection[1] != "up":
            print("Move up")
            # joyStick = JoyStickControl(z_throttle=0.8)
            # rov.send_control(joyStick)
            self.lastDirection[1] = "down"
            y -= 20
        if cv2.countNonZero(list_down) > 0 and self.lastDirection[1] != "down":
            print("Move down")
            # joyStick = JoyStickControl(z_throttle=-0.8)
            # rov.send_control(joyStick)
            self.lastDirection[1] = "up"
            y += 20
        if cv2.countNonZero(list_right) > 0 and self.lastDirection[0] != "right":
            print("Move right")
            # joyStick = JoyStickControl(y_throttle=0.8)
            # rov.send_control(joyStick)
            self.lastDirection[0] = "left"
            x += 20
        if cv2.countNonZero(list_left) > 0 and self.lastDirection[0] != "left":
            print("Move left")
            # joyStick = JoyStickControl(y_throttle=-0.8)
            # rov.send_control(joyStick)
            self.lastDirection[0] = "right"
            x -= 20

        if cv2.countNonZero(list_left) == 0 and cv2.countNonZero(list_right) == 0:
            self.lastDirection[0] = None
        if cv2.countNonZero(list_up) == 0 and cv2.countNonZero(list_down) == 0:
            self.lastDirection[1] = None

        return (x, y, w, h)


    def checkMainDirection(self, mask, size):
        # x = 0
        # y = 0
        w = size[1]
        h = size[0]
        regionSize = 30
        minimumPixels = 75

        list_down = mask[h-regionSize:h, 0:w]
        list_up = mask[0:regionSize, 0:w]
        list_left = mask[0:h, 0:regionSize]
        list_right = mask[0:h, w - regionSize : w]


        print(f"left: {cv2.countNonZero(list_left)}")
        print(f"right: {cv2.countNonZero(list_right)}")
        print(f"up: {cv2.countNonZero(list_up)}")
        print(f"down: {cv2.countNonZero(list_down)}")
        print("=====================================================================================")

        if cv2.countNonZero(list_up) > minimumPixels and self.lastDirection[1] != "up":
            print("Move up")
            joyStick = JoyStickControl(z_throttle=THROTTLE)
            rov.send_control(joyStick)
            self.lastDirection[1] = "down"
            # y -= 20
        if cv2.countNonZero(list_down) > minimumPixels and self.lastDirection[1] != "down":
            print("Move down")
            joyStick = JoyStickControl(z_throttle=-0.5)
            rov.send_control(joyStick)
            self.lastDirection[1] = "up"
            # y += 20
        if cv2.countNonZero(list_right) > minimumPixels and self.lastDirection[0] != "right":
            print("Move right")
            joyStick = JoyStickControl(y_throttle=THROTTLE)
            rov.send_control(joyStick)
            self.lastDirection[0] = "left"
            # x += 20
        if cv2.countNonZero(list_left) > minimumPixels and self.lastDirection[0] != "left":
            print("Move left")
            joyStick = JoyStickControl(y_throttle=-THROTTLE)
            rov.send_control(joyStick)
            self.lastDirection[0] = "right"
            # x -= 20

        if cv2.countNonZero(list_left) <= minimumPixels and cv2.countNonZero(list_right) <= minimumPixels:
            self.lastDirection[0] = None
        if cv2.countNonZero(list_up) <= minimumPixels and cv2.countNonZero(list_down) <= minimumPixels:
            self.lastDirection[1] = None

        # return (x, y, w, h)


    def redMask(self, image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #########general range############
        # range_low1 = np.array([0, 50, 50])
        # range_high1 = np.array([10, 255, 255])
        # range_low2 = np.array([170, 50, 50])
        # range_high2 = np.array([180, 255, 255])

        # mask1 = cv2.inRange(hsv_image, range_low1, range_high1)
        # mask2 = cv2.inRange(hsv_image, range_low2, range_high2)

        # # Return the result of two merged masks
        # return cv2.add(mask2, mask1)


        #########Specific range############
        range_low1 = np.array([0, 100, 20])
        range_high1 = np.array([0, 255, 255])
        range_low2 = np.array([160, 100, 20])
        range_high2 = np.array([190, 255, 255])

        mask1 = cv2.inRange(hsv_image, range_low1, range_high1)
        mask2 = cv2.inRange(hsv_image, range_low2, range_high2)

        # Return the result of two merged masks
        return cv2.add(mask2, mask1)

    # TODO test
    def drawRedLineContoures(self, image, mask):
        contours = cv2.findContours(mask.copy(),
                                    cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(contours) > 0:
            red_area = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(red_area)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


# video = cv2.VideoCapture("Resources/videos/fish_pen_transect (1080p).mp4")
# frame = cv2.imread("Resources/images/redLine_canvas")
# frame = cv2.imread("Resources/images/onlinePaint.png")
#frame = cv2.resize(frame,[800,800])
# frame = cv2.imread("Resources/images/circle.jpg")

# _, frame = video.read()
# frame = cv2.imread("Resources/images/227.jpg")
# redLineFollowing = RedLineFollowing()

# # frame = cam.read()
# bounding = redLineFollowing.cameraViewRectangle(frame)


# count = 0
# while 1:
    

#     # frame = cam.read()

#     cv2.imshow("ROV", frame)
#     # cv2.imwrite(f"Resources/images/{count}.jpg", frame)
#     # count = count + 1

  
#     frame =  cv2.blur(frame, (8,8))
#     mask = redLineFollowing.redMask(frame)
#     bounding = redLineFollowing.cameraViewRectangle(frame)
#     # drawRedLineContoures(frame, mask)
#     framecpy = frame.copy()
#     cv2.rectangle(framecpy, (bounding[0], bounding[1]), (bounding[0] + bounding[2], bounding[1] + bounding[3]),
#                     (255, 0, 0), 3)
#     redLineFollowing.drawRedLineContoures(framecpy, mask)
#     cv2.imshow('frame', framecpy)
#     cv2.imshow('mask', mask)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     bounding = redLineFollowing.checkDirection(mask, bounding)
# frame = cv2.imread("Resources/images/227.jpg")
# cam = cv2.VideoCapture(0)
# frame = cv2.imread("Resources/images/300.jpg")


# cam = RovCam(RovCam.FRONT)###Z
cam = cv2.VideoCapture("Resources/videos/test_Trim.mp4")
# frame = cv2.imread("Resources/images/marawanTest.jpg")

redLineFollowing = RedLineFollowing()     


# bounding = redLineFollowing.cameraViewRectangle(frame)

while 1:
    ret, frame = cam.read() ###Z
    frame = cv2.resize(frame, (780, 540),
               interpolation = cv2.INTER_NEAREST)
    frame = cv2.blur(frame, (8,8))
    mask = redLineFollowing.redMask(frame)
    redLineFollowing.checkMainDirection(mask, frame.shape)
    framecpy = frame.copy()
    redLineFollowing.drawRedLineContoures(framecpy, mask)
    cv2.imshow('frame', framecpy)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.destroyAllWindows()

    # bounding = redLineFollowing.checkDirection(mask, bounding)
