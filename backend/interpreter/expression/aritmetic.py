from ..abtract.expression import expression
from .primitive import Primitive
from ..abtract.types import ExpressionType
import copy

dominant_table = [
    [ExpressionType.INTEGER,    ExpressionType.FLOAT,   ExpressionType.NULL,    ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.FLOAT,      ExpressionType.FLOAT,   ExpressionType.NULL,    ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.NULL,       ExpressionType.NULL,    ExpressionType.STRING,  ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.NULL,       ExpressionType.NULL,    ExpressionType.NULL,    ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.NULL,       ExpressionType.NULL,    ExpressionType.NULL,    ExpressionType.NULL,    ExpressionType.NULL],
]


class Aritmetic(expression):
    def __init__(self, line, column, left, right, operator):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.operator = operator

    def Eject(self, env):
        left = self.left.Eject(env)
        right = self.right.Eject(env)

        result = Primitive(self.line, self.column, None, None)
        result.Type = dominant_table[left.Type.value][right.Type.value]

        if self.operator == '+':
            if result.Type != ExpressionType.NULL:
                result.value = left.value + right.value
            else:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == '-':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                result.value = left.value - right.value
            else:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == '*':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                result.value = left.value * right.value
            else:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == '/':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                if right.value != 0:
                    result.value = left.value / right.value
                else:
                    print(f'Error: Division by zero \n column: {self.column} line: {self.line}')
            else:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')


        elif self.operator == '%':
            
            if result.Type == ExpressionType.INTEGER:
                        if right.value != 0:
                            result.Type = right.Type
                        else:
                            print(f'Error: Division by zero \n column: {self.column} line: {self.line}')
            else:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            


        elif self.operator == 'UMINUS':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                result.Type = right.Type
            else:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        return result
    


