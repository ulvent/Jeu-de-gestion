from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

from Logs import EnterLog


class MachineView:
    def __init__(self, mc):
        self.Frame = Frame()
        self.MC = mc
        self.TreeMachine = Treeview()
        EnterLog("Init MachineView")

    def AllMachine(self, frame, list):
        for w in self.Frame.winfo_children():
            w.destroy()
        self.Frame = frame
        self.list = list
        sb = ttk.Scrollbar(self.Frame, orient='vertical')
        sb.pack(side=RIGHT, fill=Y)

        self.TreeMachine = Treeview(self.Frame, yscrollcommand=sb.set, columns=("Nom", "Niveau", "Prix"))
        for column in self.TreeMachine["columns"]:
            self.TreeMachine.column(column, anchor=CENTER)  # This will center text in rows
            self.TreeMachine.heading(column, text=column)
        self.TreeMachine['show'] = 'headings'
        self.TreeMachine.bind("<Double-1>", self.Upgrade)
        for m in list:
            price = round((m.GetPrice()*(m.GetLevel()+1))*1.21, 2)
            self.TreeMachine.insert('', END, values=(str(m.GetName()), str(m.GetLevel()), str(price)+"€", m.GetID(), price))
        self.TreeMachine.pack(fill=X)
        sb.config(command=self.TreeMachine.yview)
        Button(self.Frame, text="Retour", command= self.MC.Retour).pack(fill=X)
        EnterLog("Machine view :: AllMachine")

    def Upgrade(self, event):
        item = self.TreeMachine.item(event.widget.selection())['values']
        EnterLog("you clicked on : " + item[0])
        for w in self.Frame.winfo_children():
            w.destroy()
        Label(self.Frame, text=self.MC.GetInfo(item[3], float(item[4])), font=("Arial", 15)).pack(fill=X)
        Button(self.Frame, text="Améliorer", command=lambda: self.MC.Ameliorator(item[3], item[4])).pack(fill=X)
        Button(self.Frame, text="Retour", command=lambda : self.AllMachine(self.Frame, self.list)).pack(fill=X)