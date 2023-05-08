#creating for GUI-Digital clock Project

from tkinter import *
#importing strftime function to capturing system time.

from time import strftime
digital_clock=Tk()
digital_clock.geometry("600x300")
digital_clock.title("Digital Clock")

#display time on the label using this function

def time():
    string=strftime('%H:%M:%S%p')
    Label.config(text=string)
    Label.after(1000,time)

#increase the user experience designing the label widget

Label=Label(digital_clock,font=('calibri',40,'bold'),
        background='#AA0000',
        foreground='white')

#clock at the centre of the tkinter window

Label.pack(anchor='center')
time()
mainloop()

