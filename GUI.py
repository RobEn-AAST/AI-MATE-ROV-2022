import tkinter as tk
from tkinter import *
import threading
import os

# from grid import start_drawing 

cam = "0" # camera 0

def mapping_exec():
    print("im here ")
    os.system("python ./mapping_mosaic/mapping.py") 
    print("im out ")

def Healthy_exec():
    os.system("python ./mapping_mosaic/mapping.py") 

def MFish_exec():
    os.system("python ./mapping_mosaic/mapping.py") 

def Fltransectline_exec():
    os.system("python ./mapping_mosaic/mapping.py") 

def PIDS_exec():
    os.system("python ./mapping_mosaic/mapping.py") 


window = tk.Tk()
window.geometry('700x700')
window.title("run rov")

   # the button for transect line mission 

button1 = tk.Button(window, text = "FLYING  \n TRANSECT \nLINE" , fg = "blue", width = 18, height = 8, command = lambda : print('x'))
button1.place(x=200, y= 120)

   # the button for color detection mission

button2 = tk.Button(window, text = "CORAL COLOR" , fg = "blue", width = 18, height = 8, command = lambda : print('x'))
button2.place(x=200, y= 300)


   # the button for stitching mission


button3 = tk.Button(window, text = "STITCHING" , fg = "blue", width = 18, height = 8, command = lambda : print('x'))
button3.place(x=400, y= 120)

  

label = tk.Label(window, text = "MISSIONS" , fg = "green",font="15")
label.place(x= 300, y= 50)




button4 = tk.Button(window, text = "GRID \n TASK" , fg = "blue", width = 18, height = 8)
button4.place(x=400, y= 300)

button5 = tk.Button(window, text = "Manual\n Coral Reef" , fg = "blue", width = 18, height = 8, command = lambda : print('x'))
button5.place(x=200, y= 480)

button6 = tk.Button(window, text = "Mapping" , fg = "blue", width = 18, height = 8, command = lambda :mapping_exec())
button6.place(x=400, y= 480)


window.mainloop()





