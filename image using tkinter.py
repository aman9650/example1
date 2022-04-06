from tkinter import *
root=Tk()
root.geometry("1111x933")
root.title("                                                                                      The Hindustan Times")
photo=PhotoImage(file=r"C:\Users\krishan dev\Downloads\Brahmos-1.png")

label=Label(image=photo)

label.pack(side="top",anchor="w",padx=34, pady=34)


label1=Label(text="After missile ‘malfunction’, BrahMos buyer Manila called Indian envoy",font=("comicsansms 19 bold"))

label1.pack()

root.mainloop()

