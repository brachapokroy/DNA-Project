from Icommand import Icommand
from batch_data import Batch_data


class Batchlist(Icommand):
    def __init__(self):
        self.batch_data = Batch_data()
        pass

    def execute(self, args):
        return self.batch_data.Batches.keys()
