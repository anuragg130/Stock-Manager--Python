import pyodbc
from components import Product
from components import Distributor
from components import Purchase
from tkinter.ttk import Treeview

class DalHelper:
    def __init__(self):
        self.con = pyodbc.connect("driver={SQL Server};server=ANURAGOMEN\\SQLEXPRESS;database=projectdb;uid=sa;pwd=anurag")

    def __del__(self):
        if self.con!=None:
            self.con.close()
            self.con = None

class DALProduct(DalHelper):
    def Add_Product(self, Pro):
        flag = False
        try:
            cur = self.con.cursor()
            tup = (Pro.ProductName, Pro.Category)
            cur.execute("Insert into Products values(?,?)", tup)
            self.con.commit()
            flag = True
        except:
            self.con.rollback()

        return flag

    def Show_Product(self):

        cur= self.con.cursor()
        cur.execute("select * from Products")
        records = cur.fetchall()
        return records


class DALDistributor(DalHelper):
    def Add_Distributor(self, Dis):

        try:
            flag = False
            cur=self.con.cursor()
            tup= (Dis.DistributorName, Dis.Address, Dis.City, Dis.Contact)
            cur.execute("Insert into distributor values(?,?,?,?)",tup)
            self.con.commit()
            flag = True
        except:
            self.con.rollback()

        return flag

    def show_Distributor(self):

        cur = self.con.cursor()
        cur.execute("select * from distributor")
        records = cur.fetchall()
        return records


class DALPurchaseMaster(DalHelper):
    def Add_Purchase(self, Pur):
        flag = False
        try:
            cur = self.con.cursor()
            tup = (Pur.PurchaseDate, Pur.DistributorID, Pur.InvoiceID)
            cur.execute("Insert into PurchaseMarker values(?,?,?)", tup)
            self.con.commit()
            flag = True
        except:
            self.con.rollback()

    def show_Purchase(self):

        cur = self.con.cursor()
        cur.execute("select * from PurchaseMarker")
        records = cur.fetchall()
        return records


class DALSale(DalHelper):
    def Add_Sale(self, sal):
        flag = False
        try:
            cur = self.con.cursor()
            tup = ( sal.SaleDate, sal.CustomerName, sal.ContactNo)
            cur.execute("Insert into sales values(?,?,?)", tup)
            self.con.commit()
            flag = True
        except:
            self.con.rollback()

    def show_Sale(self):

        cur = self.con.cursor()
        cur.execute("select * from sales")
        records = cur.fetchall()
        return records