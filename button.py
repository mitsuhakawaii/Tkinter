from Tkinter import *

# Make windwos.
T = Tk()

F = Frame(T,width=200,height=200) # "Frame" is control windows size.
F.pack() # Hmm.. I don't think this function.

button1 = Button(F,text="red",fg="red",width=20,height=5)
button1.pack()

button2 = Button(F,text="brown",fg="brown",width=20,height=5)
button2.pack()

button3 = Button(F,text="blue",fg="blue",width=20,height=5)
button3.pack()

button4 = Button(F,text="green",fg="green",width=20,height=5)
button4.pack()

button5 = Button(F,text="Python",width=20,height=5).pack() #In fact, you can write .pack in oneline.

#fg = change text's color.

T.mainloop()
