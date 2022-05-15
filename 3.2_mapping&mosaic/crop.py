import cv2

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
    cropped_img1 = crop_img(cv2.imread('.\\data\\frame1.jpg'), (600,600),(0.8,1))   
    cropped_img2 = crop_img(cv2.imread('.\\data\\frame2.jpg'), (600,600),(0.8,1))
    cropped_img3 = crop_img(cv2.imread('.\\data\\frame3.jpg'), (600,600),(0.8,1))
    cropped_img4 = crop_img(cv2.imread('.\\data\\frame4.jpg'), (600,600),(0.8,1))
 
    cv2.imwrite('.\\data\\frame1.jpg' , cropped_img1)
    cv2.imwrite('.\\data\\frame2.jpg' , cropped_img2)
    cv2.imwrite('.\\data\\frame3.jpg' , cropped_img3)
    cv2.imwrite('.\\data\\frame4.jpg' , cropped_img4)

if __name__=='__main__':
    cropped_images()
    
    