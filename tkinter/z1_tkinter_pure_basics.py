from tkinter import *
from time import *
root=Tk()
root.geometry("600x400+360+150")        # +360+100  incdicates the positioning of the windwow
                                        #       360 shifted on X axis     100 on Y axis
root.resizable(1,1)         # 1,1 indicates True on x and True on y

# root.minsize(100,150)
# root.maxsize(650,450)       #   width , height

    #      root.destroy()   ese likhenge 
    #      aur jese button ke andar command ke andar function likhte hen
    #      to likhenege      root.destroy

p=PhotoImage(file="bank1.png")
root.iconphoto(True,p)
root.title("Secure Bank")




def close():
    root.destroy()

b=Button(root,text="Close",command=close)
b.pack(side =TOP,pady=5)
start=time()
#root.after(5000,root.destroy)           #after function
root.mainloop()
end=time()
print("Destroyted in %d"%(end-start))