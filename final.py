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
            filename = '/root/LocalDisk/Project/Python/Password_Viewer/mypassword'
            file = open(filename, 'r')
            account_name = []
            account_name_dupli = []
            fulladress_n = []
            fulladress = []

            my_frame = Frame(top)
            my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

            def roll(e, y, r):
                pass_list.yview("scroll", 1, "units")
                email_list.yview("scroll", 1, "units")

            for i in file:
                a = i.split("\n")
                fulladress_n.append(a)

            l = len(fulladress_n)

            for i in range(0, l):
                b = fulladress_n[i][0]
                fulladress.append(b)

            for i in range(0, l):
                c = fulladress[i].split(",")
                account_name.append(c[0])
            account_name.sort()

            [account_name_dupli.append(x) for x in account_name if x not in account_name_dupli]

            def updateit():
                file.close()
                up = Tk()
                up.title("Password Viewer")

                w = 400
                h = 200
                ws = top.winfo_screenwidth()
                hs = top.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                up.geometry('%dx%d+%d+%d' % (w, h, x, y))
                up.deiconify()
                top.destroy()

                def add():
                    if acc_entry.get() == "":
                        acc_entry.insert(0, "Enter")
                    if accemail_entry.get() == "":
                        accemail_entry.insert(0, "Enter")
                    if accpass_entry.get() == "":
                        accpass_entry.insert(0, "Enter")
                    elif acc_entry.get() == "Enter":
                        acc_entry.delete(0, END)
                        acc_entry.insert(0, "Enter")
                    elif accemail_entry.get() == "Enter":
                        accemail_entry.delete(0, END)
                        accemail_entry.insert(0, "Enter")
                    elif accpass_entry.get() == "Enter":
                        accpass_entry.delete(0, END)
                        accpass_entry.insert(0, "Enter")
                    else:
                        a = acc_entry.get()
                        b = a.capitalize()
                        con = "\n" + str(b) + "," + str(accemail_entry.get()) + "," + str(
                            accpass_entry.get())
                        upname = '/root/LocalDisk/Project/Python/Password_Viewer/mypassword'
                        update = open(upname, "a")
                        update.write(con)
                        update.close()

                        messagebox.showinfo("Success", "Successfully Updated ")

                        up.withdraw()
                        lg_option("event")

                acc_label = Label(up, text="Account Name :")
                acc_label.grid(row=0, column=0, padx=10, pady=10)
                acc_entry = Entry(up, width=30)
                acc_entry.grid(row=0, column=1, padx=10, pady=10)

                accemail_label = Label(up, text="Account Email/Username :")
                accemail_label.grid(row=1, column=0, padx=10, pady=10)
                accemail_entry = Entry(up, width=30)
                accemail_entry.grid(row=1, column=1, padx=10, pady=10)

                accpass_label = Label(up, text="Password :")
                accpass_label.grid(row=2, column=0, padx=10, pady=10, columnspan=1)
                accpass_entry = Entry(up, width=30)
                accpass_entry.grid(row=2, column=1, padx=10, pady=10)

                add_button = Button(up, text="Add", width=25, command=add)
                add_button.grid(row=3, column=1, padx=10, pady=10)


            def click(event):
                global pass_list
                global email_list
                email_label = Label(top, text="Email:")
                email_label.grid(row=0, column=1, padx=1, pady=10)
                email_list = Listbox(top, height=1, width=30, yscrollcommand=my_scrollbar.set)
                email_list.config(yscrollcommand=my_scrollbar.set)

                email_list.grid(row=0, column=2, padx=(1, 1), pady=10)
                pass_label = Label(top, text="Password:")
                pass_label.grid(row=0, column=3, padx=(10, 0), pady=1)
                pass_list = Listbox(top, height=1, width=30, yscrollcommand=my_scrollbar.set)
                pass_list.grid(row=0, column=4, padx=1, pady=10)
                my_scrollbar.config(command=roll)
                my_scrollbar.grid(row=0, column=2)
                my_frame.grid(row=0, column=2)
                e = clicked.get()
                for i in fulladress:
                    f = i.split(",")
                    if e in f:
                        email_list.insert(END, f[1])
                        pass_list.insert(END, f[2])

            clicked = StringVar()
            clicked.set("Click")
            acc_drop = OptionMenu(top, clicked, *account_name_dupli, command=click)
            acc_drop.grid(row=0, column=0, padx=10, pady=10)

            updatebut = Button(top, text="Update", width=15, command=updateit)
            updatebut.grid(row=1, column=0, padx=10, pady=5)

            close_button = Button(top, text="Close", width=15, command=root.quit)
            close_button.grid(row=2, column=0, padx=10, pady=5)









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