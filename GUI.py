from tkinter import Button
from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from GUIR.mail import mailprint

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid,self).__init__(**kwargs)
        self.cols = 2

        
        self.submit = Button(text='2.1_flay transectline')
        self.submit.bind(on_press =self.press)
        self.add_widget(self.submit)



        self.submit = Button(text='2.3_Measure fish size')
        self.submit.bind(on_press =self.press)
        self.add_widget(self.submit)


        self.add_widget(Button(text='Hello 2'))
        self.add_widget(Button(text='World 2'))
        self.add_widget(Button(text='Hello 1'))
        self.add_widget(Button(text='World 1'))
        self.add_widget(Button(text='Hello 2'))
        self.add_widget(Button(text='World 2'))

    def press(self , instance):
        print("pressed") 

class MyApp(App):
    def build(self):
        return Grid()

if __name__ == '__main__':
    MyApp().run()