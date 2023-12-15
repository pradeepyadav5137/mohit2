l=[1,2,3,2,4,3,2,6,4,6,6,6]
d={}
for i in l:
    t=i
    if i not in d:
        c=0
        for j in l:
            if(t==j):
                c=c+1
    d[i]=c
print(d)