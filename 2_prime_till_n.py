n=int(input("Enter the number -> "))

for i in range(2,n+1):          # bcuz 1 is neither prime nor composite
    t=0 
    for j in range(2,i):        # to check divisibility from 2 to one less than the number
        if(i%j==0):              
            t+=1
            break
        else:
            pass
    if(t==0):
        print(i,end=" ")