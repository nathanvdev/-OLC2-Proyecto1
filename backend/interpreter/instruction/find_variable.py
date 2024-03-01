from ..abtract.instruction import instruction

class FindVariable(instruction):
    def __init__(self, line, column, name):
        super().__init__(line, column)
        self.name = name

    def Eject(self, environment):
        return environment.Get_Variable(self.name).value

   