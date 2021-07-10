import del_command
import dup_command
import load_command
import new_command
import pair_command
import save_command
import slice_command


class factory:
    def __init__(self):
        self.commands = {"new": new_command.New_command,
                         "load": load_command.Load_command,
                         "dup": dup_command.Dup_command,
                         "pair": pair_command.Pair_command,
                         "slice": slice_command.Slice_command,
                         "del": del_command.Del_command,
                         "save": save_command.Sava_command}

    def run_command(self, user_input):
        arr = []
        user_input = user_input.split()
        i = 0
        while i < len(user_input):
            arr.append(user_input[i])
            i += 1

        command = self.commands.get(arr[0])
        try:
            obj = command()
        except Exception as e:
            return "error", e
        return obj.execute(arr[1::])
