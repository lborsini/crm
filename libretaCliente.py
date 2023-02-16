from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Customer Relationship Manager')
root.config(background='#7DA2B3')
root.geometry('650x325')
root.resizable(0,0)

table = Frame(root)
table.grid(row=1, column=0, columnspan=2, padx=22, pady=15)

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


def renderClient():
    rows = c.execute("SELECT * FROM client").fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))

def insert(client):
    c.execute("""
        INSERT INTO client (name, cel, company) VALUES (?, ?, ?)
    """, (client['name'], client['contact'], client['company']))
    conn.commit()

    renderClient()


def newClient ():
    def save():
        if not eName.get():
            messagebox.showerror('Error', "The Name is required")
            return

        if not eContact.get():
            messagebox.showerror('Error', "The Contact is required")
            return

        if not eCompany.get():
            messagebox.showerror('Error', "The Company is required")
            return

        cliente = {
            'name' : eName.get(),
            'contact' : eContact.get(),
            'company' : eCompany.get()
        }
        insert(cliente)
        top.destroy()

    #Create a new windows with the form
    top = Toplevel()
    top.title('New Client')
    top.config(background='#7DA2B3')
    top.geometry('530x205')
    top.resizable(0,0)

    lName = Label(top, text=' Name ', background='#7DA2B3', font='Times')
    lName.grid(row=0, column=0, padx=10, pady=10)
    eName = Entry(top, width=40, bg='#FFFEFF', font='Times', relief='sunken', bd=2, fg='#000', justify='center')
    eName.grid(row=0, column=1)

    lContact = Label(top, text=' Contact ', background='#7DA2B3', font='Times')
    lContact.grid(row=1, column=0, padx=10, pady=10)
    eContact = Entry(top, width=40, bg='#FFFEFF', font='Times', relief='sunken', bd=2, fg='#000', justify='center')
    eContact.grid(row=1, column=1)

    lCompany = Label(top, text=' Company ', background='#7DA2B3', font='Times')
    lCompany.grid(row=2, column=0, padx=10, pady=10)
    eCompany = Entry(top, width=40, bg='#FFFEFF', font='Times', relief='sunken', bd=2, fg='#000', justify='center')
    eCompany.grid(row=2, column=1)

    btnSave = Button(top, text='Save As', font=('Times', "10") ,background='#4DFC75', foreground='#000', bd=2, width=20, height=2, command=save)
    btnSave.grid(row = 3, column= 1, padx=10, pady=10)

    eName.focus()

    top.mainloop()


def deleteClient():
    id = tree.selection()[0]
    name = c.execute("SELECT * FROM client WHERE id = ?", (id, )).fetchone()
    resp = messagebox.askokcancel('Sure', 'Are you sure you want delete ' + name[1] + '?')

    if resp:
        c.execute("DELETE FROM client WHERE id = ?", (id, ))
        conn.commit()
        renderClient()
    else:
        pass

btnNew = Button(root, text= 'Nuevo Cliente', font=('Times', "10") ,background='#4DFC75', foreground='#000', bd=2, width=20, height=2, command=newClient)
btnNew.grid(row=0, column=0, padx=10, pady=10)

btnDel = Button(root, text= 'Eliminar Cliente', font=('Times', "10"), background='#FF6762', foreground='#000', bd=2, width=20, height=2, command=deleteClient)
btnDel.grid(row=0, column=1)

tree = ttk.Treeview(table)
tree['columns']= ('Name', 'Contact', 'Company')
tree.column('#0', width=0, stretch=NO)
tree.column('Name')
tree.column('Contact')
tree.column('Company')

tree.heading('Name', text=' Name ')
tree.heading('Contact', text=' Contact ')
tree.heading('Company', text=' Company ')

tree.grid(row=1, column=0, columnspan=2)
ttk.Style().configure('Treeview', background='#FFFEFF ', foreground='#000', font='Times', padx=20, pady=20 )

renderClient()

root.mainloop()
