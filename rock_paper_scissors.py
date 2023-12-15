import random
from tabulate import tabulate
l=["r","p","s"]
n=5
print("Enter r/p/s to play the rock paper scissors game ")
plp=0
cp=0
while(n!=0):

    print()
    
    s=input("Enter your choice -> ")
    c=random.choice(l)
    s=s.lower()

    if((s=="r" and c=="r")or(s=="p" and c=="p")or(s=="s" and c=="s")):
        print("The computer choose => ",c)
        print("This is a draw")
    
    elif((s=="r" and c=="p") or (s=="p" and c=="s") or (s=="s" and c=="r")):
        print("The computer choose => ",c)
        print("You lost")
        cp+=1

    elif((s=="r" and c=="s") or (s=="p" and c=="r") or (s=="s" and c=="p")):
        print("The computer choose => ",c)
        print("You won")
        plp+=1

    else:
        print("You enetred wrong choice")
    n-=1
head=["CPU","You"]
data=[[str(cp),str(plp)]]
print(tabulate(data,headers=head,tablefmt='double_outline'))


if(cp>=plp):
    print("You lost this match")

elif(cp==plp):
    print("This match is a draw")

else:
    print("You won hurray")
