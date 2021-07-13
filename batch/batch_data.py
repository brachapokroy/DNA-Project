class Batch_data:
    counter = 1
    Batches = {}

    def __init__(self):
        pass

    def insert_data(self, name,batch_commands):
        # gets an array of commands for a certain batch and inserts to the main dict
        self.Batches[name] = batch_commands

