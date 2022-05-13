import cv2
import os
def cut(folder):
    cnt=1
    try:
        os.mkdir('after cut')
    except FileExistsError:
        pass
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            h= img.shape[0]
            half = h//2
            top = img[:half, :]
            bottom = img[half:, :]
            filename = str(cnt)+'.jpg'
            cv2.imwrite(os.path.join('after cut', filename), top)
            cnt += 1
            filename = str(cnt)+'.jpg'
            cv2.imwrite(os.path.join('after cut', filename), bottom)
            cnt += 1
cut("D:\shape\\befor cut")