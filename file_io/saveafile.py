from tkinter import filedialog
from tkinter import *

a=open("../img/mice.jpeg", "rb")
root = Tk()
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
with open(root.filename, 'wb') as file:
    file.write(a.read())
    file.close()
a.close()
