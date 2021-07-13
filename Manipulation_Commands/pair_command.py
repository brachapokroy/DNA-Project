from Dna.DNA import DnaSequence
from Icommand import Icommand
from functions import Functions


class Pair_command(Icommand, Functions):

    def __init__(self):
        pass

    def execute(self, args):
        try:
            # checks if it was sent by index or name
            identifier = self.find_identifier(args[0])
            iden = identifier[1:]
            if isinstance(identifier, int):  # if it's an id thn we will get it's data through his id
                i = self.find_by_idetifier_id(iden)
            elif isinstance(identifier, str):  # if it's a name then we will get it's data through his id
                i = self.find_by_idetifier_name(iden)
            if self.do_new_name(args) is True:  # checks if we are required to add a new name
                name = i[1].get("name") + "_" + "p" + str(i[1].get("counter")) #adds a new name based on the old one suffix with p and counter
                i[1]["counter"] += 1
                string = self.pair_with(i[1]["string"].string) #gets the paired string
            else:
                name = args[2]
                string = self.pair_with(i[1]["string"].string)
        except Exception as e:
            return ("error", e)

        # builds the new object and inserts it to our dict
        dna = DnaSequence(string)
        id = self.array_data.insert_data(name, dna)
        if id != None:
            return "[{}]".format(id) + " " + name + " :" + "" + string
        return None

    def pair_with(self, string):
        pair1 = "at"
        pair2 = "cg"
        pair3 = "AT"
        pair4 = "CG"
        strr = ""
        for i in string:
            if i in pair1:
                strr += list(filter(lambda x: (x != i), pair1))[0]
            elif i in pair2:
                strr += list(filter(lambda x: (x != i), pair2))[0]
            elif i in pair3:
                strr += list(filter(lambda x: (x != i), pair3))[0]
            elif i in pair4:
                strr += list(filter(lambda x: (x != i), pair4))[0]

        return strr
