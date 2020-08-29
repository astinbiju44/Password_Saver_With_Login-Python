from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Password Viewer")

w=400
h=150
# get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# calculate position x, y
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root.mainloop()