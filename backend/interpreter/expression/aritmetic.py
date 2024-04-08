from ..abstract.expression import expression
from .primitive import Primitive
from ..abstract.types import ExpressionType

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
        globalenv = env.GetGlobal()
        
        left = self.left.Eject(env)
        if hasattr(left, 'value'):
            while hasattr(left.value, 'Eject'):
                left = left.value.Eject(env)

        right = self.right.Eject(env)
        if hasattr(right, 'value'):
            while hasattr(right.value, 'Eject'):
                right = right.value.Eject(env)


        result = Primitive(self.line, self.column, None, None)
        result.Type = dominant_table[left.Type.value][right.Type.value]

        if self.operator == '+':
            if result.Type != ExpressionType.NULL:
                result.value = left.value + right.value
            else:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == '-':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                result.value = left.value - right.value
            else:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == '*':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                result.value = left.value * right.value
            else:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == '/':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                if right.value != 0:
                    result.value = left.value / right.value
                else:
                    newError = {
                        "Tipo": "Semantico",
                        "Linea": self.line,
                        "Columna": self.column,
                        "Ambito": env.name,
                        "Descricion": "Error de division por cero"
                    }
                    globalenv.Errors.append(newError)
                    print(f'Error: Division by zero \n column: {self.column} line: {self.line}')
            else:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')


        elif self.operator == '%':
            
            if result.Type != ExpressionType.INTEGER:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            else:
                if right.value != 0:
                    result.value = left.value % right.value
                else:
                    newError = {
                        "Tipo": "Semantico",
                        "Linea": self.line,
                        "Columna": self.column,
                        "Ambito": env.name,
                        "Descricion": "Error de division por cero"
                    }
                    globalenv.Errors.append(newError)
                    print(f'Error: Division by zero \n column: {self.column} line: {self.line}')
           

        elif self.operator == 'UMINUS':
            if result.Type != ExpressionType.NULL and result.Type != ExpressionType.STRING:
                result.value = -left.value
            else:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        return result
    


