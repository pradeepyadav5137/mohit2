import csv
f=open("ccssvv.csv","w")
m=['name','roll no']
l=[['akshat',1],['harsh bhaiiiiii',2]]
w=csv.writer(f)
w.writerows(l)
for i in l:
    w.writerow(i)
f.close()

with open("ccssvv.csv","r") as f:
    r=csv.reader(f)
    for i in r:
        print(i)

