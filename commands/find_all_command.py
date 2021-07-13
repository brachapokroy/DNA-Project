from commands.find_command import Find_command
from functions import Functions
from dna.Data import Data


class Find_all_command(Functions):
    def __init__(self):
        self.find_all = Find_command()
        self.array_data = Data()
        pass

    def execute(self, args):
        try:
            indexes = []
            # checks if it was sent by index or name
            identifier = self.find_identifier(args[0])
            iden = args[0][1:]
            if isinstance(identifier, int):  # if it's an id thn we will get it's data through his id
                i = self.find_by_idetifier_id(iden)
            elif isinstance(identifier, str):  # if it's a name  then we will get it's data through his name
                i = self.find_by_idetifier_name(iden)
            #     checks it the sub string was sent by it's id ar as a string
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
            #     puts all the indexes of sub string in string in res
            res = [i for i in range(len(string)) if string.startswith(sub_string, i)]

        except Exception as e:
            return ("error", e)
        return res
