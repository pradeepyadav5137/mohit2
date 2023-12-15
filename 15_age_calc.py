from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime

t=datetime.datetime.now()
cd=t.day
cm=t.month
cy=t.year
print(cd,cm,cy)

dates=list(range(1,32))
months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]
k=list(range(1,13))

key_value=dict(zip(months,k))


l31=["January", "March", "May",
    "July", "August",
    "October","December"]

l30=["April", "June", "September", "November"]

l29=["February"]
years = list(range(2023,1900,-1))

def get():
    d=ds.get()
    m=ms.get()
    y=ys.get()

    l=[d,m,y]
    for i in l:
        if i =="":
            messagebox.showwarning("Error","Please Enter date")
            break
    
    if(d=='31' and (m not in l31)):
        messagebox.showwarning("Error","Incorrect date please Re-Enter Date")
    elif(d=='29' and(m=="February" and (int(y)%4!=0))):
        messagebox.showwarning("Error","Incorrect date please Re-Enter Date")
    else:
        y_year=cy-int(y)
        m_month=cm-key_value[m]
        d_day=cd-int(d)

        age_l.configure(text="The Age is :"+str(y_year))

root=Tk()
root.geometry("560x200")
root.resizable(0,0)
root.title("Age Calculator")

f=Frame(root)
f.pack()

f1=LabelFrame(f,text="Date of Birth")
f1.grid(row=0,column=0,sticky="news")

d=Label(f1,text="Date",font=("Comic Sans MS",10,"bold"))
d.grid(row=0,column=0)

m=Label(f1,text="Month",font=("Comic Sans MS",10,"bold"))
m.grid(row=0,column=1)

y=Label(f1,text="Year",font=("Comic Sans MS",10,"bold"))
y.grid(row=0,column=2)

ds=ttk.Combobox(f1,values=dates)
ds.grid(row=1,column=0)

ms=ttk.Combobox(f1,values=months)
ms.grid(row=1,column=1)

ys=ttk.Combobox(f1,values=years)
ys.grid(row=1,column=2)

for widget in f1.winfo_children():
    widget.grid_configure(padx=20,pady=5)

b=Button(f,text="Calculate",command=get)
b.grid(row=1,column=0,sticky="news",pady=20)

age_l=Label(f,text="The Age is : ")
age_l.grid(row=2,column=0,sticky="news")

root.mainloop()