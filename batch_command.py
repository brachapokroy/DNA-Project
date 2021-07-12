from batch_data import Batch_data
from Icommand import Icommand


class Batch_command(Icommand):
    def __init__(self):
        self.batch_data = Batch_data()
        pass

    def execute(self, args):
        commands = args[1:-1]
        self.batch_data.insert_data(args[0].split()[1], commands)
