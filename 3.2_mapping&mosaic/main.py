import matplotlib.pyplot as plt
from tkinter import *
from mapping import *
from mosaic import *
from PressSave import *
from crop import *




def main():
    def mapping():
        ddraw_line_widget = DrawLineWidget()
        while True:
            cv2.imshow('image', ddraw_line_widget.show_image())
            key = cv2.waitKey(10)

            # Close program with keyboard 'x'
            if key%256 == 27:
                cv2.destroyAllWindows()
                exit(1)


    def show_images():
        save()
        cropped_images()
        # read images
        list_of_images=[]
        #karim should enter theee path himself the path is not final
        DirPath='K:/AI-MATE-ROV-2022/3.2_mapping&mosaic/data'
        Images=os.listdir(DirPath)
        for img in Images:
            imgpath=os.path.join(DirPath,img)
            image=cv2.imread(imgpath)
            list_of_images.append(image)
        img_1=cv2.imshow('img1',list_of_images[0])
        img_2=cv2.imshow('img2',list_of_images[1])
        img_3=cv2.imshow('img3',list_of_images[2])
        img_4=cv2.imshow('img4',list_of_images[4])
        img_5=cv2.imshow('img5',list_of_images[4])
        img_6=cv2.imshow('img6',list_of_images[5])
        img_7=cv2.imshow('img7',list_of_images[6])
        img_8=cv2.imshow('img8',list_of_images[7])


    root=Tk()
    root.geometry('1000x1000')
    root.title('mission 3.2')
    Button(root, text ="show images", command= show_images , height=3 ,width=20).place(x=50, y=150)
    Button(root, text ="mapping", command=mapping , height=3 ,width=20).place(x=50, y=250)
    Button(root, text ="mosaic", command= mosaic , height=3 ,width=20).place(x=50, y=350)
    root.mainloop()

if __name__=='__main__':
    main()