from ..abtract.expression import expression
from .primitive import Primitive
from ..abtract.types import ExpressionType


import copy

class Relational(expression):
    def __init__(self, line, column, left, right, operator):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.operator = operator

    def Eject(self, env):
        left = self.left.Eject(env)
        right = self.right.Eject(env)

        result = Primitive(self.line, self.column, None, ExpressionType.BOOLEAN)

        if left.Type != right.Type:
            print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            return result

        if self.operator == '==':
            result.value = left.value == right.value

        elif self.operator == '!=':
            result.value = left.value != right.value

        elif self.operator == '>':
            result.value = left.value > right.value

        elif self.operator == '>=':
            result.value = left.value >= right.value

        elif self.operator == '<':
            result.value = left.value < right.value

        elif self.operator == '<=':
            result.value = left.value <= right.value
        
        return result
