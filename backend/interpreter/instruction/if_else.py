from ..abstract.instruction import instruction
from ..abstract.types import ExpressionType
from ..abstract.environment import Environment

class If_else(instruction):
    def __init__(self, line, column, condition, if_instructions, else_instructions):
        super().__init__(line, column)
        self.condition = condition
        self.if_instructions = if_instructions
        self.else_instructions = else_instructions

    def Eject(self, env):
        resultCondition = self.condition.Eject(env)
        if resultCondition.Type != ExpressionType.BOOLEAN:
            print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            return
        
        if resultCondition.value:
            env.envsCount += 1
            newEnv = Environment(env, f'{env.envsCount}-if')
            for instruction in self.if_instructions:
                instruction.Eject(newEnv)
            return
        
        elif self.else_instructions != None:
            env.envsCount += 1
            newEnv = Environment(env, f'{env.envsCount}-else')
            for instruction in self.else_instructions:
                instruction.Eject(newEnv)
            return
