from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

root = Tk()
root.geometry("600x300")
root.title("Student Data")
i = PhotoImage(file="c.png")
root.iconphoto(True, i)
root.resizable(1, 1)

def getdata():
    roll = rn_c.get()
    e = e_e.get()
    nn = name_e.get()
    c = course_c.get()
    ss = sem_s.get()
    l = [roll, e, nn, c, ss]

    for i in l:
        if i == "":
            messagebox.showwarning("Error", "Fill all the Entries")
            break
    else:
        file = open("student.csv", "a", newline="\n")
        w = csv.writer(file)
        w.writerow(l)
        file.close()

        rn_c.set("")
        e_e.set("")
        namevar.set("")
        course_c.set("")
        sem_s.delete(0, END)

        messagebox.showinfo("Entry", "The student data has been stored in the database successfully")

namevar = StringVar()
f = Frame(root)
f.pack()

f_1 = LabelFrame(f, text="Student Info")
f_1.grid(row=0, column=0)

rn = Label(f_1, text="Roll No.")
enr = Label(f_1, text="Enrollment No.")
name = Label(f_1, text="Student Name")
sem = Label(f_1, text="Semester")

rn.grid(row=0, column=0)
enr.grid(row=0, column=1)
name.grid(row=0, column=2)
sem.grid(row=2, column=1)

rn_c = ttk.Combobox(f_1, values=list(range(1, 101)))
rn_c.grid(row=1, column=0)

e_e = ttk.Combobox(f_1, values=["E{:03d}".format(i) for i in range(1, 101)], font=("calibre"))
e_e.grid(row=1, column=1)

name_e = Entry(f_1, textvariable=namevar, font=("calibre"))
name_e.grid(row=1, column=2)

sem_s = Spinbox(f_1, from_=1, to=8, font=("calibre", 10))
sem_s.grid(row=3, column=1)

course = Label(f_1, text="Course")
course.grid(row=2, column=0)

course_c = ttk.Combobox(f_1, values=["B.A", "B.A. Prog", "BSc. Maths", "B.A. History", "B.A. English",
                                     "B.A. Political Science", "BSc. Physics", "BSc. Computer Science",
                                     "Bsc. Physical Science CS", "B. Com.", "B.Com. Prog"])
course_c.grid(row=3, column=0)

for widget in f_1.winfo_children():
    widget.grid_configure(padx=10, pady=5)

b = Button(f, text="Submit", command=getdata)
b.grid(row=3, column=0, sticky="news", pady=20)

def search():
    s = Tk()
    s.geometry("300x400")
    f = Frame(s)
    f.pack()

    f_1 = LabelFrame(f, text="Student Info")
    f_1.grid(row=0, column=0)

    rn = Label(f_1, text="Roll No.")
    rn.grid(row=0, column=0, padx=10, pady=5)
    rn_c2 = ttk.Combobox(f_1, values=list(range(1, 101)))
    rn_c2.grid(row=1, column=0, padx=20, pady=30)

    nl = Label(f, text="")
    nl.grid(row=2, column=0, sticky="news")

    def find():
        rrr = rn_c2.get()
        file = open("student.csv", "r", newline="\n")
        r = csv.reader(file)
        for i in r:
            if i[0] == rrr:
                nl.configure(text=i)
                break
        else:
            nl.configure(text="No record with such roll number found")

    sb = Button(f, text="Search", command=find)
    sb.grid(row=1, column=0, sticky="news")

    s.mainloop()

b2 = Button(f, text="Search for a record", command=search)
b2.grid(row=4, column=0, pady=20)

root.mainloop()
