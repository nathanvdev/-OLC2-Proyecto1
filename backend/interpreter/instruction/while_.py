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
        result = None
        while True:
            bucleCount += 1

            condition = self.condition.Eject(env)

            if condition.Type != ExpressionType.BOOLEAN:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return result
            
            elif bucleCount > 1000:
                print('Error: Infinite loop detected')
                return result

            elif condition.value:
                env.envsCount += 1
                newEnv = Environment(env, f'{env.envsCount}-while')
                for instruction in self.instructions:
                    result = instruction.Eject(newEnv)

                    if result != None:
                        if result.Type == ExpressionType.BREAK:
                            break
                        elif result.Type == ExpressionType.CONTINUE:
                            break
                        elif result.Type == ExpressionType.RETURN:
                            return result

                if result != None:
                    if result.Type == ExpressionType.BREAK:
                        break
                    elif result.Type == ExpressionType.RETURN:
                        return result
                    
                return result
 
            elif not condition.value:
                break

            else:
                print(f'Error: Unknown error \n column: {self.column} line: {self.line}')
                return result
            
        return result

            

