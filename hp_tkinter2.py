import tkinter
from tkinter import*
win=tkinter.Tk()
v=StringVar()
w=Label(win,textvariable=v,fg="red",bg="yellow",font=("vivaldi",20,"bold"),anchor=N,justify=LEFT)
v.set("Label can be made using tkinter \n\t --by HP JK")
w.pack()
print(v.get)
win.mainloop()
