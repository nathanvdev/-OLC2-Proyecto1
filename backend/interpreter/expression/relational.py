from ..abstract.expression import expression
from .primitive import Primitive
from ..abstract.types import ExpressionType





class Relational(expression):
    def __init__(self, line, column, left, right, operator):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.operator = operator

    def Eject(self, env):
        globalenv = env.GetGlobal()
        left = self.left.Eject(env)
        while hasattr(left.value, 'Eject'):
            left = left.value.Eject(env)

        right = self.right.Eject(env)
        while hasattr(right.value, 'Eject'):
                right = right.value.Eject(env)
            

        result = Primitive(self.line, self.column, None, ExpressionType.BOOLEAN)

        if left.Type != right.Type:
            newError = {
                "Tipo": "Semantico",
                "Linea": self.line,
                "Columna": self.column,
                "Ambito": env.name,
                "Descricion": "Error de tipo en la operacion relacional"
            }
            globalenv.Errors.append(newError)
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
