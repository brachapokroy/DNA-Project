from abc import abstractmethod

from Tools.demo.beer import n

from DNA import DnaSequence
from Data import Data
from Icommand import Icommand
from functions import Functions


class Sava_command(Icommand, Functions):
    counter = 0

    def __init__(self):
        self.array_data = Data()
        pass

    def execute(self, args):
        try:
            # checks if it was sent by index or name
            identifier = self.find_identifier(args[0])
            if isinstance(identifier, int):  # if it's an id thn we will get it's data through his id
                iden_values = self.find_by_idetifier_id(identifier)
            elif isinstance(identifier, str):  # if it's a name then we will get it's data through his id
                iden_values = self.find_by_idetifier_name(identifier)
                if len(args) > 1:
                    file1 = open(args[1], 'w')
                else:
                    file1 = open(iden_values[1].get("name") + ".rawdna", 'w')
                file1.write(iden_values[1]["string"].string)
                file1.close()
        except Exception as e:
            return "error", e
        return "managed to save to file"
