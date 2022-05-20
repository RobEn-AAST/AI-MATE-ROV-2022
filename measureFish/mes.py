import cv2
from functools import total_ordering
from tkinter import *
from random import randint
import tkinter as tk  
from functools import partial
from rovlib.cameras import RovCam
import os




def destroy():
    global glob_centimeters
    f = open("length.txt", "a")
    f.write(str(glob_centimeters)+os.linesep)
    glob_centimeters = 0
    f.close()
    root.destroy()


counter = 0

f = open("length.txt", "w")
f.write("")
f.close()
glob_centimeters = 0
while True:
    # vid = cv2.VideoCapture(0)
    vid = RovCam(RovCam.FRONT)
    img = None
    valid = False
    counter+=1
    while True:
        if valid:
            break
        img = vid.read()
        # _, img = vid.read()
        img_copied = img.copy()
        # print("do u like this frame ? a / x")
        cv2.putText(img = img_copied, text = 'click s to take snapshot', org=(15,30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.2, color=(255,0,0), thickness=3)

        cv2.imshow("q", img_copied)
        if cv2.waitKey(4) == ord('s'):
            img_copied = img.copy()
            cv2.putText(img = img_copied, text = 'approve : a deny : x', org=(15,30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.2, color=(255,0,0), thickness=3)
            cv2.imshow("q", img_copied)
            # while True:
            key_in = cv2.waitKey(0)
            if key_in == ord('a'):
                valid = True
                img = cv2.resize(img, (700,700))
                cv2.imwrite("a.png",img)
                break
            if key_in == ord('x'):
                continue
            if key_in == 27:
                exit()


    root = Tk()
    root.geometry("700x700")
    

    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    #setting tkinter window size
    root.geometry("%dx%d" % (width, height))
    root.title("Geeeks For Geeks")
    root.bind('<Escape>',lambda e: destroy())
    
    # Add image file
    bg = PhotoImage(file = "a.png")
    
    #root.configure(background='DeepSkyBlue4')

    class DrawLine:
        def __init__(self,master):

            self.ref_cm = 2.3
            self.ref_pix = 0

            self.referencing = True
            
            self.canvas = Canvas(master, width=1500, height=1500)
            self.canvas.bind("<Button-1>", lambda e: self._move(e.x,e.y))
            img = bg    
            self.canvas.create_image(50,30, anchor=NW, image=bg) 
            self.previous_pos = None
            self.total_length = 0
            self.t = Label(master, text=f"Total Length: {self.total_length} pixels",font=('Arial',12),pady=5,bg="DeepSkyBlue4",fg="white")
            self.t.pack()
            self.turn = 0
            self.canvas.pack(side="left")


            self.e1 = Entry(self.canvas)
            self.e2 = Entry(self.canvas)
            self.e3 = Entry(self.canvas)
            self.e4 = Entry(self.canvas)
        

            label2 = tk.Label(root, text="M = N * a * L^b", font="5").place(x=1000, y=80) 

            label3 = tk.Label(root, text="a which is determined by species", font="5").place(x=800, y=120)  
            self.canvas.create_window(1320,100,window=self.e1)
            label4 = tk.Label(root, text="b which is determined by environmental conditions", font="5").place(x=800, y=160)
            self.canvas.create_window(1320,140,window=self.e2)
            label5 = tk.Label(root, text="N is the number of fish in pen", font="5").place(x=800, y=200) 
            self.canvas.create_window(1320,180,window=self.e3)
            label6 = tk.Label(root, text="L is the average length (centimeters)", font="5").place(x=800, y=240)   
            self.canvas.create_window(1320,220,window=self.e4)

            button1 = tk.Button(root, text = "calculate" , fg = "blue", width = 10, height = 5, command = self.result)
            button1.place(x=1000, y= 290)

            self.my_string_var = StringVar()
            # self.my_string_var.set("result = ")
            label7 = tk.Label(root, text="result = ", font="20", textvariable = self.my_string_var).place(x=800, y=350) 
            self.my_string_var.set("result = ")

            #result = int(e3)*int(e1)*int(e4)^int(e2) 
            #self.config(text="Result = %d" % result)  

        def result(self):
            e1t = self.e1.get()
            e2t = self.e2.get()
            e3t = self.e3.get()
            e4t = self.e4.get()
            print(e1t, e2t, e3t, e4t)
            result = float(e3t)*float(e1t)*(float(e4t)**float(e2t))*10**-3
            result= "{:.2f}".format(result)
            print(result)
            self.my_string_var.set("result = " + str(result))   
    

        def _move(self,new_x,new_y):
            global glob_centimeters
            new_length = 0
            if(self.turn == 2):
                self.turn = 0
                self.previous_pos = None


            self.turn += 1
            if(self.referencing):
                self.canvas.create_oval(new_x + 5, new_y + 5, new_x - 5, new_y - 5, width=0, fill='blue')
            else:
                self.canvas.create_oval(new_x + 5, new_y + 5, new_x - 5, new_y - 5, width=0, fill='red')
            if self.previous_pos:
                old_x, old_y = self.previous_pos
                self.canvas.create_line(old_x, old_y, new_x, new_y, width=2)
                new_length = ((new_x - old_x) ** 2 + (new_y - old_y) ** 2) ** (1 / 2) 
                if (not self.referencing):
                    self.total_length += new_length

                    self.centimeters =  self.total_length * self.ref_cm / self.ref_pix
                    print(self.centimeters)
                    glob_centimeters += self.centimeters
                    self.t.config(text=f"Total Length: {round(self.centimeters ,2)} cm")
            self.previous_pos = (new_x, new_y)

            if(self.turn == 2 and self.referencing):
                self.ref_pix = new_length
                self.total_length = 0
                self.referencing = False


    

    DrawLine(root)

    root.mainloop()
    if cv2.waitKey(4) == 27:
        cv2.destroyAllWindows()
        break
