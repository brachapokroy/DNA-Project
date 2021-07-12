from find_command import Find_command
from functions import Functions
from Data import Data


class Find_all_command(Functions):
    def __init__(self):
        self.find_all = Find_command()
        self.array_data = Data()
        pass

    def execute(self, args):
        try:
            indexes = []
            identifier = self.find_identifier(args[0])
            iden = args[0][1:]
            if isinstance(identifier, int):
                i = self.find_by_idetifier_id(iden)
            elif isinstance(identifier, str):
                i = self.find_by_idetifier_name(iden)
            if args[1][0] == "#":
                identifier1 = self.find_identifier(args[1])
                iden1 = args[1][1:]
                if isinstance(iden1, int):
                    j = self.find_by_idetifier_id(iden1)
                elif isinstance(iden1, str):
                    j = self.find_by_idetifier_name(iden1)
                sub_string = j[1]["string"].string
                string = i[1]["string"].string
            else:
                sub_string = args[1]
                string = i[1]["string"].string
            res = [i for i in range(len(string)) if string.startswith(sub_string, i)]

        except Exception as e:
            return ("error", e)
        Find_command.counter=0
        return res
