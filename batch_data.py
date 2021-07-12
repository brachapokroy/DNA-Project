class Batch_data:
    counter = 1
    Batches = {}

    def __init__(self):
        pass

    def insert_data(self, name,batch_commands):
        self.Batches[name] = batch_commands

