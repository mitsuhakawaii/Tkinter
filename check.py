from Tkinter import *
from tkMessageBox import *
T = Tk()

def hello():
	showinfo("hi","i'm hyun")
def bye():
	showerror("bye","bye")


v1 = IntVar()

v2 = IntVar()

#Make CheckButton.


C1 = Checkbutton(T,text="hello",variable=v1,onvalue=1,offvalue=0,height=5,width=20,command=hello)
C2 = Checkbutton(T,text="Bye",variable=v2,onvalue=1,offvalue=0,height=5,width=20,command=bye)
C1.pack()
C2.pack()

T.mainloop()
