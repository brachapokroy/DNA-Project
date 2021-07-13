from dna.DNA import DnaSequence
from dna.Data import Data
from Icommand import Icommand


class Load_command(Icommand):
    def __init__(self):
        self.array_data = Data()

    def execute(self, args):
        try:
            file = args[0]  # get's file name from  args at the first place
            file1 = open(file, "r+")
            output = file1.read()
            file_name = file.split(".")[0]
            dna = DnaSequence(output)  # creates a new instance of dna based on what was read from the file
            id = self.array_data.insert_data(file_name, dna)
        except Exception as e:
            return ("error", e)
        if id is not None:
            if len(output) > 40:
                return "[{}]".format(id) + " " + file_name + " :" + "" + output[:32] + "..." + output[37:40]
            else:
                return "[{}]".format(id) + " " + file_name + " :" + "" + output
        return None
