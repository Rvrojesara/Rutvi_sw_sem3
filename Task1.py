import tkinter as tk
from tkinter import*

root=Tk()
root.geometry("500x500")

def Menu():
    print(Button1)

w=Label(root,text="Menu",font="40").pack()

Checkbutton1=tk.IntVar()
Checkbutton2=tk.IntVar()
Checkbutton3=tk.IntVar()
Checkbutton4=tk.IntVar()
Checkbutton5=tk.IntVar()

Button1=Checkbutton(root,text="Pizza -> 500",variable=Checkbutton1,onvalue=1,offvalue=0,
height=2,width=10)

Button2=Checkbutton(root,text="Dosa -> 200",variable=Checkbutton2,onvalue=1,offvalue=0,
height=2,width=10)

Button3=Checkbutton(root,text="Maggi -> 100",variable=Checkbutton3,onvalue=1,offvalue=0,
height=2,width=10)

Button4=Checkbutton(root,text="Cold Drink -> 150",variable=Checkbutton4,onvalue=1,offvalue=0,
height=2,width=15)

Button5=Checkbutton(root,text="Calculate",variable=Checkbutton5,onvalue=1,offvalue=0,
height=2,width=15)

Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()

root.mainloop()