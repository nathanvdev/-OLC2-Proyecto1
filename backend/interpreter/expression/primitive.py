from ..abstract.expression import expression

class Primitive(expression):
    def __init__(self, line, column, value, Type):
        super().__init__(line, column)
        self.value = value
        self.Type = Type
        self.tmpType = Type

    def Eject(self, env):
        return self
