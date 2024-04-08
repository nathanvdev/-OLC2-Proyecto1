from ..abstract.instruction import instruction
from ..abstract.environment import Environment
from ..expression.primitive import Primitive
from ..abstract.types import ExpressionType
import copy


class for_(instruction):
    def __init__(self, line, column, assignment, condition, evalue, op, instructions):
        super().__init__(line, column)
        self.assignment = assignment
        self.condition = condition
        self.evalue = evalue
        self.op = op
        self.instructions = instructions


    def Eject(self, env:Environment):
        globalenv = env.GetGlobal()
        result = None
        env.envsCount += 1
        newEnv = Environment(env, f'{env.envsCount}-for')

        tmpAssignment = copy.deepcopy(self.assignment)
        tmpAssignment.const = True
        tmpAssignment.Eject(newEnv)

        cycleCount = 0
        while True:
            cycleCount += 1
            if cycleCount > 1000:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error en el ciclo for"
                }
                globalenv.Errors.append(newError)
                print('Error: Infinite loop')
                return
            
            if self.condition.Eject(newEnv).value != True:
                return
            
            for instruction in self.instructions:
                result = instruction.Eject(newEnv)

                if result != None and hasattr(result, 'tmpType'):
                    if result.tmpType == ExpressionType.BREAK:
                        break
                    elif result.tmpType == ExpressionType.CONTINUE:
                        break
                    elif result.tmpType == ExpressionType.RETURN:
                        return result

            if result != None and hasattr(result, 'tmpType'):
                if result.tmpType == ExpressionType.BREAK:
                    break
                elif result.tmpType == ExpressionType.RETURN:
                    return result

            if self.op == '+':
                newEnv.ForceAssignVariable(self.line, self.column, self.evalue.name, '+=', Primitive(self.line, self.column, 1, ExpressionType.INTEGER))
            elif self.op == '-':
                newEnv.ForceAssignVariable(self.line, self.column, self.evalue.name, '-=', Primitive(self.line, self.column, 1, ExpressionType.INTEGER))

        return result
            




        