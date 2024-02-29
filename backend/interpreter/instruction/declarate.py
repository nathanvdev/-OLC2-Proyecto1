from ..abtract.instruction import instruction
from ..abtract.environment import Environment
class Declarate(instruction):
    def __init__(self, line, column, id, type, expression):
        super().__init__(line, column)
        self.id = id 
        self.type = type
        self.value = expression

    def Eject(self, env: Environment):
        if self.value != None:
            self.value = self.value.Eject(env)
        
        
        if self.type != None and self.value != None:
            if self.type != self.value.Type:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return
        
        if self.type == None and self.value != None:
            self.type = self.value.Type


        env.SaveVariable(self.id, self.value)
        print(f'Variable {self.id}')
