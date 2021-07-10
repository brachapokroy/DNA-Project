from abc import abstractmethod


class Icommand:
    @abstractmethod
    def execute(self, *args,**kwargs):
        """calculates shape area."""
        pass


