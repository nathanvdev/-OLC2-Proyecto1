from ..abstract.instruction import instruction
from ..abstract.environment import Environment
from ..abstract.variables import Variables


class Declarate(instruction):
    def __init__(self, line, column, id, type, expression, const):
        super().__init__(line, column)
        self.id = id 
        self.type = type
        self.value = expression
        self.const = const

    def Eject(self, env: Environment):

        if self.value != None:
            self.value = self.value.Eject(env)
        
        
        if self.type != None and self.value != None:
            if self.type != self.value.Type:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return
        
        if self.type == None and self.value != None:
            self.type = self.value.Type

        newVar = Variables(self.id, self.type, self.value, self.const)


        env.SaveVariable(newVar)

