#Autor : Alexis Callens
import os
from datetime import datetime
from time import strftime


def EnterLog(chaine):
    with open("Data/Logs.txt", "a+") as File:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date += " : "
        date += chaine
        date += "\n"
        File.write(date)


def EraseLog():
    os.remove("Data/Logs.txt")