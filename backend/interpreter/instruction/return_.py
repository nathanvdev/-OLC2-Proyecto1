from ..abstract.instruction import instruction
from ..abstract.types import ExpressionType

class Return_(instruction):
    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression

    def Eject(self, env):
        result = self.expression.Eject(env)
        result.Type = ExpressionType.RETURN
        return result