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
        EnterLog("Init Search View")

    def AllSearch(self, list, root):
        self.Frame = root
        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeSearch = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Nom", "prix", "Fait"))
        for column in self.TreeSearch["columns"]:
            self.TreeSearch.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeSearch.heading(column, text=column)
        self.TreeSearch['show'] = 'headings'
        #self.TreeSearch.bind("<Double-1>", self.InfoBuy)
        fait = None
        for s in list:
            if int(s.GetCheck()) == 1:
                fait = "OUI"
            else:
                fait = "NON"
            self.TreeSearch.insert('', END, values=(s.GetName(), str(s.GetPrice())+"€", fait, s.GetID()))
        self.TreeSearch.pack(fill=X)
        sb.config(command=self.TreeSearch.yview)
        Button(self.Frame, text="Retour", command=self.SC.Retour).pack(fill=X)
        EnterLog("Search view :: AllSearch")