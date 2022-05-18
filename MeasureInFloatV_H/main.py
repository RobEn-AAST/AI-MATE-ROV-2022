from tkinter import *
import math

win=Tk()
win.geometry("600x350")

def cal_square():
   v=float(a.get())
   angle=float(b.get())
   t=float(c.get())
   angle=(angle-90)*math.pi/180
   v=v*3.6
   d=v*t
   Vdist=d*math.cos(angle)
   label.config(text= round(Vdist, 3))

   Hdist=d*math.sin(angle)
   labe2.config(text= round(Hdist, 3))

   svdist=Vdist/2
   labe3.config(text= round(svdist, 1))
   shdist=Hdist/2
   labe4.config(text= round(shdist, 1))

   

# Create an Entry widget
Label(win, text="Velocity:", font=('Calibri 15')).place(x= 20, y= 20)
a=Entry(win)
a.place(x= 100, y= 30)

Label(win, text="Angle:", font=('Calibri 15')).place(x= 20, y= 60)
b=Entry(win)
b.place(x= 100, y= 70)
Label(win, text="Time :", font=('Calibri 15')).place(x= 20, y= 100)
c=Entry(win)
c.place(x= 100, y= 110)


label = Label( win, text="Vertical in km:", font=('Calibri 15') )
label.place(x= 30, y= 160)

label=Label(win, font=('Calibri 15'))
label.place(x= 190, y= 160)

labe2 = Label( win, text="horizontal in km:", font=('Calibri 15') )
labe2.place(x= 30, y= 200)

labe2=Label(win, font=('Calibri 15'))
labe2.place(x= 190, y= 200)

labe3 = Label( win, text="vertical in square:", font=('Calibri 15') )
labe3.place(x= 280, y= 160)

labe3=Label(win, font=('Calibri 15'))
labe3.place(x= 470, y= 160)

labe4 = Label( win, text="horizontal in square:", font=('Calibri 15') )
labe4.place(x= 280, y= 200)

labe4=Label(win, font=('Calibri 15'))
labe4.place(x= 470, y= 200)

Button(win, text="CALCULATE ", command=cal_square).place(x= 220, y= 280)

win.mainloop()
