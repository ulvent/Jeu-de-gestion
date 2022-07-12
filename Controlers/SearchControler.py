from Logs import EnterLog


class SearchControler:
    def __init__(self):
        self.Searches = []
        EnterLog("Init SearchControler")

    def ReadSearch(self):
        with open("Data/Save/Search.txt") as File:
            data = File.readlines()
