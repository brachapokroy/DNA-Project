# this class contains the data of every sequence it is a static dict so everyone can use it
class Data:
    counter = 1
    currentData = {}

    def __init__(self):
        pass
    #    inserts a new sequence to the dict
    def insert_data(self, name, dna):
        for i in dna.string:
            if i not in "ACGTacgt":
                return None
        data_object = {"name": name, "string": dna,"counter":1}
        Data.currentData[Data.counter] = data_object
        Data.counter += 1
        return Data.counter - 1
