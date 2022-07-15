from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Scrollbar, Treeview

from Logs import EnterLog


class SearchView:
    def __init__(self, sc):
        self.SC = sc
        self.Frame = Frame()
        self.TreeSearch = Treeview()
        self.List = []
        EnterLog("Init Search View")

    def AllSearch(self, list, root):
        self.Frame = root
        self.List = list

        for w in self.Frame.winfo_children():
            w.destroy()

        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeSearch = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Nom", "prix", "Fait"))
        for column in self.TreeSearch["columns"]:
            self.TreeSearch.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeSearch.heading(column, text=column)
        self.TreeSearch['show'] = 'headings'
        self.TreeSearch.bind("<Double-1>", self.InfoBuy)
        fait = None
        for s in list:
            if int(s.GetCheck()) == 1:
                fait = "OUI"
            else:
                fait = "NON"
            self.TreeSearch.insert('', END, values=(s.GetName(), str(s.GetPrice()*1.21)+"€", fait, s.GetID()))
        self.TreeSearch.pack(fill=X)
        sb.config(command=self.TreeSearch.yview)
        Button(self.Frame, text="Retour", command=self.SC.Retour).pack(fill=X)
        EnterLog("Search view :: AllSearch")

    def InfoBuy(self, event):
        item = self.TreeSearch.item(event.widget.selection())['values']
        EnterLog("you clicked on : " + item[0])
        for w in self.Frame.winfo_children():
            w.destroy()
        Label(self.Frame, text=self.SC.GetInfo(item[3]), font=("Arial", "20")).pack()
        if item[2] != "OUI":
            Button(self.Frame, text="Acheter", command=lambda: self.SC.Buy(item[3])).pack(fill=X)
        Button(self.Frame, text="retour", command=lambda: self.AllSearch(self.List, self.Frame)).pack(fill=X)
        if not self.SC.GetInfo(item[3]):
            EnterLog("RessourceView :: GetInfo :: ERROR:None object")
        else:
            EnterLog("RessourceView :: GetInfo :: SUCCESS")