from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry("500x500")
window.title("My Login")
window.config(bg="pink")

user_lbl=Label(window, text="Username")
user_lbl.pack()

user_entry=Entry(window, textvariable="username")
user_entry.pack()

pass_lbl=Label(window, text="Password")
pass_lbl.pack()

pass_entry=Entry(window, textvariable="password", show="*")
pass_entry.pack()


def check():
    all_login={"litha":"litha123", "odwa":"odwa123", "siphe": "siphe123","lwando": "lwando123"}
    my_user=user_entry.get()
    password=pass_entry.get()
    if (my_user, password)in all_login.items():
        messagebox.showinfo("INFO", "Correct Login")
        window.withdraw()
        import CheckingLog
        CheckingLog.verify()
    else:
        messagebox.showinfo("INFO", "Incorrect Login")
        user_entry.delete(0, END)
        pass_entry.delete(0, END)




mybutton= Button(window, text="Login ", bg="magenta", command=check).pack()







window.mainloop()