from ..abstract.instruction import instruction
from ..abstract.environment import Environment
from ..expression.primitive import Primitive
from ..abstract.types import ExpressionType

class for_(instruction):
    def __init__(self, line, column, assignment, condition, evalue, op, instructions):
        super().__init__(line, column)
        self.assignment = assignment
        self.condition = condition
        self.evalue = evalue
        self.op = op
        self.instructions = instructions


    def Eject(self, env:Environment):
        result = None
        env.envsCount += 1
        newEnv = Environment(env, f'{env.envsCount}-for')

        self.assignment.const = True
        self.assignment.Eject(newEnv)

        cycleCount = 0
        while True:
            cycleCount += 1
            if cycleCount > 1000:
                print('Error: Infinite loop')
                return
            
            if self.condition.Eject(newEnv).value != True:
                return
            
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

            if self.op == '+':
                newEnv.ForceAssignVariable(self.evalue.name, '+=', Primitive(self.line, self.column, 1, ExpressionType.INTEGER))
            elif self.op == '-':
                newEnv.ForceAssignVariable(self.evalue.name, '-=', Primitive(self.line, self.column, 1, ExpressionType.INTEGER))

        return result
            




        