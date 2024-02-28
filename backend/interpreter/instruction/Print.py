from ..abtract.instruction import instruction

class Print(instruction):
    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression
        

    def Eject(self, env):
        value = self.expression.Eject(env)
        print(value.value)