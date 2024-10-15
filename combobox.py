from tkinter import ttk
from tkinter import Tk
window = Tk()
window.geometry('200x200')
months = ['1','2','3','4']
a = ttk.Combobox(width= 50, value = months)
a.pack()



window.mainloop()
