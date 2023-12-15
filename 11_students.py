r=["Roll no.", "Enrollment no.", "Name", "Course", "Semester"]

s=[[  1,  "E001",   "John Doe",  "Computer Science", 1],
[  2,  "E002",   "Jane Smith",  "Electrical Engineering", 1],
[  3,  "E003",   "Alice Johnson",  "Mechanical Engineering", 2],
[  4,  "E004",   "Bob Williams",  "Civil Engineering", 1],
[  5,  "E005",   "Eva Wilson",  "Chemistry", 3],
[  6,  "E006",   "Michael Brown",  "Physics", 2],
[  7,  "E007",   "Sarah Davis",  "Biology", 4],
[  8,  "E008",   "Chris Miller",  "Mathematics", 1],
[  9,  "E009",   "Emily Wilson",  "Computer Science", 2],
[  10,  "E010",   "David Lee",  "Electrical Engineering", 2]]


import csv
f=open("student.csv","w")
w=csv.writer(f)
w.writerow(r)
w.writerows(s)
f.close()
