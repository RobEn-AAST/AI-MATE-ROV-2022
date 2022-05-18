import cv2

def crop_imgs(img,dim = (600,600) ,scale= (0.95,1)):
    
    for j in range(4):
        img[j] = cv2.resize(img[j],dim,interpolation=cv2.INTER_LINEAR)
        ym, xm = img[j].shape[0] / 2, img[j].shape[1] / 2
        hight, width = img[j].shape[0] * scale[0], img[j].shape[1] * scale[1]
        x1, x2 = xm - width / 2, xm + width / 2
        y1, y2 = ym - hight / 2, ym + hight / 2
        img[j] = img[j][int(y1):int(y2), int(x1):int(x2)]
        
        return img;

if __name__=='__main__':
    crop_imgs()
    
    
