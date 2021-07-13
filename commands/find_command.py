from dna.Data import Data
from Icommand import Icommand
from functions import Functions


class Find_command(Icommand,Functions):
    counter = 0

    def __init__(self):
        self.array_data = Data()
        pass

    def execute(self, args):
        try:
            # checks if it was sent by index or name
            identifier = self.find_identifier(args[0])
            iden=args[0][1:]
            if isinstance(identifier, int): # if it's an id thn we will get it's data through his id
                i = self.find_by_idetifier_id(iden)
            elif isinstance(identifier, str): # if it's a name  then we will get it's data through his name
                i = self.find_by_idetifier_name(iden)
                #     checks it the sub string was sent by it's id ar as a string
            if args[1][0]=="#":
                identifier1 = self.find_identifier(args[1])
                iden1 = args[1][1:]
                if isinstance(iden1, int):# checks if it was sent by index or name
                    j = self.find_by_idetifier_id(iden1)
                elif isinstance(iden1, str):# if it's a name  then we will get it's data through his name
                    j = self.find_by_idetifier_name(iden1)
                if j[1]["string"].string in i[1]["string"].string:
                    index = i[1]["string"].string.find(j[1]["string"].string)# finds firs index of the substring in string
            else:
                if args[1] in i[1]["string"].string:
                    index=i[1]["string"].string.find(args[1])# finds firs index of the substr

        except Exception as e:
            return ("error", e)
        return index
