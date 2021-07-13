from batch.batch_data import Batch_data
from Icommand import Icommand
from factory import factory

# run a specific batch
class Run_batch(Icommand):

    def __init__(self):
        self.batch_data = Batch_data()
        self.my_factory = factory()

    def execute(self, args):
        # to run all batch commands we must get the aray of commanda fron the batch_data where it is stored as a dictinary where the key is the name of the batch and the value is the array of commands
        batch_results=[]
        args=args.split()
        # getting batches value which is an array of commands
        commands = self.batch_data.Batches[args[1]]
        for i in commands:
            # runs every command in the array by the factory class
            batch_results.append("the result of command :{}".format(i)+" is :"+str(self.my_factory.run_command(i)))
        return batch_results
