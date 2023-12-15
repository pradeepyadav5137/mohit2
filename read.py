f=open("file.txt","w")
x="hello my name is akshat jaiswal\nand i am a student at DSC, DU"
f.write(x)
a=["\naur bhai ","kiddan\n","kahin nahi bhai"]
f.writelines(a)
#f.close()                   # very important to write this 

f=open("file.txt","r")
x=f.read(3)
x1=f.readline()
x2=f.readlines()
print(x)
print(x1)
print(x2)
