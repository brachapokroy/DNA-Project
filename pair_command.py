from DNA import DnaSequence
from Data import Data
from Icommand import Icommand


class Pair_command(Icommand):

    def __init__(self):
        self.array_data = Data()

    def execute(self, args):
        try:
            identifier = args[0]
            identifier = identifier[1:]
            for i in self.array_data.currentData.items():
                if i[0] == int(identifier):
                    if args[2] == "@@":
                        name = i[1].get("name") + "_" + "p" + str(i[1].get("counter"))
                        i[1]["counter"] += 1
                        string = self.pair_with(i[1]["string"].string)
                        break
                    else:
                        name = args[2]
                        string = self.pair_with(i[1]["string"].string)
                        break
        except Exception as e:
            return ("error", e)

        dna = DnaSequence(string)
        id = self.array_data.insert_data(name, dna)

        if id != None:
            return "[{}]".format(id) + " " + name + " :" + "" + string
        return None

    def pair_with(self, string):
        pair1 = "at"
        pair2 = "cg"
        pair3="AT"
        pair4="CG"
        strr=""
        for i in string:
            if i in pair1:
                strr+=list(filter(lambda x: (x!=i) , pair1))[0]
            elif i in pair2:
                strr +=list(filter(lambda x: (x!=i) , pair2))[0]
            elif i in pair3:
                strr += list(filter(lambda x: (x != i), pair3))[0]
            elif i in pair4:
                strr +=list(filter(lambda x: (x != i), pair4))[0]

        return strr
