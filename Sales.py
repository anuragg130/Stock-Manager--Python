import tkinter as tk
from tkinter import messagebox
from datalayer import *
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
from components import Sales, Sales_Transactions


class form_sales:

    def add_clicked(self):
        i = self.cmb2.current()
        tid = self.pro[i][0]
        name = self.Name.get()
        pname = self.product.get()

        self.Tree1.insert("", self.counter.get(), text=tid,
                          values=(self.Date.get(), name, self.contact.get(), pname,  self.quantity.get(), self.price.get(),
                                  self.quantity.get() * self.price.get()))

    def save_clicked(self):
        sal = Sales()
        sal.SaleDate = self.Date.get()
        sal.CustomerName = self.Name.get()
        sal.ContactNo = self.contact.get()

        objDal = DALSale()
        objDal.Add_Sale(sal)
        messagebox.showinfo("Stock Manager", "Sale Done successfully...")

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sales Master")
        self.root.geometry("1000x1000")

        self.Date = tk.StringVar()
        self.Name = tk.StringVar()
        self.clicked = tk.StringVar()
        self.contact = tk.StringVar()
        self.quantity = tk.IntVar()
        self.click = tk.StringVar()
        self.dis = tk.StringVar()
        self.product = tk.StringVar()
        self.price = tk.IntVar()
        self.transactions = []
        self.counter = tk.IntVar()

        self.lb1 = tk.Label(self.root, text="Date")
        self.lb1.place(x=40, y=40)
        self.ent1 = tk.Entry(self.root, textvariable=self.Date)
        self.ent1.place(x=150, y=40)

        self.lb2 = tk.Label(self.root, text='Customer Name')
        self.lb2.place(x=300, y=40)
        self.ent22 = tk.Entry(self.root, textvariable=self.Name)
        self.ent22.place(x=400, y=40)

        self.lb3 = tk.Label(self.root, text="Contact No.")
        self.lb3.place(x=570, y=40)
        self.ent2 = tk.Entry(self.root, textvariable=self.contact)
        self.ent2.place(x=640, y=40)

        self.lb4 = tk.Label(self.root, text="Product")
        self.lb4.place(x=40, y=100)
        pl = DALProduct()
        self.pro = pl.Show_Product()
        produc = []
        for i in range(0, len(self.pro)):
            produc.append(self.pro[i][1])
        self.cmb2 = Combobox(self.root, textvariable=self.product, state='readonly')
        self.cmb2.place(x=100, y=100)
        self.cmb2['values'] = produc

        self.lb3 = tk.Label(self.root, text="Quantity")
        self.lb3.place(x=250, y=100)
        self.ent2 = tk.Entry(self.root, textvariable=self.quantity)
        self.ent2.place(x=320, y=100)

        self.lb3 = tk.Label(self.root, text="Price")
        self.lb3.place(x=460, y=100)
        self.ent2 = tk.Entry(self.root, textvariable=self.price)
        self.ent2.place(x=510, y=100)

        self.btn1 = tk.Button(self.root, text='Add', command=self.add_clicked)
        self.btn1.place(x=40, y=150)

        self.Tree1 = Treeview(self.root)
        self.Tree1.place(x=5, y=200)

        self.Tree1['columns'] = ("c1", "c2", "c3", "c4", "c5", "c6", "c7")
        self.Tree1.heading("#0", text="Transaction ID")
        self.Tree1.heading("c1", text="Sale Date")
        self.Tree1.heading("c2", text="Customer Name")
        self.Tree1.heading("c3", text="Contact No.")
        self.Tree1.heading("c4", text="Product Name")
        self.Tree1.heading("c5", text="Quantity")
        self.Tree1.heading("c6", text="Price")
        self.Tree1.heading("c7", text="Total")

        self.btn2 = tk.Button(self.root, text='Save', command=self.save_clicked)
        self.btn2.place(x=30, y=450)

        self.root.mainloop()


obj = form_sales()
