from tkinter import*
from tkinter.ttk import*
from time import strftime
import tkinter.messagebox
from ticket import*
import main





term=Tk()
term.geometry("500x500")
term.title("ticket form")

menubar=Menu(term)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
# menu_0=Menu(term, Text="Selection Menu",width=20,font=("bold",20))

file.add_separator()
file.add_command(label ='Exit', command = term.destroy)

def Create():
    createn=Toplevel(term)
    createn.title("Create a New Ticket")
    createn.geometry("500x500")
    createn.grid_columnconfigure((0,1),weight=1)
    
    L1=Label(createn,text="Staff Id:")
    L2=Label(createn,text="Staff Name:")
    L3=Label(createn,text="Email:")
    L4=Label(createn,text="issue:")


    E1=Entry(createn)
    E2=Entry(createn)
    E3=Entry(createn)
    E4=Entry(createn)

    submit=Button(createn,text="Submit",)
    
    L1.grid(row=3, column=0)
    E1.grid(row=3, column=1, sticky="ew")
    L2.grid(row=4, column=0)
    E2.grid(row=4, column=1, sticky="ew")
    L3.grid(row=5, column=0)
    E3.grid(row=5, column=1, sticky="ew")
    L4.grid(row=6, column=0)
    E4.grid(row=6, column=1, sticky="ew")
    submit.pack()
    
    
    


def Show():
    createn=Toplevel(term)
    createn.title("All Tickets")
    createn.geometry("500x500")
    

def Respond():
    createn=Toplevel(term)
    createn.title("Repond")
    createn.geometry("500x500")
    Label(createn,text="Create a new ticket").pack()

b1=Button(term,text="create a ticket",width=40,command=Create)
b2=Button(term,text="Show all Tickets",width=40,command=Show)
b3=Button(term,text="Provide a response",width=40,command=Respond)
b4=Button(term,text="reopen a ticket",width=40)
b5=Button(term,text="display stats",width=40,)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()


# label_0=Label(term)
term.config(menu = menubar)
term.mainloop()