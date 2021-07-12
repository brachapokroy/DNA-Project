from batch_command import Batch_command
from factory import factory
from run_batch_command import  Run_batch



class CLI:
    def __init__(self):
        self.factory = factory()
        self.run=Run_batch()
        self.batch_command=Batch_command()

    def run_command(self):
        batch_commands=[]
        val=""
        try:
            while val is not None:
                val = input("> cmd >>>")
                if val.split(" ")[0]!="batch" and "run" not in val:
                    print(self.factory.run_command(val))
                if val.split()[0]=="batch":
                    # if we get batch commands then it will append all commands at batch mode
                    batch_commands.append(val)
                    while val !="end" :
                        val = str(input("> batch >>>"))
                        batch_commands.append(val)
                    self.batch_command.execute(batch_commands)
                batch_commands=[]
                val=""
                if "run" in val:
                    print(self.run.execute(val))


        except Exception as e:
            return "error", e




if __name__ == '__main__':
    my_cli = CLI()
    my_cli.run_command()
