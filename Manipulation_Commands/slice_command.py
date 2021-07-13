from Dna.DNA import DnaSequence

from Icommand import Icommand
from functions import Functions


class Slice_command(Icommand, Functions):

    def __init__(self):
        # self.array_data = Functions.Data()
        pass

    def execute(self, args):
        try:
            identifier = self.find_identifier(args[0])
            iden = args[0][1:]
            start_index = args[1]
            end_index = args[2]
            if isinstance(identifier, int):
                i = self.find_by_idetifier_id(iden)
            elif isinstance(identifier, str):
                i = self.find_by_idetifier_name(iden)
            if self.do_new_name(args) is True:
                name = i[1].get("name") + "_" + "s" + str(i[1].get("counter"))
                i[1]["counter"] += 1
                string = i[1]["string"].string
                try:
                    string = string[int(start_index):int(end_index)]
                except Exception as e:
                    return ("error", e)
            else:
                name = args[4]
                string = i[1]["string"].string[start_index:end_index]
        except Exception as e:
            return ("error", e)
        dna = DnaSequence(string)
        id = self.array_data.insert_data(name, dna)
        if id != None:
            return "[{}]".format(id) + " " + name + " :" + "" + string
        return
