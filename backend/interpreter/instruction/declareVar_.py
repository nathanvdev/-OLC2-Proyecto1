from ..abstract.instruction import instruction
from ..abstract.environment import Environment
from ..abstract.variables import Variables


class DeclareVar_(instruction):
    def __init__(self, line, column, id, type, expression, const):
        super().__init__(line, column)
        self.id = id 
        self.type = type
        self.value = expression
        self.const = const

    def Eject(self, env: Environment):
        globalenv = env.GetGlobal()
        if self.value != None:
            self.value = self.value.Eject(env)
        
        
        if self.type != None and self.value != None:
            if self.type != self.value.Type:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en la declaracion de variable"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return
        
        if self.type == None and self.value != None:
            self.type = self.value.Type

        newVar = Variables(self.line, self.column, self.id, self.type, self.value, self.const)


        env.SaveVariable(newVar)

        return

