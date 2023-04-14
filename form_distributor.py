import tkinter as tk
from components import Distributor
from datalayer import DALDistributor
from tkinter import messagebox

class form_distributor:

    def __init__(self):
        self.root= tk.Tk()
        self.root.title("Distributor Form")
        self.root.geometry("300x300")

        self.disname = tk.StringVar()
        self.add = tk.StringVar()
        self.city = tk.StringVar()
        self.contact = tk.StringVar()

        self.lb1 = tk.Label(self.root, text="Distributor Name")
        self.lb1.place(x=40, y=40)

        self.ent1 = tk.Entry(self.root, textvariable=self.disname)
        self.ent1.place(x=150, y=40)

        self.lb2 = tk.Label(self.root, text="Address")
        self.lb2.place(x=40, y=70)

        self.ent2 = tk.Entry(self.root, textvariable=self.add)
        self.ent2.place(x=150, y=70)

        self.lb3 = tk.Label(self.root, text="City")
        self.lb3.place(x=40, y=100)

        self.ent3 = tk.Entry(self.root, textvariable= self.city)
        self.ent3.place(x=150, y=100)

        self.lb4 = tk.Label(self.root, text="Contact No.")
        self.lb4.place(x=40, y=130)

        self.ent4 = tk.Entry(self.root, textvariable=self.contact)
        self.ent4.place(x=150, y=130)

        self.btn1 = tk.Button(self.root, text="Save", command=self.save_clicked)
        self.btn1.place(x=150, y=160)

        self.root.mainloop()

    def save_clicked(self):
        d = Distributor()
        d.DistributorName = self.disname.get()
        d.Address = self.add.get()
        d.City = self.city.get()
        d.Contact = self.contact.get()

        objDal = DALDistributor()
        if objDal.Add_Distributor(d)== True:
            messagebox.showinfo("Stock Manager","Distributor Details Added Successfully....")




obj = form_distributor()