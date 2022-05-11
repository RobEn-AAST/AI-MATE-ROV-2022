import cv2
import os
import matplotlib.pyplot as plt

def crop_img(img,dim ,scale):
    for j in range(8):
        img = cv2.resize(img,dim,interpolation=cv2.INTER_LINEAR)
        ym, xm = img.shape[0] / 2, img.shape[1] / 2
        hight, width = img.shape[0] * scale[0], img.shape[1] * scale[1]
        x1, x2 = xm - width / 2, xm + width / 2
        y1, y2 = ym - hight / 2, ym + hight / 2
        cropped_img = img[int(y1):int(y2), int(x1):int(x2)]
        return cropped_img;

def cropped_images():
    # read images
    list_of_images=[]
    #karim should enter theee path himself the path is not final
    DirPath='K:/AI-MATE-ROV-2022/3.2_mapping&mosaic/data'
    Images=os.listdir(DirPath)

    for img in Images:
        imgpath=os.path.join(DirPath,img)
        image=cv2.imread(imgpath)
        list_of_images.append(image)
    
    for i in range(8):
        cropped_img = crop_img(list_of_images[i], (600,600),(0.8,1))
        name = './data/frame' + str(i+1) + '.jpg'
        cv2.imwrite(name, cropped_img)

if __name__=='__main__':
    cropped_images()
    