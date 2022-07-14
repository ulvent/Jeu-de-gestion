from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from Logs import EnterLog


class RecipeView:
    def __init__(self, rc):
        self.Frame = Frame()
        self.TreeRecipe = Treeview()
        self.RC = rc
        self.list = []
        EnterLog("Init RecipeView")

    def AllRecipesList(self, frame, list):
        self.Frame = frame
        self.list = list
        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeRecipe = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Produit", "Quantité"))
        for column in self.TreeRecipe["columns"]:
            self.TreeRecipe.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeRecipe.heading(column, text=column)
        self.TreeRecipe['show'] = 'headings'
        self.TreeRecipe.bind("<Double-1>", self.InfoProd)
        for r in list:
            self.TreeRecipe.insert('', END, values=(str(r.GetProduct()), str(r.GetQuantity()), r.GetID()))
        self.TreeRecipe.pack(fill=X)
        sb.config(command=self.TreeRecipe.yview)
        Button(self.Frame, text="Retour", command=lambda: self.RC.RetourCompany(self.Frame)).pack(fill=X)
        EnterLog("Recipe view :: AllRecipeList")

    def InfoProd(self, event):
        qt = IntVar()
        item = self.TreeRecipe.item(event.widget.selection())['values']
        EnterLog("you clicked on : " + item[0])
        r = self.RC.GetRecipeById(item[2])
        for w in self.Frame.winfo_children():
            w.destroy()
        Label(self.Frame, text=self.RC.GetInfo(item[2]), font=("Arial", 15)).pack(fill=X)
        entry = Entry(self.Frame, textvariable=qt)
        entry.pack(fill=X)
        entry.delete(0, END)
        entry.focus()
        Button(self.Frame, text="Produire", command=lambda: self.RC.Production(qt.get(), r)).pack(fill=X)
        Button(self.Frame, text="Retour", command=lambda: self.RC.AllRecipeByList(self.Frame, self.list)).pack(fill=X)

