from dna.Data import Data

class Functions:
    def __init__(self):
        self.array_data = Data()

    def find_identifier(self,identifier):
        # checks if the user gave an id or name
        try:
            if identifier[0] == "#":
                return int(identifier[1:])
            elif identifier[0] =="@":
                return identifier[1:]
        except Exception as e:
            return "error", e
    # gets an id of a sequence and will return it's data from the dict
    def find_by_idetifier_id(self,id):
        for i in self.array_data.currentData.items():
            if i[0] == int(id):
                return i

    # gets an nabe of a sequence and will return it's data from the dict
    def find_by_idetifier_name(self,name):
        for i in self.array_data.currentData.items():
            if i[1].get("name")==name:
                return i

    # check's if a new name is required
    def do_new_name(self,args):
        for i in args:
            if i=="@@":
                return True


