import tkinter as tk
from tkinter import *
import threading
import os

# from grid import start_drawing 
def script_exec(script_name):
    os.system("python ./"+script_name)


def start_script_thread(script_name):
    camera_read = threading.Thread(target=script_exec, args=(script_name,))
    camera_read.daemon = False
    # camera_read.daemon = True
    camera_read.start()


window = tk.Tk()
window.geometry('950x500')
window.title("run rov")

   # the button for transect line mission 
button1 = tk.Button(window, text = "FLYING  \n TRANSECT \nLINE" , fg = "blue", width = 18, height = 8, command = lambda :start_script_thread("flyTransect/main.py"))
button1.place(x=100, y= 120)

   # the button for color detection mission
button2 = tk.Button(window, text = "Measure Fish" , fg = "blue", width = 18, height = 8, command = lambda :start_script_thread("measureFish/mes.py"))
button2.place(x=500, y= 120)

   # the button for stitching mission
button3 = tk.Button(window, text = "Docking" , fg = "blue", width = 18, height = 8, command = lambda :start_script_thread("dockingStation/movement.py"))
button3.place(x=300, y= 120)


label = tk.Label(window, text = "MISSIONS" , fg = "green",font="15")
label.place(x= 425, y= 50)


button4 = tk.Button(window, text = "Measuring \n WRECK" , fg = "blue", width = 18, height = 8, command = lambda :start_script_thread("mosaicAndMapping/measureWreck.py"))
button4.place(x=700, y= 120)


# button5 = tk.Button(window, text = "Nothing " , fg = "blue", width = 18, height = 8, command = lambda : print('x'))
# button5.place(x=100, y= 320)


# button6 = tk.Button(window, text = "Mapping" , fg = "blue", width = 18, height = 8, command = lambda :start_script_thread("mosaicAndMapping/mapping.py"))
# button6.place(x=300, y= 320)


button7 = tk.Button(window, text = "Float" , fg = "blue", width = 18, height = 8, command = lambda :start_script_thread("MeasureInFloatV_H/main.py"))
button7.place(x=500, y= 320)


button8 = tk.Button(window, text = "Mosaic" , fg = "blue", width = 18, height = 8, command = lambda :start_script_thread("mosaicAndMapping/main.py"))
button8.place(x=300, y= 320)


window.mainloop()