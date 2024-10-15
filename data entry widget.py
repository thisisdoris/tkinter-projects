#data entry widget 
from tkinter import *
window = Tk()
window.geometry('940x320')
def submit():
    yusername=entry.get()
    print(f'hello {yusername}')
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)


window.title('dataentry widget')
entry = Entry(window,font=('arial', 40),fg='pink',bg='black')
entry.pack(side=LEFT)
#entry.config(show='*')
#entry.insert(0,'hello')  #از قبل مقدار داشته باشه
submit_button=Button(window,text='submit',font=('times new roman',20),command= submit)
submit_button.pack(side=RIGHT)
delete_button=Button(window,text='delete',font=('times new roman',20),command=delete)
delete_button.pack(side=RIGHT)
backspace_button= Button(window,text='backspace',font=('times new roman',20),command=backspace)
backspace_button.pack(side=RIGHT)

















window.mainloop()