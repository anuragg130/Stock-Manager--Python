import tkinter as tk
from tkinter.ttk import Treeview
from datalayer import DALDistributor

class List_Distributor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1100x400")
        self.root.title("Distributor List")

        self.Tree1 = Treeview(self.root)
        self .Tree1.place(x=40,y=40)

        self.Tree1['columns'] = ("c1", "c2", "c3", "c4")
        self.Tree1.heading("#0", text="Distributor ID")
        self.Tree1.heading("c1", text="Distributor Name")
        self.Tree1.heading("c2", text="Address")
        self.Tree1.heading("c3", text="City")
        self.Tree1.heading("c4", text="Contact No.")

        lp = DALDistributor()
        records = lp.show_Distributor()

        for i in range(0, len(records)):
            self.Tree1.insert("", i, text=records[i][0], values=( records[i][1], records[i][2], records[i][3], records[i][4]))

        self.root.mainloop()


obj = List_Distributor()
