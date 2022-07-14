from tkinter import ttk
from tkinter.ttk import Treeview

from Logs import EnterLog
from tkinter import *


class BillView:
    def __init__(self, rb):
        self.Frame = Frame()
        self.TreeBill = Treeview()
        self.BC = rb
        EnterLog("Init BillView")

    def GetAllBill(self, list, frame):
        self.Frame = frame
        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeBill = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Number", "Achat/Vente", "Product", "Total"))
        for column in self.TreeBill["columns"]:
            self.TreeBill.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeBill.heading(column, text=column)
        self.TreeBill['show'] = 'headings'
        self.TreeBill.bind("<Double-1>", self.InfoBill)
        for b in list:
            if b.GetType() == 1:
                ty = "Vente"
            else:
                ty = "Achat"
            self.TreeBill.insert('', END, values=(b.GetNumber(), ty, b.GetProduct(), str(b.GetTotalPrice()) + "€"))
        self.TreeBill.pack(fill=X)
        sb.config(command=self.TreeBill.yview)
        Button(self.Frame, text="Retour", command=self.BC.Retour).pack(fill=X)
        EnterLog("Bill view :: GetAllBill")

    def InfoBill(self, event):
        qt = IntVar()
        item = self.TreeBill.item(event.widget.selection())['values']
        EnterLog("you clicked on : " + item[1])
        for w in self.Frame.winfo_children():
            w.destroy()
        Label(self.Frame, text=self.BC.GetInfo(item[0]), font=("Arial", "20")).pack()
        Button(self.Frame, text="retour", command=lambda: self.BC.GetAllBill(self.Frame)).pack(fill=X)
        if not self.BC.GetInfo(item[2]):
            EnterLog("BillView :: InfoBill :: ERROR:None object")
        else:
            EnterLog("BillView :: InfoBill :: SUCCESS")

