from ..abstract.expression import expression
from ..abstract.types import ExpressionType
from ..expression.primitive import Primitive

class funcEmbebidas_(expression):
    def __init__(self, line, column, operator, expression):
        super().__init__(line, column)
        self.expression = expression
        self.operator = operator

        
    def Eject(self, env):
        globalenv = env.GetGlobal()
        if self.operator == "parseInt":
            result = self.expression.Eject(env)
            while hasattr(result.value, 'Eject'):
                result = result.value.Eject(env)
            try:
                newResult = Primitive(self.line, self.column, int(result.value), ExpressionType.INTEGER)
                return newResult
            except:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == "parseFloat":
            result = self.expression.Eject(env)
            while hasattr(result.value, 'Eject'):
                result = result.value.Eject(env)
            try:
                newResult = Primitive(self.line, self.column, float(result.value), ExpressionType.FLOAT)
                return newResult
            except:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == "toString":
            result = self.expression.Eject(env)
            if result == None:
                return None
            while hasattr(result.value, 'Eject'):
                result = result.value.Eject(env)
            try:
                newResult = Primitive(self.line, self.column, str(result.value), ExpressionType.STRING)
                return newResult
            except:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            
        elif self.operator == "toLowerCase":
            result = self.expression.Eject(env)
            while hasattr(result.value, 'Eject'):
                result = result.value.Eject(env)
            try:
                newResult = Primitive(self.line, self.column, str(result.value).lower(), ExpressionType.STRING)
                return newResult
            except:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == "toUpperCase":
            result = self.expression.Eject(env)
            while hasattr(result.value, 'Eject'):
                result = result.value.Eject(env)
            try:
                newResult = Primitive(self.line, self.column, str(result.value).upper(), ExpressionType.STRING)
                return newResult
            except:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')

        elif self.operator == "typeof":
            result = self.expression.Eject(env)
            while hasattr(result.value, 'Eject'):
                result = result.value.Eject(env)
            try:
                newResult = Primitive(self.line, self.column, result.Type.name , ExpressionType.STRING)
                return newResult
            except:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la operacion aritmetica"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')