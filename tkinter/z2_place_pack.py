from tkinter import *
from time import *
root=Tk()
root.geometry("200x200")        # +360+100  incdicates the positioning of the windwow
                                        #       360 shifted on X axis     100 on Y axis
root.resizable(1,1)         # 1,1 indicates True on x and True on y

root.minsize(100,150)
root.maxsize(650,450)       #   width , height

l=Label(root,text="Hello this is a Label",font="helvetica")
l.place(relx=0.15 , rely=0.2, anchor=NW)

b=Button(root,text="Button")
b.place(relx=0.5,rely=0.5,anchor=NW)
root.mainloop()