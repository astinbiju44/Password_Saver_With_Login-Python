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

def lg_option(event):
    if lgpass_entry.get() == "":
        lgpass_entry.insert(0, "")
    else:
        text = lgpass_entry.get()
        if text == "8520":
            top = Toplevel()
            top.title("Password Viewer")
            w = 650
            h = 130
            ws = top.winfo_screenwidth()
            hs = top.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            top.geometry('%dx%d+%d+%d' % (w, h, x, y))
            top.deiconify()
            root.withdraw()








        else:
            messagebox.showerror("ERROR", "Wrong Password")





lgpass_label=Label(root,text="Enter Your Password",font=("Helvetica", 16))
lgpass_label.pack(pady=(10,0))

lgpass_entry=Entry(root,width=50,show="*",bd=10,textvariable=10)
lgpass_entry.bind("<Return>",lg_option)
lgpass_entry.pack()


lgbutton=Button(root,text="Continue",width=10,font=("Helvetica", 15),relief=GROOVE,command=lambda : lg_option("event"))
lgbutton.bind("<Return>",lg_option)
lgbutton.pack(pady=(10,0))




root.mainloop()