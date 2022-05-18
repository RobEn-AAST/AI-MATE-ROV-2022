import cv2
def split_img(img):
    list=[]
    for i in (img):
        im = i
        if im is not None:
            h= im.shape[0]
            half = h//2
            top = im[:half, :]
            bottom = im[half:, :]
            list.append(top)
            list.append(bottom)
    datasave(list)
    return list
def datasave(imgs):
    count=1
    for i in (imgs):
        im = i
        if im is not None:
            filename = '.\\data\\split'+str(count)+'.jpg'
            cv2.imwrite(filename, im)
            count += 1
            
if __name__=='__main__':
    split_img()