from factory import factory


class CLI:
    def __init__(self):
        self.factory = factory()

    def run_command(self):
        val = input("> cmd >>>")
        while val is not None:
            print(self.factory.run_command(val))
            val = str(input("> cmd >>>"))



if __name__ == '__main__':
    my_cli=CLI()
    my_cli.run_command()