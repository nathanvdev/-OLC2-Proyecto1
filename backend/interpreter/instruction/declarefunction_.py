from ..abstract.instruction import instruction
from ..abstract.types import ExpressionType
from ..instruction.return_ import Return_

class DeclareFunction_(instruction):
    def __init__(self,line, column, id_, params, returnType, instructions):
        super().__init__(line, column)
        self.id_ = id_
        self.params = params
        self.returnType = returnType
        self.instructions = instructions

    def Eject(self, env):
        globalenv = env.GetGlobal()
        if self.returnType is not None:
            if not isinstance(self.instructions[-1], Return_):
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error en la declaracion de la funcion"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Function {self.id_} must return a value \n\tcolumn: {self.column} line: {self.line}')
                return
                    
        env.SaveFunction(self.id_, self)

