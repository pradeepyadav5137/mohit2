import csv

f=open("student.csv","r")
r=csv.reader(f)
l=list(r)
print(l)
for i in l:
    sem=i[4]
    if sem=='2':            #csv files mein data string format mein input chale jaata h
        print(i)
f.close()