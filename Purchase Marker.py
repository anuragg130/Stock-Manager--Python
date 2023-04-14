import tkinter as tk
from tkinter import messagebox
from datalayer import *
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
from components import Purchase, Purchase_Transaction


class form_purchasemarker:

    def add_clicked(self):
        i = self.cmb2.current()
        pid = self.pro[i][0]
        pname = self.product.get()

        self.Tree1.insert("", self.counter.get(), text=pid,
                          values=(pname, self.quantity.get(), self.price.get(), self.quantity.get() * self.price.get()))
        self.counter.set(self.counter.get() + 1)
        tran = Purchase_Transaction()
        tran.ProductID = pid
        tran.Product_Name = pname
        tran.Quantity = self.quantity.get()
        tran.Price = self.price.get()
        tran.Total = self.quantity.get() * self.price.get()

        self.transactions.append(tran)

    def save_clicked(self):
        pur = Purchase()
        i = self.cmb1.current()
        did = self.dist[i][0]
        pur.PurchaseDate = self.Date.get()
        pur.DistributorID = did
        pur.InvoiceID = self.invoice.get()

        objDal = DALPurchaseMaster()
        objDal.Add_Purchase(pur)
        messagebox.showinfo("Stock Manager", "Purchase Done successfully...")

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Purchase Marker")
        self.root.geometry("1000x1000")

        self.Date = tk.StringVar()
        self.clicked = tk.StringVar()
        self.invoice = tk.StringVar()
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

        self.lb2 = tk.Label(self.root, text='Distributor')
        self.lb2.place(x=300, y=40)

        lp = DALDistributor()
        self.dist = lp.show_Distributor()
        distr = []
        for i in range(0, len(self.dist)):
            distr.append(self.dist[i][1])
        self.cmb1 = Combobox(self.root, textvariable=self.dis, state='readonly')
        self.cmb1.place(x=370, y=40)
        self.cmb1['values'] = distr

        self.lb3 = tk.Label(self.root, text="Invoice No.")
        self.lb3.place(x=530, y=40)

        self.ent2 = tk.Entry(self.root, textvariable=self.invoice)
        self.ent2.place(x=600, y=40)

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
        self.Tree1.place(x=10, y=200)

        self.Tree1['columns'] = ("c1", "c2", "c3", "c4")
        self.Tree1.heading("#0", text="Product ID")
        self.Tree1.heading("c1", text="Product Name")
        self.Tree1.heading("c2", text="Quantity")
        self.Tree1.heading("c3", text="Price")
        self.Tree1.heading("c4", text="Total")

        self.btn2 = tk.Button(self.root, text='Save', command=self.save_clicked)
        self.btn2.place(x=30, y=450)

        self.root.mainloop()


obj = form_purchasemarker()
