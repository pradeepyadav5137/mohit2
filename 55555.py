from tkinter import *
from tkinter import messagebox 
root=Tk()
root.geometry("600x400+360+150")
root.resizable(1,1)

root.title("Calculator")


ii=PhotoImage(file="ccc.png")
i=Label(root,image=ii,bg="#FF9163")
i.place(x=0,y=0)


n1v=IntVar()
n2v=IntVar()
ans=Label(root,bg="white",padx=80,pady=20,font=("calibre",20))
ans.place(x=38,y=310)

def calc1():
    n=n1v.get()
    nn=n2v.get()
    a=n+nn
    ans.config(text=a)


def calc2():
    n=n1v.get()
    nn=n2v.get()
    ans.config(text=n-nn)
def calc3():
    n=n1v.get()
    nn=n2v.get()
    ans.config(text=n*nn)
def calc4():
    n=n1v.get()
    nn=n2v.get()
    if(nn==0):
        messagebox.showwarning("Error","Can't divide by 0")
    else:
        print(n/nn)
        ans.config(text=n/nn)
plusi=PhotoImage(file="+.png")
b1=Button(root,image=plusi,bg="#FF9163",command=calc1)
b1.place(x=40,y=200)

minusi=PhotoImage(file="-.png")
b2=Button(root,image=minusi,bg="#FF9163",command=calc2)
b2.place(x=170,y=200)

muli=PhotoImage(file="x.png")
b3=Button(root,image=muli,bg="#FF9163",command=calc3)
b3.place(x=300,y=200)

divi=PhotoImage(file="d.png")
b4=Button(root,image=divi,bg="#FF9163",command=calc4)
b4.place(x=440,y=200)

n1=Entry(root,bg="white",fg="black",font=("calibre",15),textvariable=n1v)
n1.place(x=300,y=60)

n2=Entry(root,bg="white",fg="black",font=("calibre",15),textvariable=n2v)
n2.place(x=300,y=140)



root.mainloop()