f=open("f.txt","r")
s="aeiou"

x=f.read()
x2=x.lower()            #lower functions does not edits the original string 
                        #    but it creates a copy of lowered string 
d=dict.fromkeys(s,0)
print(d)
for i in x2:
    if i in s:
        d[i]+=1
print(d)
