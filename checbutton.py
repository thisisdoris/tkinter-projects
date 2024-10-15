from tkinter import *
def display():
    if(x.get()==1):
        print('you agreed.')
    else:
        print("you didn't agree:(")  
window = Tk()

window.geometry('640x640')
x = IntVar()
check_button =Checkbutton(window, text = "i agree",variable= x,command=display )
check_button.pack()



window.mainloop()