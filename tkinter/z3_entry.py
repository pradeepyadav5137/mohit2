from tkinter import *
from time import *
import csv
file=open("13.csv","a")

root=Tk()
root.geometry("500x200+360+150")
root.resizable(1,1)
root.title("Entry")
ii=PhotoImage(file="bank1.png")
root.iconphoto(True,ii)
f=Frame(root,bg="#acd4fa")
f.pack(anchor=N,fill=BOTH,expand=400)
usr=Label(f,text="Username",font=("calibre",20,"bold"),bg="#acd4fa")
pas=Label(f,text="Password",font=("calibre",20,"bold"),bg="#acd4fa")

usrval=StringVar()
pasval=StringVar()
usre=Entry(f,textvariable=usrval,font=("calibre",15,"bold"))
pase=Entry(f,textvariable=pasval,font=("calibre",15,"bold"),show="*")

def func():
    
    ok=Tk()
    ok.geometry("240x100+560+320")
    ok.minsize(200,100)
    ok.maxsize(222,150)
    ok.resizable(0,0)
    l=Label(ok,text="Thanks for registering ",font=("calibre",15,"bold"))
    l.pack(anchor=CENTER,ipadx=0,ipady=100)
    ok.mainloop()

def getit():
    u=usre.get()
    p=pase.get()

    usrval.set("")
    pasval.set("")

    x=check(u,p)
    if x!=1:
        w=csv.writer(file)
        w.writerow([u,p])
        func()

def check(a,b):
    a=str(a);b=str(b)
    a=a.strip()
    b=b.strip()

    if (len(a)<=3 or len(b)<=5):
        new=Tk()
        new.geometry("440x100+560+320")
        new.resizable(0,0)
        l=Label(new,text="""The username should of atleast of 4 characters and 
        password must be of atleast of 6 characters""",font=("calibre",10,"bold"))
        l.pack(anchor=CENTER,ipadx=0,ipady=100)
        new.mainloop()
        return 1
s=Button(f,text="Submit",font=("calibre",15,"bold"),command=getit)

usr.grid(row=0,column=0,ipadx=40,ipady=30)
usre.grid(row=0,column=1)
pas.grid(row=1,column=0)
pase.grid(row=1,column=1)
s.grid(row=2,column=1)

root.mainloop()