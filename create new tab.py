from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry('420x420')
notebook = ttk.Notebook(window)
tab1= Frame(notebook)
tab2= Frame(notebook)
notebook.add(tab1,text= 'tab 1')
notebook.add(tab2 , text = 'tab 2')
notebook.pack(expand= TRUE, fill= BOTH)
Label(tab1, text= ' hello this is tab 1 ', width=50,height=25, bg= '#123456').pack()
Label(tab2, text= ' hello this is tab 2 ', width=50,height=25,bg= '#365412').pack()








window.mainloop()