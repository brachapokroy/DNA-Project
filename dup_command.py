from DNA import DnaSequence
from Data import Data
from Icommand import Icommand


class Dup_command(Icommand):
    counter = 0

    def __init__(self):
        self.array_data = Data()

    def execute(self, args):
        try:
            identifier = args[0]
            identifier = identifier[1:]
            for i in self.array_data.currentData.items():
                if i[0] == int(identifier):
                    if len(args) == 1:
                        name = i[1].get("name")+ "_" + str(i[1].get("counter"))
                        i[1]["counter"] += 1
                        string = i[1]["string"].string + i[1]["string"].string
                        break
                    else:
                        name = args[1]
                        string = i[1]["string"].string + i[1]["string"].string
                        break
        except Exception as e:
            return ("error", e)

        dna = DnaSequence(string)
        id = self.array_data.insert_data(name, dna)

        if id != None:
            return "[{}]".format(id) + " " + name + " :" + "" + string
        return None
