import imp
from mosaic import mosaic
from PressSave import save
from crop import crop_imgs
from cut2Parts import split_img
from time import sleep
from random8 import Display8imgs
import cv2

def show_images():
    imgs_list = save()
    imgs_cropped_list = crop_imgs(imgs_list)
    img8_list = split_img(imgs_cropped_list)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img8_list


if __name__=='__main__':
    img8_list = show_images()
    sleep(2)
    Display8imgs(img8_list)
    mosaic(img8_list)
