from tkinter import ttk
from tkinter.ttk import Treeview

from Logs import EnterLog
from tkinter import *


class RessourceView:
    def __init__(self, rc):
        self.frame = Frame()
        self.tmp = Frame()
        self.RC = rc
        self.List = []
        self.TreeRessource = Treeview()
        EnterLog("Init RessourceView")

    def Shop(self, list, root):
        self.Frame = root
        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeRessource = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Nom", "prix"))
        for column in self.TreeRessource["columns"]:
            self.TreeRessource.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeRessource.heading(column, text=column)
        self.TreeRessource['show'] = 'headings'
        self.TreeRessource.bind("<Double-1>", self.InfoBuy)
        for r in list:
            self.TreeRessource.insert('', END, values=(r.GetName(), str(r.GetPrice())+"€", r.GetID()))
        self.TreeRessource.pack(fill=X)
        sb.config(command=self.TreeRessource.yview)
        Button(self.Frame, text="Retour", command=self.RC.Retour).pack(fill=X)
        EnterLog("Ressource view :: Shop")


    def InfoBuy(self, event):
        qt = IntVar()
        item = self.TreeRessource.item(event.widget.selection())['values']
        EnterLog("you clicked on : " + item[0])
        for w in self.Frame.winfo_children():
            w.destroy()
        Label(self.Frame, text=self.RC.GetInfo(item[2]), font=("Arial", "20")).pack()
        entry = Entry(self.Frame, textvariable=qt)
        entry.pack(fill=X)
        entry.delete(0, END)
        entry.focus()
        Button(self.Frame, text="Acheter", command=lambda: self.RC.Buy(qt, item[2])).pack(fill=X)
        Button(self.Frame, text="retour", command=lambda: self.RC.GetShop(self.Frame)).pack(fill=X)
        if not self.RC.GetInfo(item[2]):
            EnterLog("RessourceView :: GetInfo :: ERROR:None object")
        else:
            EnterLog("RessourceView :: GetInfo :: SUCCESS")

    def GetStorage(self, frame, list):
        self.Frame = frame
        self.List = list

        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeRessource = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Nom", "Quantité"))
        for column in self.TreeRessource["columns"]:
            self.TreeRessource.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeRessource.heading(column, text=column)
        self.TreeRessource['show'] = 'headings'
        self.TreeRessource.bind("<Double-1>", self.InfoSell)
        for r in list:
            self.TreeRessource.insert('', END, values=(r.GetName(), str(r.GetQuantity()), r.GetID()))
        self.TreeRessource.pack(fill=X)
        sb.config(command=self.TreeRessource.yview)
        Button(self.Frame, text="Retour", command=self.RC.Retour).pack(fill=X)
        EnterLog("Ressource view :: GetStorage")

    def InfoSell(self, event):
        qt = IntVar()
        price = StringVar()
        item = self.TreeRessource.item(event.widget.selection())['values']
        EnterLog("you clicked on : " + item[0])
        for w in self.Frame.winfo_children():
            w.destroy()
        Label(self.Frame, text=self.RC.GetInfo(item[2]), font=("Arial", "20")).pack()
        entry = Entry(self.Frame, textvariable=qt)
        entryS = Entry(self.Frame, textvariable=price)
        Label(self.Frame, text="Quantité Vendue :").pack()
        entry.pack(fill=X)
        entry.delete(0, END)
        entry.focus()
        Label(self.Frame, text="Prix de vente :").pack()
        entryS.pack(fill=X)
        entryS.delete(0, END)
        Button(self.Frame, text="Vendre", command=lambda: self.RC.Sell(qt.get(), price.get(), item[2])).pack(fill=X)
        Button(self.Frame, text="retour", command=lambda: self.GetStorage(self.Frame, self.List)).pack(fill=X)
        if not self.RC.GetInfo(item[2]):
            EnterLog("RessourceView :: GetInfo :: ERROR:None object")
        else:
            EnterLog("RessourceView :: GetInfo :: SUCCESS")
