from dna.DNA import DnaSequence
from dna.Data import Data
from Icommand import Icommand
from functions import Functions


class Dup_command(Icommand, Functions):
    counter = 0

    def __init__(self):
        self.array_data = Data()

    def execute(self, args):
        try:
            # checks if it was sent by index or name
            identifier = self.find_identifier(args[0])
            if isinstance(identifier, int):  # if it's an id thn we will get it's data through his id
                i = self.find_by_idetifier_id(identifier)
            elif isinstance(identifier, str):  # if it's a name  then we will get it's data through his name
                i = self.find_by_idetifier_name(identifier)
                # checks if a name was sent or a new name will be defined
                if self.do_new_name(self, args):
                    name = i[1].get("name") + "_" + str(i[1].get("counter"))
                    i[1]["counter"] += 1
                else:
                    name = args[1]  # if a new name was sent
                string = i[1]["string"].string + i[1]["string"].string  # dups the string

        except Exception as e:
            return ("error", e)

        dna = DnaSequence(string)  # creates a new dna sequence
        id = self.array_data.insert_data(name, dna)
        if id != None:
            return "[{}]".format(id) + " " + name + " :" + "" + string
        return None
