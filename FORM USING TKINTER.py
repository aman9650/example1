from tkinter import *
root=Tk()
root.geometry("700x500")

def getvals():
    print("it works")

#Heading
Label(root,text="welcome to python",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
                                                                             
#TEXT FOR OUR FORM                                                                          
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="gender")
emergency=Label(root,text="Emergency Contact")
paymentmode=Label(root,text="Payment Mode")

#PACK TEXT FOR OUR FROM USING GRID
name.grid(row="1",column="2")
phone.grid(row="2",column="2")
gender.grid(row="3",column="2")
emergency.grid(row="4",column="2")
paymentmode.grid(row="5",column="2")


#TKINTER VARIABLES FOR STORING ENTERIES
namevalue = StringVar()
phonevalue = StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodswervicevalue=IntVar()


#ENTERIES FOR OUR FROM
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)


#PACKING THE ENTERIES
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)


#CHECKBOX AND PACKING IT
foodswervice=Checkbutton(text="Want to prebook your meal?",variable=foodswervicevalue)
foodswervice.grid(row=6,column=3)

#BUTTON AND PACKING IT AND ASSIGNING IT A COMMAND
Button(text="Submit the Form",command=getvals).grid(row=7,column=3)

root.mainloop()