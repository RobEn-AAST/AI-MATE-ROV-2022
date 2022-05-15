import cv2

def split_img():
    count=1
    for i in range(1,5,1):
        IMg_path='.\\data\\frame'+str(i)+'.jpg'
        img = cv2.imread(IMg_path)
        if img is not None:
            h= img.shape[0]
            half = h//2
            top = img[:half, :]
            bottom = img[half:, :]
            filename = '.\\data\\split'+str(count)+'.jpg'
            cv2.imwrite(filename,top)
            count += 1
            filename = '.\\data\\split'+str(count)+'.jpg'
            cv2.imwrite(filename, bottom)
            count += 1

if __name__=='__main__':
    split_img()
