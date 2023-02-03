from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title('CRM')

conn = sqlite3.connect('crm.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists client (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cel TEXT NOT NULL,
        company TEXT NOT NULL
    );
""")

def newClient ():
    pass

def deleteClient():
    pass

btnNew = Button(root, text= 'Nuevo Cliente', command=newClient)
btnNew.grid(row=0, column=0)

btnDel = Button(root, text= 'Eliminar Cliente', command=deleteClient)
btnDel.grid(row=0, column=1)

tree = ttk.Treeview(root)
tree['columns']= ('Name', 'Contact', 'Company')
tree.column('#0', width=0, stretch=NO)
tree.column('Name')
tree.column('Contact')
tree.column('Company')

tree.heading('Name', text=' Name ')
tree.heading('Contact', text=' Contact ')
tree.heading('Company', text=' Company ')

tree.grid(row=1, column=0, columnspan=2)

root.mainloop()
