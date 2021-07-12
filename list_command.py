from Data import Data
from Icommand import Icommand


class List(Icommand):
    def __init__(self):
        self.list_data = Data()
        pass

    def execute(self, args):
        arr=[]
        result = sorted(self.list_data.currentData.items(), key=lambda tup: tup[0])
        return result