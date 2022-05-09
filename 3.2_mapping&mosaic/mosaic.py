import cv2
from screeninfo import get_monitors
def mosaic():
    window_name= "fullscreen"

    # width and height of the window
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height
    
    # make full screen window
    cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # read images
    img1 = cv2.imread("1.jpg")
    img2 = cv2.imread("2.jpg")
    img3 = cv2.imread("3.jpg")
    img4 = cv2.imread("4.jpg")
    img5 = cv2.imread("5.jpg")
    img6 = cv2.imread("6.jpg")
    img7 = cv2.imread("7.jpg")
    img8 = cv2.imread("8.jpg")

    img_1=cv2.resize(img1,(width//4,height//2))
    img_2=cv2.resize(img2,(width//4,height//2))
    img_3=cv2.resize(img3,(width//4,height//2))
    img_4=cv2.resize(img4,(width//4,height//2))
    img_5=cv2.resize(img5,(width//4,height//2))
    img_6=cv2.resize(img6,(width//4,height//2))
    img_7=cv2.resize(img7,(width//4,height//2))
    img_8=cv2.resize(img8,(width//4,height//2))

    #final shape review
    img_review= final_shape([[img_1,img_2,img_3,img_4],[img_5,img_6,img_7,img_8]])

    cv2.imshow(window_name,img_review)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# gathering images
def final_shape(list_2d):
    return cv2.vconcat([cv2.hconcat(list_1) for list_1 in list_2d])

mosaic()
