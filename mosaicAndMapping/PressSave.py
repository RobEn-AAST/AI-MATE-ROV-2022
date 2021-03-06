import cv2
import os
from rovlib.cameras import RovCam

def rescale(frame,scale=0.6):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions, interpolation=cv2.INTER_AREA)

def save():
    list_of_images=[]
    # frame
    currentframe = 1
    cam = RovCam(RovCam.MISC1)

    try:
        # creating a folder named data
        if not os.path.exists('./data'):
            os.makedirs('./data')

    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    # Read the video from specified path

    while True:
        frame = cam.read()
        frame_resized =rescale(frame)
        cv2.imshow('video resized',frame_resized)
        
        k = cv2.waitKey(10)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        
        elif k%256==32:
            #press space to delete
            while 1:
                try:
                    no_of_images_to_be_removed=(input("the no of previos photos to remove"))
                    if(no_of_images_to_be_removed=='q'or no_of_images_to_be_removed=='Q'):
                        break
                    no_of_images_to_be_removed=int(no_of_images_to_be_removed)
                    if(no_of_images_to_be_removed<=(currentframe-1)):
                        for images in range(currentframe*1,currentframe-(no_of_images_to_be_removed+1),-1):
                            try:
                                if(os.path.exists('.\\data\\frame' + str(images) + '.jpg')):
                                    os.remove('.\\data\\frame' + str(images) + '.jpg')
                                    currentframe-=1
                            except Exception:
                                print('doesnt exist')        
                                break
                        break
                    else:
                        print('out of range')
                        continue     
                except Exception:
                    print("invalid input")
                    continue         
                    
        elif k%256 == 115 or k%256 == 83: 
            # press s or S
            print(f'creating img {currentframe} ')
            list_of_images.append(frame)
            currentframe+=1
    del cam
    cv2.destroyAllWindows
    return list_of_images;


if __name__=='__main__':
    save()

