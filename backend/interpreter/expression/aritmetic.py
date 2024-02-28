from ..abtract.expression import expression
import copy

class Aritmetic(expression):
    def __init__(self, line, column, left, right, operator):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.operator = operator

    def Eject(self, env):
        left = self.left.Eject(env)
        right = self.right.Eject(env)

        result = copy.deepcopy(left)
        result.value = None

        if self.operator == '+':
            result.value = left.value + right.value

        elif self.operator == '-':
            result.value =  left.value - right.value

        elif self.operator == '*':
            result.value =  left.value * right.value

        elif self.operator == '/':
            result.value =  left.value / right.value

        elif self.operator == '%':
            result.value =  left.value % right.value

        elif self.operator == 'UMINUS':
            result.value =  left.value * -1

        return result