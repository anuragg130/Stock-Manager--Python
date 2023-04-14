import tkinter as tk
from tkinter.ttk import Treeview
from datalayer import DALProduct

class List_Products:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x400")
        self.root.title("Product List")

        self.Tree1 = Treeview(self.root)
        self .Tree1.place(x=40,y=40)

        self.Tree1['columns'] = ("c1", "c2")
        self.Tree1.heading("#0", text="Product ID")
        self.Tree1.heading("c1", text="Product Name")
        self.Tree1.heading("c2",text="Category")

        lp = DALProduct()
        records = lp.Show_Product()

        for i in range(0, len(records)):
            self.Tree1.insert("", i, text=records[i][0], values=( records[i][1], records[i][2]))

        self.btn1 = tk.Button(self.root, text="Delete", command=self.delete)
        self.btn1.pack()


        self.root.mainloop()

    def delete(self):
        selected_item = self.Tree1.selection()[0]
        self.Tree1.delete(selected_item)


obj= List_Products()
