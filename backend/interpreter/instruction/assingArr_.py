from ..abstract.instruction import instruction
from ..abstract.types import ExpressionType

class AssignArr_(instruction):
    def __init__(self, line, column, id_, expression, expression2):
        super().__init__(line, column)
        self.id_ = id_
        self.expression = expression
        self.expression2 = expression2

    def Eject(self, env):
        tmp = env.GetArray(self.id_)
        if tmp == None:
            return
        
        elif tmp.const:
            print(f'Error: Array {self.id_} is constant \n column: {self.column} line: {self.line}')
            return

        index = self.expression.Eject(env)
        value = self.expression2.Eject(env)

        if index.Type != ExpressionType.INTEGER:
            print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            return

        tmp.Assign(index, value)
        return