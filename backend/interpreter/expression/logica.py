from ..abtract.expression import expression
from .primitive import Primitive
from ..abtract.types import ExpressionType

class Logica(expression):
    def __init__(self, line, column, left, right, operator):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.operator = operator

    def Eject(self, env):
        left = self.left.Eject(env)
        right = self.right.Eject(env)

        result = Primitive(self.line, self.column, None, ExpressionType.BOOLEAN)

        if left.Type != ExpressionType.BOOLEAN or right.Type != ExpressionType.BOOLEAN:
            print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            return result

        if self.operator == '&&':
            result.value = left.value and right.value

        elif self.operator == '||':
            result.value =  left.value or right.value

        elif self.operator == '!':
            result.value =  not left.value

        return result