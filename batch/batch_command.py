from batch.batch_data import Batch_data
from Icommand import Icommand


class Batch_command(Icommand):
    def __init__(self):
        self.batch_data = Batch_data()
        pass

    def execute(self, args):
        # slices the first and last that contain the batch mode(at args[0]) and end command at args[-1]
        commands = args[1:-1]
        # inserts the batch commands to the main batch data dict inserting the batch name as key and commands array as value
        self.batch_data.insert_data(args[0].split()[1], commands)
