import imp
from mosaic import mosaic
from PressSave import save
from crop import crop_imgs
from cut2Parts import split_img
from time import sleep
from random8 import Display8imgs
from mapping import DrawLineWidget
import cv2

def mapping():
    draw_line_widgetk = DrawLineWidget()
    while True:
        cv2.imshow('image', draw_line_widgetk.show_image())
        key = cv2.waitKey(10)

        # Close program with keyboard 'esc'
        if key == 27:
            cv2.destroyAllWindows()
            break


if __name__=='__main__':
    imgs_list = save()
    imgs_cropped_list = crop_imgs(imgs_list)
    img8_list = split_img(imgs_cropped_list)
    sleep(1)
    mapping()
    Display8imgs(img8_list)
    mosaic(img8_list)
