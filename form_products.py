import tkinter as tk
from tkinter.ttk import Combobox
from components import Product
from datalayer import DALProduct
from tkinter import messagebox

class form_products:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Products Form")
        self.root.geometry("400x200")

        self.PName = tk.StringVar()

        self.lb1 = tk.Label(self.root, text="Product Name")
        self.lb1.place(x=40, y=40)

        self.ent1 = tk.Entry(self.root, textvariable=self.PName)    
        self.ent1.place(x=150, y=40)

        self.lb2 = tk.Label(self.root, text="Category")
        self.lb2.place(x=40, y=70)

        self.category = tk.StringVar()
        self.category.set("Electrical")

        self.rb1 = tk.Radiobutton(self.root, text="Electrical", variable=self.category, value="Electrical")
        self.rb1.place(x=140, y=70)

        self.rb2 = tk.Radiobutton(self.root, text="Electronics", variable=self.category, value="Electronic")
        self.rb2.place(x=240, y=70)

        self.btn1 = tk.Button(self.root, text="Save", command=self.save_clicked)
        self.btn1.place(x=150, y=120)

        self.btn2 = tk.Button(self.root, text="Close", command=self.close_clicked)
        self.btn2.place(x=240, y=120)

        self.root.mainloop()

    def save_clicked(self):
        p = Product()
        p.ProductName = self.PName.get()
        p.Category = self.category.get()

        objDAL = DALProduct()
        if objDAL.Add_Product(p)==True:
            messagebox.showinfo("Stock Manager","Product added successfully...")

    def close_clicked(self):
        self.root.destroy()

obj = form_products()