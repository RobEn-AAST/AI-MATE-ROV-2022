import cv2

def crop_img(img,dim ,scale):

    img = cv2.resize(img,dim,interpolation=cv2.INTER_LINEAR)
    ym, xm = img.shape[0] / 2, img.shape[1] / 2
    hight, width = img.shape[0] * scale[0], img.shape[1] * scale[1]
    x1, x2 = xm - width / 2, xm + width / 2
    y1, y2 = ym - hight / 2, ym + hight / 2
    cropped_img = img[int(y1):int(y2), int(x1):int(x2)]

    return cropped_img

img = cv2.imread('img.jpg')
cropped_img = crop_img(img, (600,600),(0.8,1))
#cv2.imshow('c',cropped_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

