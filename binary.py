import pickle
f=open("binary.dat","wb+")
l=["Akshat","Jaiswal","Harsh","bhaiiiiiiiiii"]
pickle.dump(l,f)            # dump a list l in file f
f.close()
f=open("binary.dat","rb+")
x=pickle.load(f)

f.close()
print(x)