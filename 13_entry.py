from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

root=Tk()
root.geometry("600x430")
root.title("Event registration form")
i=PhotoImage(file="c.png")
root.iconphoto(True,i)
root.resizable(1,1)

def getdata():
    
    t=title_c.get()
    u=usrn_e.get()
    l=lstn_e.get()
    a=age_spin.get()

    y=yc.get()
    s=sems.get()
    c=course_c.get()
    lst=[t,u,l,a,y,s,c]

    ttick=tickv.get()
   
    c=0
    for i in lst:
        if(i==""):
            c+=1
    print(c)
    if(ttick=="Not Registered"):
        messagebox.showwarning("Warning","Please check the tick box")

    elif(c!=0):
        messagebox.showwarning("Warning","Please fill up all the Enteries")
    else:
        file=open("13_register.csv","a",newline="\n")
        w=csv.writer(file)
        w.writerows([lst])

f=Frame(root)
f.pack()

f_1=LabelFrame(f,text="User Info",)
f_1.grid(row=0,column=0)

title=Label(f_1,text="Title")
usrn=Label(f_1,text="First Name")
lstn=Label(f_1,text="Last Name")
age=Label(f_1,text="Age")


title.grid(row=0,column=0)
usrn.grid(row=0,column=1)
lstn.grid(row=0,column=2)
age.grid(row=2,column=0)

title_c=ttk.Combobox(f_1,values=["","Dr.","Mr.","Mrs."])
title_c.grid(row=1,column=0)

usrn_e=Entry(f_1,font=("calibre"))
usrn_e.grid(row=1,column=1)

lstn_e=Entry(f_1,font=("calibre"))
lstn_e.grid(row=1,column=2)

age_spin=Spinbox(f_1,from_=10, to=150,font=("calibre",10))
age_spin.grid(row=3,column=0)

for widget in f_1.winfo_children():
    widget.grid_configure(padx=10,pady=5)

f_2=LabelFrame(f,text="Educational Info")
f_2.grid(row=1,column=0,sticky="news",pady=20)

year=Label(f_2,text="Year")
year.grid(row=0,column=0)

yc=ttk.Combobox(f_2,values=['I',"II","III","IV"])
yc.grid(row=1,column=0)

sem=Label(f_2,text="Semester")
sem.grid(row=0,column=1)

sems=Spinbox(f_2,from_=1, to=8)
sems.grid(row=1,column=1)

course=Label(f_2,text="Course")
course.grid(row=0,column=2)

course_c=ttk.Combobox(f_2,values=["B.A","B.A. Prog","BSc. Maths","B.A. History","B.A. English",
                                  "B.A. Political Science"
                                  ,"BSc. Physics","BSc. Computer Science"
                                  ,"Bsc. Physical Science CS","B. Com.","B.Com. Prog"])
course_c.grid(row=1,column=2)

for widget in f_2.winfo_children():
    widget.grid_configure(padx=20,pady=10) 


f_3=LabelFrame(f,text="Confirm Registration")
f_3.grid(row=2,column=0,sticky="news")

l=Label(f_3,text=""" "I hereby declare that all the above information filled by
me is correct and I bear full responsibility in case of any false information
provided that may or may not cancel my registration in the event." """)
l.pack(anchor="nw")

tickv=StringVar()
tick=Checkbutton(f_3,variable=tickv,text="Click to register",
                 onvalue="Registered",offvalue="Not Registered")
tick.pack(anchor="nw",padx=45)

b=Button(f,text="Submit",command=getdata)
b.grid(row=3,column=0,sticky="news",pady=20)
root.mainloop()