from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

from Controlers.RecipeControler import RecipeControler
from Logs import EnterLog


class CompanyView:
    def __init__(self, cv, back, sc):
        self.CV = cv
        self.Frame = Frame()
        self.TreeCompany = Treeview()
        self.RC = RecipeControler(back, sc)
        EnterLog("Init CompanyView")

    def GetUsine(self, frame, list):
        self.Frame = frame
        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeCompany = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Nom", "Niveau"))
        for column in self.TreeCompany["columns"]:
            self.TreeCompany.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeCompany.heading(column, text=column)
        self.TreeCompany['show'] = 'headings'
        self.TreeCompany.bind("<Double-1>", self.GetRecipeByMachine)
        for m in list:
            self.TreeCompany.insert('', END, values=(m.GetName(), str(m.GetLevel()), m.GetID()))
        self.TreeCompany.pack(fill=X)
        sb.config(command=self.TreeCompany.yview)
        Button(self.Frame, text="Retour", command=self.CV.Retour).pack(fill=X)
        EnterLog("Companyview :: GetUsine")

    def GetRecipeByMachine(self, event):
        item = self.TreeCompany.item(event.widget.selection())['values']
        EnterLog("you clicked on : " + item[0])
        for w in self.Frame.winfo_children():
            w.destroy()
        self.RC.AllRecipeByList(self.Frame, self.RC.GetRecipesByMachine(int(item[2]), int(item[1])))

