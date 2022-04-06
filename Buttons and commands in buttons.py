from tkinter import *
root=Tk()
root.geometry("900x700")
root.title("BUTTONS IN TKINTER")

def hello():
    print("hello Tkinter button")

def name():
    print("name is aman")

frame= Frame(root,borderwidth=6,bg="WHITE",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame,fg="red",text="hello",command=hello)
b1.pack(side=LEFT)

b2=Button(frame,fg="red",text="name",command=name)
b2.pack(side=LEFT,padx=12)

b3=Button(frame,fg="red",text="print now")
b3.pack(side=LEFT,padx=12)

b3=Button(frame,fg="red",text="print now")
b3.pack(side=LEFT,padx=12)



root.mainloop()
