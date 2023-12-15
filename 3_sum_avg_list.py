l=[2,4,2,2,4,4,2,6,10,10]
s=sum(l)
s2=0
for i in l:
    s2+=i
print("Sum method 1 -> ",s,"\nSum method 2 -> ",s2,"\n")

avg=s/len(l)
print("Average -> ",avg)