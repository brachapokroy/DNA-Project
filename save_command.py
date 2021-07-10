from abc import abstractmethod

from Tools.demo.beer import n

from DNA import DnaSequence
from Data import Data
from Icommand import Icommand


class Sava_command(Icommand):
    counter = 0

    def __init__(self):
        self.array_data = Data()
        pass

    def execute(self, args):
        identifier = args[0]
        identifier = identifier[1:]
        try:
            for i in self.array_data.currentData.items():
                if i[0] == int(identifier):
                    if len(args)>2:
                        file1 = open(args[1], 'w')
                        file1.write(i[1]["string"].string)
                        file1.close()
                    else:
                        file1 = open(i[1].get("name")+".rawdna", 'w')
                        file1.write(i[1]["string"].string)
                        file1.close()

        except Exception as e:
            return ("error", e)
        return "managed to save to file"
