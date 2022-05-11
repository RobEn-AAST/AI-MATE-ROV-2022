import cv2
import os


def rescale(frame,scale=0.6):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions, interpolation=cv2.INTER_AREA)

def save():

    # frame
    currentframe = 1
    cam = cv2.VideoCapture(0)

    try:
        # creating a folder named data
        if not os.path.exists('K:/AI-MATE-ROV-2022/3.2_mapping&mosaic/data'):
            os.makedirs('K:/AI-MATE-ROV-2022/3.2_mapping&mosaic/data')

    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    # Read the video from specified path

    while True:
        ret, frame = cam.read()
        frame_resized =rescale(frame)
        cv2.imshow('video resized',frame_resized)
        if not ret:
            break
        k = cv2.waitKey(10)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 115 or k%256 == 83: 
            # press s or S
            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += 1
    cam.release()

    cv2.destroyAllWindows

if __name__=='__main__':
    save()

