
from tkinter import *
from tkinter import messagebox
window2 =Tk()
window2.title("Erro Checks")
window2.geometry("500x500")
window2.config(bg="pink")


labelling=Label()
def verify():
    messagebox.showinfo("you guys are crazy")
    mycheck=Button(window2, text="check status", command=verify)
    mycheck.pack()

def check():
    try:
        entry_get = int(check_entry.get())
        if entry_get > 3000:
            messagebox.showinfo("Qualfy", 'You qualify for the Malaysia trip. Congratulations.')
            check_entry.delete(0, END)

        else:
            messagebox.showinfo("Qualfy", 'You need more funds')
            check_entry.delete(0, END)

    except ValueError:
           messagebox.showinfo("Quality", 'Please deposit more funds for this excursion')




check_account=Label(window2, text="Please enter amount in your account")
check_account.pack()

check_entry=Entry(window2, textvariable="")
check_entry.pack()

mybutton= Button(window2, text="Check qualfication ", bg="magenta",command=check).pack()
exit_button = Button(window2,text="Exit", bg="red",command=window2.destroy).pack()

window2.mainloop()