from Tkinter import *
import tkMessageBox

T = Tk()

#make function(def)
def order():
        tkMessageBox.showinfo("Hi", "I'm a hyun_park")
        tkMessageBox.showwarning("HI", "I'm a warning_hyun_park")

        #Exist etc message function..

B1 = Button(T,text="red",fg="red",width=20,height=5,command=order) #Command is use the python system.(maybe)


B1.pack()

T.mainloop()
