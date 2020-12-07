from tkinter import *
import string
import random

window = Tk()

source = string.ascii_letters + string.digits + string.punctuation
def process():
    result = random.sample(source, int(e1.get()))  # get password length
    pwd = "".join(result)
    e2.delete(0,"end")
    e2.insert(0, pwd)

def copy():
    window.clipboard_clear()
    window.clipboard_append(e2.get())  # copy generated password

l1 = Label(window, text="Password Length")
l2 = Label(window, text="Generated Password")
l1.grid(row=0,column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="Generating", command=process)
b2 = Button(window, text="Copy", command=copy)
b1.grid(row=2, column=0)
b2.grid(row=2,column=1)

window.mainloop()
