class Product:
    def __init__(self):
        self.ProductID = 0
        self.ProductName = None
        self.Category = None


class Distributor:
    def __init__(self):
        self.DistributorID = 0
        self.DistributorName = None
        self.Address = None
        self.City = None
        self.Contact = None

class Purchase:
    def __init__(self):
        self.PurchaseMasterID = 0
        self.PurchaseDate = 0
        self.DistributorID = 0
        self.InvoiceID = None
        self.Transactions = []

class Purchase_Transaction:
    def __init__(self):
        self.ProductID = None
        self.Product_Name = None
        self.Quantity = 0
        self.Price = 0
        self.Total = 0

class Sales:
    def __init__(self):
        self.SaleMasterID = 0
        self.SaleDate = None
        self.CustomerName = None
        self.ContactNo = None

class Sales_Transactions:
    def __init__(self):
        self.TransactionID = 0
        self.ProductID = 0
        self.Quantity = 0
        self.Price = 0
