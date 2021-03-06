from dna.DNA import DnaSequence
from dna.Data import Data
from Icommand import Icommand


class New_command(Icommand):
    counter = 0

    def __init__(self):
        self.array_data = Data()
        pass

    def execute(self, args):
        string = args[0]
        if len(args) >= 2:
            name = args[1]
            name = name[1:]
        else:
            New_command.counter += 1
            name = "seq" + str(New_command.counter)
        dna = DnaSequence(string)
        # the id is the number of the sequence that has been added to the static dict
        id = self.array_data.insert_data(name, dna)
        if id != None:
            return "[{}]".format(id) + " " + name + " :" + "" + string
        return None
