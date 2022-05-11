from mapping import *
from mosaic import *
from PressSave import *
from crop import *

def mapping():
    ddraw_line_widget = DrawLineWidget()
    while True:
        cv2.imshow('image', ddraw_line_widget.show_image())
        key = cv2.waitKey(10)

        # Close program with keyboard 'esc'
        if key%256 == 27:
            cv2.destroyAllWindows()
            break


def show_images():
    save()
    cropped_images()

    cv2.imshow('img1',cv2.imread('./data/frame8.jpg'))
    cv2.imshow('img2',cv2.imread('./data/frame8.jpg'))
    cv2.imshow('img3',cv2.imread('./data/frame8.jpg'))
    cv2.imshow('img4',cv2.imread('./data/frame8.jpg'))
    cv2.imshow('img5',cv2.imread('./data/frame8.jpg'))
    cv2.imshow('img6',cv2.imread('./data/frame8.jpg'))
    cv2.imshow('img7',cv2.imread('./data/frame8.jpg'))
    cv2.imshow('img8',cv2.imread('./data/frame8.jpg'))


if __name__=='__main__':
    show_images()
    mapping()
    mosaic()