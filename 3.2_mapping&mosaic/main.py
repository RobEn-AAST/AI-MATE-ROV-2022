from mapping import DrawLineWidget
from mosaic import mosaic
from PressSave import save
from crop import cropped_images
from cut2Parts import split_img
from time import sleep
import cv2

def mapping():
    draw_line_widget = DrawLineWidget()
    while True:
        cv2.imshow('image', draw_line_widget.show_image())
        key = cv2.waitKey(0)

        # Close program with keyboard 'x'
        if key%256 == 27:
            cv2.destroyAllWindows()
            break
        
def show_images():
    save()
    cropped_images()
    split_img()

    cv2.imshow('image1',cv2.imread('.\\data\\split1.jpg'))
    cv2.imshow('image2',cv2.imread('.\\data\\split2.jpg'))
    cv2.imshow('image3',cv2.imread('.\\data\\split3.jpg'))
    cv2.imshow('image4',cv2.imread('.\\data\\split4.jpg'))
    cv2.imshow('image5',cv2.imread('.\\data\\split5.jpg'))
    cv2.imshow('image6',cv2.imread('.\\data\\split6.jpg'))
    cv2.imshow('image7',cv2.imread('.\\data\\split7.jpg'))
    cv2.imshow('image8',cv2.imread('.\\data\\split8.jpg'))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    show_images()
    sleep(2)
    mapping()
    mosaic()