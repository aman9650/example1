from tkinter import *
root=Tk()
root.geometry("900x700")
root.title("FRAME")
f1=Frame(root, bg="blue", borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(root,borderwidth=8,bg="red",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Project Tkinter-PYcharm")
l.pack(pady=144)
l2=Label(f2,text="Project Tkinter X",font="23")
l2.pack(padx=133)
root.mainloop()
