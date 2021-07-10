from DNA import DnaSequence
from Data import Data
from Icommand import Icommand


class Slice_command(Icommand):

    def __init__(self):
        self.array_data = Data()

    def execute(self, args):
        try:
            identifier = args[0]
            identifier = identifier[1:]
            start_index=args[1]
            end_index=args[2]
            for i in self.array_data.currentData.items():
                if i[0] == int(identifier):
                    if args[4] == "@@":
                        name = i[1].get("name") + "_" + "s" + str(i[1].get("counter"))
                        i[1]["counter"] += 1
                        string = i[1]["string"].string
                        try:
                                string=string[int(start_index):int(end_index)]
                        except Exception as e:
                            return ("error", e)
                        break
                    else:
                        name = args[4]
                        string = i[1]["string"].string[start_index:end_index]
                        break
        except Exception as e:
            return ("error", e)
        dna = DnaSequence(string)
        id = self.array_data.insert_data(name, dna)
        if id != None:
            return "[{}]".format(id) + " " + name + " :" + "" + string
        return None

