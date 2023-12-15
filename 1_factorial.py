def fact(q):
    if q==0 :
        return 1
    else:
        return q*fact(q-1)

number=int(input("Enter a positive whole number -> "))
x=fact(number)
print("The factorial of the number is-> ",x,"\n")






n=int(input("Enter a positive whole number -> "))
f=1
for i in range(1,n+1):
    f=f*i
print("The factorial of the number is-> ",f)