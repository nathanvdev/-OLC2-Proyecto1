from ..abstract.expression import expression
from .primitive import Primitive
from ..abstract.types import ExpressionType

# The `dominant_table` is a 2D list that represents the dominant type resulting from arithmetic
# operations between two operands. Each row corresponds to the type of the left operand, and each
# column corresponds to the type of the right operand. The value at the intersection of a row and
# column represents the resulting dominant type when performing an arithmetic operation between
# operands of those types.
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
        
        # The function `Eject` performs arithmetic operations on two operands and handles error cases for
        # type mismatch and division by zero.
        
        # :param env: It seems like the code snippet you provided is a method called `Eject` within a
        # class. The method seems to handle arithmetic operations such as addition, subtraction,
        # multiplication, division, modulus, and unary minus on expressions represented by nodes in a tree
        # structure
        # :return: The function `Eject` returns the result of the operation performed based on the
        # operator specified in the code snippet. The result is an instance of the `Primitive` class with
        # the appropriate type and value calculated from the left and right operands.
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
    


