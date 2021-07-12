
from Data import Data
from Icommand import Icommand
from functions import Functions


class Del_command(Icommand,Functions):
    counter = 0

    def __init__(self):
        self.array_data = Data()
        pass

    def execute(self, args):
        # checks if it was sent by index or name
        identifier = self.find_identifier(args[0])
        yes = "yY"
        no = "nN"
        try:

            if isinstance(identifier, int):# if it's an id thn we will get it's data through his id
                i = self.find_by_idetifier_id(identifier)
            elif isinstance(identifier, str): # if it's a name then we will get it's data through his id
                i = self.find_by_idetifier_name(identifier)
            confirm = input("do you really want to delete :" + i[1].get("name") + ":" + i[1]["string"].string + "?" + "please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
            while confirm not in yes and confirm not in no:
                confirm = input("please enter a valid char")
            if confirm in yes:
                del self.array_data.currentData[i[0]]
                print("deleted:" + "[{}]".format(i[0]) + i[1].get("name") + ":" + i[1]["string"].string)
                return
            elif confirm in no:
                print("Deletion was canceled")
                return
        except Exception as e:
            return "error", e
            print("this sequence does not exist")

        return
