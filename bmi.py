from tkinter import *

def bmi ():
    a = float(entry1.get())
    b = float(entry2.get())
    c = b/a**2 *10000
    print(c)
    label3 = Label(window , text = c , font = ('arial',20))
    label3.pack()
    
    if c <= 18.5:
        Label(window, text ='UNDER WEIGHT', font = ('arial',15)).pack()
    elif 18.5< c <=24.9 :
        Label(window, text ='NORMAL', font = ('arial',15)).pack()
    elif 25.0< c <29.9:
        Label(window, text ='OVER WEIGHT', font = ('arial',15)).pack()
    elif 30.0 < c <34.9:
        Label(window, text ='OBESE', font = ('arial',15)).pack()
    else :
        Label(window, text ='EXTREMELY OBSE', font = ('arial',15)).pack()



window = Tk()
window.geometry('320x320')

label1 = Label(window,text = 'height (m) :',font = ('arial, 15'))
label1.pack()

entry1 = Entry(window, bg = 'yellow',width=15,font = 20,)
entry1.pack()

label2 = Label(window,text = 'weight (kg) :',font = ('arial, 15'))
label2.pack()

entry2 = Entry(window, bg = 'yellow',width=15,font = 20)
entry2.pack()

button = Button (window,text = ' calculate BMI',font = ('arial',15),bd =5 , command = bmi)
button.pack()













window.mainloop()