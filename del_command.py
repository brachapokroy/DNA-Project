from abc import abstractmethod

from Tools.demo.beer import n

from DNA import DnaSequence
from Data import Data
from Icommand import Icommand


class Del_command(Icommand):
    counter = 0

    def __init__(self):
        self.array_data = Data()
        pass

    def execute(self, args):
        identifier = args[0]
        identifier = identifier[1:]
        yes = "yY"
        no = "nN"
        try:
            for i in self.array_data.currentData.items():
                if i[0] == int(identifier):
                    confirm = input("do you really want to delete :" + i[1].get("name") + ":" + i[1]["string"].string + "?" + "please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
                    while confirm not in  yes and confirm not in no:
                        confirm = input("please enter a valid char")
                    if confirm in yes:
                        del self.array_data.currentData[int(identifier)]
                        print("deleted:" + "[{}]".format(identifier) + i[1].get("name") + ":" + i[1]["string"].string)
                        return
                    elif confirm in no:
                        print("Deletion was canceled")
                        return
        except Exception as e:
            return ("error", e)
        print("this sequence does not exist")

        return
