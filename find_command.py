from DNA import DnaSequence
from Data import Data
from Icommand import Icommand
from functions import Functions


class Find_command(Icommand,Functions):
    counter = 0

    def __init__(self):
        self.array_data = Data()
        pass

    def execute(self, args):
        try:
            identifier = self.find_identifier(args[0])
            iden=args[0][1:]
            if isinstance(identifier, int):
                i = self.find_by_idetifier_id(iden)
            elif isinstance(identifier, str):
                i = self.find_by_idetifier_name(iden)
            if args[1][0]=="#":
                identifier1 = self.find_identifier(args[1])
                iden1 = args[1][1:]
                if isinstance(iden1, int):
                    j = self.find_by_idetifier_id(iden1)
                elif isinstance(iden1, str):
                    j = self.find_by_idetifier_name(iden1)
                if j[1]["string"].string in i[1]["string"].string:
                    index = i[1]["string"].string.find(j[1]["string"].string)
            else:
                if args[1] in i[1]["string"].string:
                    index=i[1]["string"].string.find(args[1])

        except Exception as e:
            return ("error", e)
        return index
