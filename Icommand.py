from abc import abstractmethod

# all classes thet inherit Icommand will implement an execute function
class Icommand:
    @abstractmethod
    def execute(self, *args,**kwargs):
        """calculates shape area."""
        pass


