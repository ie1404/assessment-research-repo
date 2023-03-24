from tkinter import*
from tkinter.ttk import*
from time import strftime
import tkinter.messagebox
term=Tk()
term.geometry("500x500")
term.title("ticket form")

menubar=Menu(term)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
# menu_0=Menu(term, Text="Selection Menu",width=20,font=("bold",20))
# def Exitcallback():
#     term.messagebox.showerror("Closing","goodbye")
    
file.add_separator()
file.add_command(label ='Exit', command = term.destroy)

# label_0=Label(term)
term.config(menu = menubar)
term.mainloop()