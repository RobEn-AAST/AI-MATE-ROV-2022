import cv2
from screeninfo import get_monitors
import numpy as np

def Display8imgs(imgs):
    window_name= "fullscreen"

    # width and height of the window
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height
    
    # make full screen window
    cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # resize images

    img_1=cv2.resize(imgs[0],(width//3,height//3))
    img_2=cv2.resize(imgs[1],(width//3,height//3))
    img_3=cv2.resize(imgs[2],(width//3,height//3))
    img_4=cv2.resize(imgs[3],(width//3,height//3))
    img_5=cv2.resize(imgs[4],(width//3,height//3))
    img_6=cv2.resize(imgs[5],(width//3,height//3))
    img_7=cv2.resize(imgs[6],(width//3,height//3))
    img_8=cv2.resize(imgs[7],(width//3,height//3))
    img_9=np.zeros((height//3,width//3,3), np.uint8)

    #final shape review
    img_review= final_shape([[img_7,img_4,img_2],[img_6,img_9,img_5],[img_1,img_3,img_8]])

    cv2.imshow(window_name,img_review)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# gathering images
def final_shape(list_2d):
    return cv2.vconcat([cv2.hconcat(list_1) for list_1 in list_2d])

if __name__=='__main__':
    Display8imgs()
    