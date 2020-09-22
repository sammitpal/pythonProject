from tkinter import *
import tkinter.messagebox as messagebox
def getVals():
    print("Submitting Form...")
    x = gendervalue.get()
    if x == 0:
        s = "Male"
    else:
        s = "Female"
    print(f"{namevalue.get(),phonevalue.get(),s}")
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),s}\n")
    messagebox.showinfo("information","Thank you, We will be in touch with you shortly")

root = Tk()
root.geometry("400x200")
root.title("My First GUI Tutorial")
root.minsize(200,100)
l1 = Label(root,text="Welcome")
l1.grid(row=0,column=3);

name = Label(root , text="Name")
phone = Label(root , text="Phone")
gender = Label(root , text="Gender")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = IntVar()

nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)

nameentry.grid(row=1,column=3,padx=20)
phoneentry.grid(row=2,column=3)

male = Radiobutton(text="Male", variable=gendervalue, value = 0)
female = Radiobutton(text="Female", variable=gendervalue, value = 1)

male.grid(row=3,column=3)
female.grid(row=3,column=4)

submit = Button(text = "Submit",command=getVals)
submit.grid(row=5,column=3)
root.mainloop()