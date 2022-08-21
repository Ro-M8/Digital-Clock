from tkinter import Tk
from tkinter import Label
import time
import sys

master =Tk()
master.title("DGITAL CLOCK")

def get_time():
    timeVar =  time.strftime("%I:%M:%S  %p")   
    clock.config(text=timeVar)
    clock.after(200,get_time)


clock = Label(master, font=("Arial",50),bg="black",fg="white")
clock.pack()

get_time()

master.mainloop()