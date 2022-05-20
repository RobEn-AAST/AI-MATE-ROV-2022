import cv2

def torotate(imgs):
    
    imgs[0] = cv2.rotate(imgs[0], cv2.ROTATE_90_CLOCKWISE)
    imgs[1] = cv2.rotate(imgs[1], cv2.ROTATE_90_CLOCKWISE)
    imgs[2] = cv2.rotate(imgs[2], cv2.ROTATE_90_CLOCKWISE)
    imgs[3] = cv2.rotate(imgs[3], cv2.ROTATE_90_CLOCKWISE)

    return imgs


if __name__=='__main__':
    torotate()
