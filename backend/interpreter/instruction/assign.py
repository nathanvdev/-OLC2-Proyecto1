from ..abstract.instruction import instruction

class Assign(instruction):
    def __init__(self, line, column, name, op, expression):
        super().__init__(line, column)
        self.name = name
        self.op = op
        self.expression = expression

    def Eject(self, env):

        value = self.expression.Eject(env)
        env.AssignVariable(self.name, self.op, value)
