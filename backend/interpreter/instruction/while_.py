from ..abstract.instruction import instruction
from ..abstract.types import ExpressionType
from ..abstract.environment import Environment

class while_(instruction):
    def __init__(self, line, column, condition, instructions):
        super().__init__(line, column)
        self.condition = condition
        self.instructions = instructions


    def Eject(self, env):
        bucleCount = 0
        
        while True:
            bucleCount += 1

            condition = self.condition.Eject(env)

            if condition.Type != ExpressionType.BOOLEAN:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return
            
            elif bucleCount > 1000:
                print('Error: Infinite loop detected')
                return

            elif condition.value:
                env.envsCount += 1
                newEnv = Environment(env, f'{env.envsCount}-while')
                for instruction in self.instructions:
                    instruction.Eject(newEnv)
 
            elif not condition.value:
                break

            else:
                print(f'Error: Unknown error \n column: {self.column} line: {self.line}')
                return

            

