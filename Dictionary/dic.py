from tkinter import *
from PyDictionary import PyDictionary
import json

root=Tk()
root.geometry('250x200')

def find_meaning():
    word=e1.get()
    dic=PyDictionary()
    l1.config(text=str(dic.meaning(word)))

e1=Entry(root,font=('times 15',15,'bold'))
e1.grid(row=2,column=2)

btn=Button(root,text='Find meaning',command=find_meaning)
btn.grid(row=4,column=2)

l1=Label(root,text="",font='times 10')
l1.grid(row=6,column=2)

root.mainloop()