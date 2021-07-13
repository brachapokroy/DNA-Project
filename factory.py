from batch import batchlist
from commands import dup_command, find_command, find_all_command, list_command, load_command, new_command
from Management_Commands import del_command, save_command
from Manipulation_Commands import pair_command, slice_command

# this class in responsible for directing every command to it's implementing class
class factory:
    def __init__(self):
        self.commands = {"new": new_command.New_command,
                         "load": load_command.Load_command,
                         "dup": dup_command.Dup_command,
                         "pair": pair_command.Pair_command,
                         "slice": slice_command.Slice_command,
                         "del": del_command.Del_command,
                         "save": save_command.Sava_command,
                         "find": find_command.Find_command,
                         "find_all": find_all_command.Find_all_command,
                         "batchlist": batchlist.Batchlist,
                         "list": list_command.List
                         }

    def run_command(self, user_input):
        arr = []
        user_input = user_input.split()
        i = 0
        # append user input to an array after slicing it to words
        while i < len(user_input):
            arr.append(user_input[i])
            i += 1
        # builds an object of the command type
        command = self.commands.get(arr[0])
        try:
            obj = command()
        except Exception as e:
            return "error", e
        return obj.execute(arr[1::])
