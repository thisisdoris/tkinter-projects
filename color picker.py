#color picker 
from tkinter import *
from tkinter import colorchooser
window = Tk()
window.geometry('420x420')
def click():
    color = colorchooser.askcolor()
    colorHEX = color[1]
    window.config(bg=colorHEX)
    print(color)
button = Button(window,text= 'click me ', command= click)
button.pack()





window.mainloop()